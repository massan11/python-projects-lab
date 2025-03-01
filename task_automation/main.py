import argparse
import logging
import yaml
import schedule
import time
from tasks import file_operations, data_processing

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
    
def execute_task(task_name, config):
    if task_name == "file_operations":
        file_operations.organize_files(config.get("file_operations", {}))
    # elif task_name == "data_processing":
    #     data_processing.process_data(config.get("data_processing", {}))
    else:
        print(f"Task '{task_name}' not found.")
        logging.warning(f"Unknown task: {task_name}")

# CLI Argument Parsing
def main():
    parser = argparse.ArgumentParser(description="Task Automation Script")
    parser.add_argument("task", help="Specify the task to execute (e.g., file_operations, data_processing)")
    args = parser.parse_args()

    config = load_config()
    execute_task(args.task, config)

if __name__ == "__main__":
    main()