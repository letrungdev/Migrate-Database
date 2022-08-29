import json
import sqlite3
import os
import config
from sqlite3 import Error


class ParseData:

    def __init__(self, obj):
        self.obj = obj

    def loads(self, data):
        if type(data) in (dict, list):
            return json.dumps(data, ensure_ascii=False)
        return data

    def get_tuple(self, keys):
        return tuple(self.loads(self.obj.get(o)) for o in keys)



class CouchDB2Sqlite:

    def __init__(self, username, password, database_couchdb, database_sqlite):
        self.username, self.password, self.database_couchdb, self.database_sqlite = username, password, database_couchdb, database_sqlite
        # self.export_data()
        self.delete_old_database()
        self.conn = sqlite3.connect(database_sqlite)
        self.cur = self.conn.cursor()
        self.create_database()

    def delete_old_database(self):
        if os.path.isfile(self.database_sqlite):
            os.remove(self.database_sqlite)

    def export_data(self):
        code = "curl -X GET http://{0}:{1}@127.0.0.1:5984/{2}/_all_docs?include_docs=true > {2}.json"
        os.system(code.format(self.username, self.password, self.database_couchdb))
        print(code.format(self.username, self.password, self.database_couchdb))

    def create_database(self):
        for sql_table in config.create_tables:
            try:
                self.cur.execute(sql_table)
            except Error as e:
                print(e)
        self.conn.commit()

    def insert_data(self):
        rows = json.load(open("{}.json".format(self.database_couchdb), encoding="utf8"))['rows']
        for row in rows:
            row = row["doc"]
            for table in config.columns:
                if row.get("type") == table:
                    self.cur.execute(config.insert[row.get("type")], ParseData(row).get_tuple(config.columns.get(row.get("type")).split(", ")))

        self.conn.commit()


CouchDB2Sqlite(config.username, config.password, config.database_couchdb, config.database_sqlite).insert_data()

