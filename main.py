import logging
import time
from watchdog.observers import Observer

from src.config.config import ANALOG_RAW_DIR, INSTRUMENT_RAW_DIR
from src.config.logging_config import setup_logging
from src.event_handler import EventHandler

setup_logging()
logger = logging.getLogger(__name__)


def main():
    logger.info("フォルダ監視を開始します。")

    observer = Observer()

    # アナログ試験結果フォルダの監視登録
    observer.schedule(EventHandler(), path=str(ANALOG_RAW_DIR), recursive=True)

    # 分析機器試験結果フォルダの監視登録
    observer.schedule(EventHandler(), path=str(INSTRUMENT_RAW_DIR), recursive=True)

    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()


if __name__ == "__main__":
    main()
