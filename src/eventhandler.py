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
        logger.info("ファイルを検出しました: %s", path)

        if path.name.startswith("~$"):
            logger.error("一時ファイルです: %s", path.name)
            return

        if path.suffix.lower() not in SUPPORTED_EXT:
            logger.error("サポートされていない形式のファイルです: %s", path.name)
            return

        if "analog_test" in path.parts:
            logger.info("アナログ試験結果を検出しました: %s", path)

            try:
                handle_analog_test(path)
            except Exception as e:
                logger.exception(
                    "アナログ試験結果の解析中にエラーが発生しました: %s", path
                )
                logging.exception("エラー: %s", e)
        elif "instrument_analysis" in path.parts:
            logger.info("分析機器の試験結果を検出しました: %s", path)
            # handle_instrument_analysis(path)
        else:
            logger.warning("不明なデータ型です: %s", path)


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
