from dotenv import load_dotenv
import os

def environ(name: str):
    load_dotenv()
    return os.environ[name]