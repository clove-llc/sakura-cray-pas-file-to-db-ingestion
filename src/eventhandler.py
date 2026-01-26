import time
import logging

from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from src.config.config import SUPPORTED_EXT, ANALOG_RAW_DIR, INSTRUMENT_RAW_DIR
from src.config.logging_config import setup_logging
from src.handler.analog_test import handle_analog_test

setup_logging()
logger = logging.getLogger(__name__)


class EventHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        path = Path(str(event.src_path))
        logger.info("File detected: %s", path)

        if path.name.startswith("~$"):
            logger.error("Is a temporary file: %s", path.name)
            return

        if path.suffix.lower() not in SUPPORTED_EXT:
            logger.error("Unsupported file extension: %s", path.name)
            return

        if "analog_test" in path.parts:
            logger.info("Analog test result detected: %s", path)

            try:
                handle_analog_test(path)
            except Exception as e:
                logger.exception("Failed to process analog test file: %s", path)
                logging.exception("Error: %s", e)
        elif "instrument_analysis" in path.parts:
            logger.info("Analyzer result detected: %s", path)
            # handle_instrument_analysis(path)
        else:
            logger.warning("Unknown data type: %s", path)


observer = Observer()
observer.schedule(EventHandler(), path=str(ANALOG_RAW_DIR), recursive=True)
observer.schedule(EventHandler(), path=str(INSTRUMENT_RAW_DIR), recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()
