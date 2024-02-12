import os
import sys
from dotenv import load_dotenv

load_dotenv()

absent_env_vars = []

TEST_DATABASE_PATH = os.environ['TEST_DATABASE_PATH'] \
    if "TEST_DATABASE_PATH" in os.environ else absent_env_vars.append('TEST_DATABASE_PATH')

if absent_env_vars:
    print("Absent environment variables:")
    print(', '.join(absent_env_vars))

    sys.exit(1)