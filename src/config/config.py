from pathlib import Path

DATA_DIR = Path("data")

ANALOG_RAW_DIR = DATA_DIR / "incoming" / "analog_test" / "raw"
INSTRUMENT_RAW_DIR = DATA_DIR / "incoming" / "instrument_analysis" / "raw"

SUPPORTED_EXT = {".xlsx", ".xls", ".csv"}
