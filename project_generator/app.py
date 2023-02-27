import project_generator.template as template

from jinja2 import Environment, FileSystemLoader
from os import getcwd, path, remove
import subprocess
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s | %(message)s')

def run():
    logging.info("Started Project Generator")

    config = get_config()

    create_spring_project(config["main_projects_directory"], config["project_name"])

    create_files_from_templates(config)

    clean_up_unwanted_files(config)

    logging.info("Done")

# General configuration

def get_config():
    config = {
        "main_projects_directory": "/home/jgoral/Documents/projects",
        "project_name": "sample-project", 
        "server_port": 8989 
    }
    
    config["target_directory"] = config["main_projects_directory"] + "/" + config["project_name"]

    return config

def get_target_dir(project_name):
    return path.dirname(getcwd()) + "/" + project_name

# Run spring cli to create project

def create_spring_project(main_projects_directory, project_name):
    logging.info("Creating Spring boot project...")

    subprocess.run(["resources/scripts/spring_cli_init.sh", main_projects_directory, project_name])

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