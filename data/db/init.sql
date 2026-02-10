CREATE TABLE IF NOT EXISTS analog_test_results (
    id SERIAL PRIMARY KEY,
    recipe_id TEXT NOT NULL,
    task_id TEXT NOT NULL,
    temperature_c DOUBLE PRECISION,
    operator TEXT,
    test_date DATE
);
