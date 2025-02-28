import logging
import time
import yaml

logging.basicConfig(
    filename="logs/automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def load_config(config_path = "config.yaml") -> dict:
    '''Load the configuration file'''
    try:
        with open(config_path, "r") as file:
            return yaml.safe_load(file)
    except Exception as e:
        logging.error(f"Error loading config file: {e}")
        return {}