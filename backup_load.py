"""
Wrapping the loading of the backup function and getting the configurations from the connection files
"""
import sys
from pathlib import Path

import yaml

from functions.utils import get_folder
from functions.database import load_backup

if __name__ == '__main__':
    curr_folder = get_folder()
    filepath = Path(sys.argv[1])
    with open(curr_folder / "connections.yml", encoding='utf-8') as file:
        db_config = yaml.safe_load(file)
    load_backup(db_config["host"],db_config["port"],db_config["db"],db_config["user"],db_config["password"],filepath)
