
import os
from typing import List
import psycopg2

from dotenv import load_dotenv


load_dotenv()


def get_db_connection():
    conn = psycopg2.connect(host=os.environ['POSTGRES_HOST'],
                            database=os.environ['POSTGRES_DB'],
                            user=os.environ['POSTGRES_USERNAME'],
                            password=os.environ['POSTGRES_PASSWORD'])
    return conn


def all_notices():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM notices')
    notices = cur.fetchall()

    cur.close()
    conn.close()
    return notices


def find_notice_by_title(title: str) -> List[tuple]:
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM notices where title = %s', [title])
    notices = cur.fetchall()

    cur.close()
    conn.close()
    return notices


def create_notice(notice):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO notices (title, link, created_at, updated_at) VALUES (%s, %s, %s, %s)",
                (notice['title'], notice['link'], notice['date'], notice['date']))
    conn.commit()

    cur.close()
    conn.close()
