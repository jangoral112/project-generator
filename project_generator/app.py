import project_generator.template as template

from jinja2 import Environment, FileSystemLoader
from os import getcwd, path, remove
import subprocess
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s | %(message)s')

def run():
    logging.info("Started Project Generator")

    config = get_config()

    create_spring_project(config)

    create_files_from_templates(config)

    clean_up_unwanted_files(config)

    logging.info("Done")

# General configuration

def get_config():
    config = { 
        "project_name": "sample-project", 
        "server_port": 8989 
    }
    
    config["target_directory"] = get_target_dir(config["project_name"])

    return config

def get_target_dir(project_name):
    return path.dirname(getcwd()) + "/" + project_name

# Run spring cli to create project

def create_spring_project(config):
    logging.info("Creating Spring boot project...")

    subprocess.run([f"resources/scripts/spring_cli_init.sh", config["target_directory"]])

# Creating files from templates

def create_files_from_templates(config):
    filenames = [
        ".justfile",
        ".dist.env",
        "docker-compose.yml",
        "Dockerfile"
    ]

    for filename in filenames:
        template.create_file_from_template(config, filename)

# Clean up

def clean_up_unwanted_files(config):
    logging.info("Cleaning up unwanted files")

    logging.info("Removing HELP.md file")
    remove(config["target_directory"] + "/" + "HELP.md")