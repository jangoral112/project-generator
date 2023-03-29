from .templating import create_file_from_template, FileName

from os import getcwd, path, remove, makedirs
import subprocess
import logging


def run():
    logging.info("Started Project Generator")

    config = get_config()

    create_spring_project(config["main_projects_directory"], config["project_name"])

    create_files_from_templates(config)

    create_additional_directory_structure(config)

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
    logging.info("Creating files from tempaltes")
    
    file_names = [
        FileName.JUSTFILE,
        FileName.DOT_ENV,
        FileName.DOCKER_COMPOSE,
        FileName.DOCKERFILE
    ]

    for file_name in file_names:
        create_file_from_template(config, file_name)

# Create missing directory structure e.g. docker/database/docker-entrypoint-initdb.d

def create_additional_directory_structure(config):
    logging.info("Creating missing directory structure")

    makedirs(config["target_directory"] + "/" + "docker/database/docker-entrypoint-initdb.d", exist_ok=True)

# Clean up

def clean_up_unwanted_files(config):
    logging.info("Cleaning up unwanted files")

    logging.info("Removing HELP.md file")
    remove(config["target_directory"] + "/" + "HELP.md")
    
    logging.info("Removing gradlew.bat file")
    remove(config["target_directory"] + "/" + "gradlew.bat")