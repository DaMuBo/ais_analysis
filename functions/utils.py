from pathlib import Path

def get_folder():
    """
    returns the actual project folder and makes it easy for file handlings
    """
    
    return Path.cwd()