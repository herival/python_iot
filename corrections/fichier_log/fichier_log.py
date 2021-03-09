import logging
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--message", type=str)
parser.add_argument("--level", type=str)
# parser.add_argument("--file", type=str)
args = parser.parse_args()

logging.basicConfig(
    filename='test.log',
    format='%(asctime)s \
            %(levelname)s \
            %(message)s ',
    level=logging.DEBUG)

if (args.level) == 'info':
    logging.info(args.message)
elif (args.level) == 'warning':
    logging.warning(args.message)
# logging.warning('Attention')