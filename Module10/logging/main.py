import logging

from another_module import log_me

logging.basicConfig(
    level=logging.INFO,
    filename="app.log",
    format="%(asctime)s: %(name)s: %(levelname).4s - %(message)s",
)

logger = logging.getLogger("main")

logger.info("today is Thursday")
logger.warning("Not Friday")

log_me()
