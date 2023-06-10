import subprocess
import logging

def clean_project(config):
    
    logging.info(f'Cleaning up project at { config["root_directory"]+"/"+config["project_name"] }')
    
    subprocess.run(["resources/scripts/project_cleaner.sh", config["root_directory"], config["project_name"]])
    
    logging.info("Done")