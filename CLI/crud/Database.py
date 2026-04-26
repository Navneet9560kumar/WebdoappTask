"""
database.py
===========
MySQL se connect karo aur table banao.
Apna host, user, password, database name yahan daalo.
"""

import mysql.connector

# ─── Yahan apni MySQL details daalo ───────────────────
DB_CONFIG = {
    "host":     "localhost",
    "user":     "root",          
    "password": "Navneet@123", 
    "database": "school_db",     
}
# ──────────────────────────────────────────────────────



def get_connection():
    """
    Har function call pe naya MySQL connection deta hai.
    """
    conn = mysql.connector.connect(**DB_CONFIG)
    return conn


def create_database():
    """
    'school_db' database exist nahi karta toh bana do.
    Pehli baar chalao — sirf ek baar zaroori hai.
    """
    config_without_db = {k: v for k, v in DB_CONFIG.items() if k != "database"}
    conn = mysql.connector.connect(**config_without_db)
    cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_CONFIG['database']}")
    conn.commit()
    conn.close()
    print(f"✅ Database '{DB_CONFIG['database']}' ready!")


def create_table():
    """
    students table banao agar exist nahi karta.
    MySQL syntax — SQLite se thoda alag hai.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id      INT           AUTO_INCREMENT PRIMARY KEY,
            name    VARCHAR(100)  NOT NULL,
            age     INT           NOT NULL,
            course  VARCHAR(100)  NOT NULL,
            marks   FLOAT         NOT NULL
        )
    """)
    conn.commit()
    conn.close()
    print("✅ Table 'students' ready!")