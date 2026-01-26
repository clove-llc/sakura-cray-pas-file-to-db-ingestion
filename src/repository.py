import sqlite3
from pathlib import Path

DB_PATH = Path("data/db/app.db")


def insert_analog_test_results(df):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.executemany(
        """
        INSERT INTO analog_test_results (
            resipe_id, task_id, temperature_c, operator, test_date
        ) VALUES (?, ?, ?, ?, ?)
        """,
        df.values.tolist(),
    )

    conn.commit()
    conn.close()
