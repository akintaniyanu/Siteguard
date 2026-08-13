import sqlite3


DATABASE = "siteguard.db"


def get_connection():
    connection = sqlite3.connect(DATABASE)

    connection.row_factory = sqlite3.Row

    return connection


def create_tables():

    connection = get_connection()

    # Table for scan results
    connection.execute("""
        CREATE TABLE IF NOT EXISTS scans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            domain TEXT NOT NULL,
            score INTEGER,
            scanned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Table for domains managed by SiteGuard
    connection.execute("""
        CREATE TABLE IF NOT EXISTS domains (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            domain TEXT UNIQUE NOT NULL,
            added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()


def save_scan(domain, score):

    connection = get_connection()

    connection.execute(
        """
        INSERT INTO scans (domain, score)
        VALUES (?, ?)
        """,
        (domain, score)
    )

    connection.commit()
    connection.close()


def get_scan_history():

    connection = get_connection()

    scans = connection.execute(
        """
        SELECT domain, score, scanned_at
        FROM scans
        ORDER BY scanned_at DESC
        """
    ).fetchall()

    connection.close()

    return scans


def add_domain(domain):

    connection = get_connection()

    try:

        connection.execute(
            """
            INSERT INTO domains (domain)
            VALUES (?)
            """,
            (domain,)
        )

        connection.commit()

        return True

    except sqlite3.IntegrityError:

        return False

    finally:

        connection.close()


def get_domains():

    connection = get_connection()

    domains = connection.execute(
        """
        SELECT id, domain, added_at
        FROM domains
        ORDER BY added_at DESC
        """
    ).fetchall()

    connection.close()

    return domains


def delete_domain(domain_id):

    connection = get_connection()

    connection.execute(
        """
        DELETE FROM domains
        WHERE id = ?
        """,
        (domain_id,)
    )

    connection.commit()

    connection.close()
