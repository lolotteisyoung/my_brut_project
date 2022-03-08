import sqlite3
from my_database import connect_to_db


def create_page(page):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        statement = 'INSERT INTO ourmedia_page_info(created_at, id, name) VALUES (?,?,?)'
        cursor.execute(statement, [page['created_at'], page['id'], page['name']])
        conn.commit()
    except:
        conn.rollback()
    finally:
        conn.close()


def create_video(video):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        statement = 'INSERT INTO ourmedia_video_info(created_at, id, title, page_id) VALUES (?,?,?,?)'
        cursor.execute(statement, [video['created_at'], video['id'], video['title'], video['page_id']])
        conn.commit()
    except:
        conn.rollback()
    finally:
        conn.close


def create_insight(insight):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        statement = 'INSERT INTO ourmedia_video_insight(created_at, id, video_id, likes, views) VALUES (?,?,?,?,?)'
        cursor.execute(statement,
                       [insight['created_at'], insight['id'], insight['video_id'], insight['likes'], insight['views']])
        conn.commit()
    except:
        conn.rollback()
    finally:
        conn.close()

def update_insight(insight):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        statement = 'UPDATE ourmedia_video_insight SET likes=?, views=? WHERE id = ?'
        cursor.execute(statement, [insight['likes'], insight['views'], insight['id']])
        conn.commit()
    except:
        conn.rollback()
    finally:
        conn.close()


def get_pages():
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        statement = 'SELECT created_at, id, name FROM ourmedia_page_info'
        cursor.execute(statement)
        conn.commit()
        return cursor.fetchall()
    except:
        conn.rollback()
    finally:
        conn.close()


def get_videos():
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        statement = 'SELECT created_at, id, title, page_id FROM ourmedia_video_info'
        cursor.execute(statement)
        conn.commit()
        return cursor.fetchall()
    except:
        conn.rollback()
    finally:
        conn.close()


def get_insights():
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        statement = 'SELECT created_at, id, video_id, likes, views FROM ourmedia_video_insight'
        cursor.execute(statement)
        conn.commit()
        return cursor.fetchall()
    except:
        conn.rollback()
    finally:
        conn.close()


def get_insights_by_video(id):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        statement = 'SELECT created_at, id, video_id, likes, views FROM ourmedia_video_insight WHERE id = ? '
        cursor.execute(statement, [id])
        conn.commit()
        return cursor.fetone()
    except:
        conn.rollback()
    finally:
        conn.close()


def delete_page(id):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        statement = 'DELETE FROM ourmedia_page_info WHERE id = ?'
        cursor.execute(statement, [id])
        conn.commit()
    except:
        conn.rollback()
    finally:
        conn.close()


def delete_video(id):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        statement = 'DELETE FROM ourmedia_video_info WHERE id = ?'
        cursor.execute(statement, [id])
        conn.commit()
    except:
        conn.rollback()
    finally:
        conn.close()


def delete_insight(id):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        statement = 'DELETE FROM ourmedia_video_insight WHERE id = ?'
        cursor.execute(statement, [id])
        conn.commit()
    except:
        conn.rollback()
    finally:
        conn.close()
