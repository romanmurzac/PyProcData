import logging

logger = logging.getLogger("PDDLogger")
logging.basicConfig(
    filename='docs/pdd_logs.log',
    encoding='utf-8',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p'
    )
