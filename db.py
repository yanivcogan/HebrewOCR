import mysql.connector

suppress_db = 0

if not suppress_db:
    my_db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="akevot"
    )
    my_cursor = my_db.cursor()


def save_docs(name, path_to_img, path_to_pdf, text, avg_conf):
    if suppress_db:
        return
    sql = """INSERT INTO
                docs (`name`, `image`, `pdf`, `text`, `conf`)
                VALUES (%s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                `name` = VALUES(`name`),
                `image` = VALUES(`image`),
                `pdf` = VALUES(`pdf`),
                `text` = VALUES(`text`),
                `conf` = VALUES(`conf`)"""
    val = (name, path_to_img, path_to_pdf, text, avg_conf)
    my_cursor.execute(sql, val)


def commit():
    if suppress_db:
        return
    my_db.commit()
