import sqlite3
from my_database import connect_to_db


def create_page(page):
    conn = connect_to_db()
    cursor = conn.cursor()
    statement = 'INSERT INTO ourmedia_page_info(created_at, page_id, page_name) VALUES (?,?,?)'
    cursor.execute(statement, [page['created_at'], page['page_id'], page['page_name']])
    conn.commit()


def create_video(video):
    conn = connect_to_db()
    cursor = conn.cursor()
    statement = 'INSERT INTO ourmedia_video_info(created_at, video_id, video_title, page_id) VALUES (?,?,?,?)'
    cursor.execute(statement, [video['created_at'], video['video_id'], video['video_title'], video['page_id']])
    conn.commit()


def create_insight(insight):
    conn = connect_to_db()
    cursor = conn.cursor()
    statement = 'INSERT INTO ourmedia_video_insight(created_at, id, video_id, video_likes, video_views) VALUES (?,?,?,?,?)'
    cursor.execute(statement,
                   [insight['created_at'], insight['id'], insight['video_id'], insight['video_likes'], insight['video_views']])
    conn.commit()


def update_insight(insight):
    conn = connect_to_db()
    cursor = conn.cursor()
    statement = 'UPDATE ourmedia_video_insight SET video_likes=?, video_views=? WHERE video_id = ?'
    cursor.execute(statement, [insight['video_likes'], insight['video_views'], insight['video_id']])
    conn.commit()


def get_pages():
    conn = connect_to_db()
    cursor = conn.cursor()
    statement = 'SELECT created_at, page_id, page_name FROM ourmedia_page_info'
    cursor.execute(statement)
    conn.commit()
    return cursor.fetchall()


def get_videos():
    conn = connect_to_db()
    cursor = conn.cursor()
    statement = 'SELECT created_at, video_id, video_title, page_id FROM ourmedia_video_info'
    cursor.execute(statement)
    conn.commit()
    return cursor.fetchall()


def get_insights():
    conn = connect_to_db()
    cursor = conn.cursor()
    statement = 'SELECT created_at, id, video_id, video_likes, video_views FROM ourmedia_video_insight'
    cursor.execute(statement)
    conn.commit()
    return cursor.fetchall()


def get_insights_by_video(video_id):
    conn = connect_to_db()
    cursor = conn.cursor()
    statement = 'SELECT created_at, id, video_id, video_likes, video_views FROM ourmedia_video_insight WHERE video_id = ? '
    cursor.execute(statement, [video_id])
    conn.commit()
    return cursor.fetone()


def delete_page(page_id):
    conn = connect_to_db()
    cursor = conn.cursor()
    statement = 'DELETE FROM ourmedia_page_info WHERE page_id = ?'
    cursor.execute(statement, [page_id])
    conn.commit()


def delete_video(video_id):
    conn = connect_to_db()
    cursor = conn.cursor()
    statement = 'DELETE FROM ourmedia_video_info WHERE video_id = ?'
    cursor.execute(statement, [video_id])
    conn.commit()


def delete_insight(video_id):
    conn = connect_to_db()
    cursor = conn.cursor()
    statement = 'DELETE FROM ourmedia_video_insight WHERE video_id = ?'
    cursor.execute(statement, [video_id])
    conn.commit()
