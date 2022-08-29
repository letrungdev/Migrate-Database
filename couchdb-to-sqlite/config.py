# Config
username = 'admin'
password = 'pass'
database_couchdb = "dunno-envi"
database_sqlite = "envi_test.db"


columns = {
            "e_envi": "id, e, m, p",
            "e_vien": "id, e, m, p",
            "envi": "id, word, keyword, pronounce, snym, word_family, content, freq, conjugation, topic",
            "grammar": "id, level, tag, title, tag, key, related, contents",
            "topic": "id, name, path, total",
            "vien": "id, word, pronounce_vi, content"
            }

# Create table
create_tables = [""" CREATE VIRTUAL TABLE "e_envi" USING fts4(id, e, m, p, notindexed=p) """,
                 """ CREATE VIRTUAL TABLE "e_vien" USING fts4(id, e, m, p, notindexed=p) """,
                 """ CREATE VIRTUAL TABLE "envi" USING fts4(id ,word ,keyword ,pronounce ,snym, word_family ,content,freq , conjugation, topic, notindexed=pronounce, notindexed=snym, notindexed=word_family, notindexed=content, notindexed=freq,notindexed=conjugation)""",
                 """ CREATE TABLE grammar( id integer PRIMARY KEY, level text, title text, tag text, key text, related text, contents text ) """,
                 """ CREATE TABLE topic( id integer PRIMARY KEY, name TEXT, path TEXT , total INT) """,
                 """ CREATE VIRTUAL TABLE "vien" USING fts4(id,word ,pronounce ,content , notindexed=content) """
                 ]


# Insert
insert = {
    "e_envi": """INSERT INTO e_envi
                      (id, e, m, p)
                      VALUES (?, ?, ?, ?);""",
    "e_vien": """INSERT INTO e_vien
                          (id, e, m, p)
                          VALUES (?, ?, ?, ?);""",

    "envi": """INSERT INTO envi
                          (id, word, keyword, pronounce, snym, word_family, content, freq, conjugation, topic)
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""",

    "grammar": """INSERT INTO grammar
                          (id, level, tag, title, tag, key, related, contents)
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?);""",

    "topic": """INSERT INTO topic
                          (id, name, path, total)
                          VALUES (?, ?, ?, ?);""",

    "vien": """INSERT INTO vien
                          (id, word, pronounce, content)
                          VALUES (?, ?, ?, ?);"""
}



