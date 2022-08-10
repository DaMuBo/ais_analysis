"""
Managing Database operations like creating backups, getting data and so on.
"""

from subprocess import PIPE, Popen
from pathlib import Path


def create_backup(host,port, db, user, password, filename, pg_dump_path ='C:/Program Files/' ):
    """
    Creating a Backup file from the specified database
    """
    pg_dump = sorted(Path(pg_dump_path).glob('**/bin/pg_dump.exe'))[0]
    pg_path = pg_dump.parent
    dumper = Path("./pg_dump")
    cmd = f'''cd "{str(pg_path)}" && {str(dumper)} --dbname={db} -h {host} -p {port} -U {user} -f {str(filename)}'''
    popen = Popen(cmd,stdin=PIPE,stderr=PIPE, universal_newlines=True, shell=True)
    return popen.communicate(f"{password}\n")
          
def load_backup(host,port, db, user, password, filename, pg_dump_path ='C:/Program Files/'):
    """
    Loading the backUp in the given Database
    """
    pg_dump = sorted(Path(pg_dump_path).glob('**/bin/psql.exe'))[0]
    pg_path = pg_dump.parent
    dumper = Path("./psql")
    cmd = f'''cd "{str(pg_path)}" && type {str(filename)} | {str(dumper)} --dbname={db} -h {host} -p {port} -U {user} '''
    print(cmd)
    popen = Popen(cmd,stdin=PIPE,stderr=PIPE, universal_newlines=True, shell=True)
    return popen.communicate(f"{password}\n")