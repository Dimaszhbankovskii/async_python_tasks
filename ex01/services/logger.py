import sys
import logging
from logging import StreamHandler, Formatter


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


handler = StreamHandler(stream=sys.stdout)
format = Formatter(fmt='[%(asctime)s: %(levelname)s] %(message)s')

handler.setFormatter(format)
logger.addHandler(handler)
