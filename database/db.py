import sqlite3

DB_NAME = "database/scanner.db"


# Initialize Database
def init_db():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    # Users Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    # Scan History Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS scans(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        target TEXT,
        hostname TEXT,
        risk TEXT,
        scan_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


# Save Scan Result
def save_scan(target, hostname, risk):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO scans(target, hostname, risk)
    VALUES(?,?,?)
    """, (target, hostname, risk))

    conn.commit()
    conn.close()


# Get Scan History
def get_history():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM scans
    ORDER BY scan_date DESC
    """)

    data = cursor.fetchall()

    conn.close()

    return data


# Create User
def create_user(username, password):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    try:

        cursor.execute("""
        INSERT INTO users(username,password)
        VALUES(?,?)
        """, (username, password))

        conn.commit()

    except sqlite3.IntegrityError:

        print("Username already exists")

    finally:

        conn.close()


# Get User
def get_user(username):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM users
    WHERE username=?
    """, (username,))

    user = cursor.fetchone()

    conn.close()

    return user


# Total Scans Count
def get_total_scans():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    SELECT COUNT(*)
    FROM scans
    """)

    total = cursor.fetchone()[0]

    conn.close()

    return total


# High Risk Count
def get_critical_count():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    SELECT COUNT(*)
    FROM scans
    WHERE risk='HIGH'
    """)

    count = cursor.fetchone()[0]

    conn.close()

    return count


# Get Latest Scan
def get_latest_scan():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM scans
    ORDER BY id DESC
    LIMIT 1
    """)

    scan = cursor.fetchone()

    conn.close()

    return scan


# Delete Scan
def delete_scan(scan_id):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM scans
    WHERE id=?
    """, (scan_id,))

    conn.commit()

    conn.close()


# Delete User
def delete_user(user_id):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM users
    WHERE id=?
    """, (user_id,))

    conn.commit()

    conn.close()


# Get All Users
def get_all_users():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM users
    ORDER BY id DESC
    """)

    users = cursor.fetchall()

    conn.close()

    return users