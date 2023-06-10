import logging

import sys

logging.basicConfig(level=logging.INFO, format='%(levelname)s | %(message)s')

from project_generator import app

if __name__ == '__main__':
    app.run(sys.argv[1])