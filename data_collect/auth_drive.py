import json
from yaml import safe_load
from pydrive.auth import GoogleAuth
from loguru import logger
import os
from sys import stderr

loglevel = os.getenv("LOGLEVEL", "INFO").upper()
logger.remove()
logger.add(stderr, level=loglevel)

class Config:
    def __init__(self, config_path="../config.yaml"):
        with open(config_path) as f:
            self.complete = safe_load(f)
            self.credentials = self.complete.get("credentials")

def auth_gdrive(client_secrets_path, cache_file="../credentials/cached_google_credentials.txt"):
    gauth = GoogleAuth()

    # Try to load cached client credentials, else launch webserver to auth
    gauth.LoadCredentialsFile(cache_file)
    gauth.DEFAULT_SETTINGS['client_config_file'] = client_secrets_path
    if gauth.credentials is None:
        logger.debug("No GDrive credentials cache found. Initializating GDrive Web Server Auth")
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        logger.debug("Refreshing Gdrive Access token.")
        gauth.Refresh()
    else:
        logger.debug("Credentials cache found.")
        gauth.Authorize()
    # Save the current credentials to a file
    gauth.SaveCredentialsFile(cache_file)

    return gauth
