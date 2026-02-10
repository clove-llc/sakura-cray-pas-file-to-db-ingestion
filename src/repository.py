from src.config.postgres import get_connection


def insert_analog_test_results(df):
    sql = """
        INSERT INTO analog_test_results (
            recipe_id, task_id, temperature_c, operator, test_date
        ) VALUES (%s, %s, %s, %s, %s)
    """

    records = df.values.tolist()

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.executemany(sql, records)
