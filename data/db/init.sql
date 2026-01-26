CREATE TABLE IF NOT EXISTS analog_test_results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    resipe_id TEXT NOT NULL,
    task_id TEXT NOT NULL,
    temperature_c REAL,
    operator TEXT,
    test_date TEXT
);