import logging

# Configure logging
logging.basicConfig(
    filename='logs/test_execution.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log(message):
    logging.info(message)
