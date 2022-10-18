from dotenv import load_dotenv
import os
load_dotenv()
DOMAIN_NAME = os.environ.get("DOMAIN_NAME")
ALGO = os.environ.get("ALGO")
AUDIENCE = os.environ.get("AUDIENCE")
