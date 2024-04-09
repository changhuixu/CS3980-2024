from logging.handlers import TimedRotatingFileHandler
from logging import StreamHandler, basicConfig, INFO


def setup_logging():
    console_log = StreamHandler()
    file_log = TimedRotatingFileHandler("./logs/app.log", when="d", interval=1)
    basicConfig(
        level=INFO,
        format="%(asctime)s %(levelname).4s %(name)s:%(lineno)d %(message)s",
        handlers=[console_log, file_log],
    )
