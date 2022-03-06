import os
import sqlite3
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


def connect_to_db():
    db = os.environ.get("MY_SQL_DB")
    try:
        conn = sqlite3.connect(db)
        print("🏠 the database has been created/connexion to the database has been successfull")
        return conn

    except:
        print(f"‼ Failed to connect to the database {db}")


def create_table():
    page_table = """CREATE TABLE IF NOT EXISTS ourmedia_page_info(
    created_at TIMESTAMP,
    page_id INTEGER PRIMARY KEY,
    page_name TEXT)"""
    video_table = """CREATE TABLE IF NOT EXISTS ourmedia_video_info(
    created_at TIMESTAMP,
    video_id INTEGER PRIMARY KEY,
    video_title TEXT,
    "page_id INTEGER, FOREIGN KEY(page_id) REFERENCES ourmedia_page_info(page_id)")"""
    insight_table = """CREATE TABLE IF NOT EXISTS ourmedia_insight_video(
    created_at TIMESTAMP,
    id INTEGER PRIMARY KEY,
    "video_id INTEGER, FOREIGN KEY(video_id) REFERENCES ourmedia_video_info(video_id)"
    video_likes INTEGER,
    video_views INTEGER)"""

    conn = connect_to_db()
    cursor = conn.cursor()

    try:
        cursor.execute(page_table)
        print("🔖 the table ourmedia_page_info has been successfully added to the database")
    except:
        print("‼ Failed to create the table ourmedia_page_info")

    try:
        cursor.execute(video_table)
        print("🔖 the table ourmedia_video_info has been successfully added to the database")
    except:
        print("‼ Failed to create the table ourmedia_video_info")

    try:
        cursor.execute(insight_table)
        print("🔖 the table ourmedia_video_insight has been successfully added to the database")
    except:
        print("‼ Failed to create the table ourmedia_video_insight")

    finally:
        conn.close()


if __name__ == '__main__':
    connect_to_db()
    create_table()
