import logging
from pathlib import Path
from src.excel_reader import read_analog_test_excel
from src.repository import insert_analog_test_results

logger = logging.getLogger(__name__)


def handle_analog_test(path: Path):
    logger.info("Start processing analog test file: %s", path.name)

    df = read_analog_test_excel(path)
    insert_analog_test_results(df)

    logger.info("Inserted %d records from %s", len(df), path.name)
