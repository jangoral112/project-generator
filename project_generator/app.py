from .recipe import read_recipe

from .tasks import generate_project, clean_project

import logging


def run(app_task):
    logging.info("Started Project Generator")
    logging.info(f"Task: {app_task}")
    
    config = get_config()

    match app_task:
        case "generate":
            generate_project(config)
        case "clean":
            clean_project(config)
        case _:
            raise ValueError("No argument provided. Available task: generate, clean ")

# Load configuration 

def get_config():
    config = read_recipe("./test/resources/recipe.json")

    config["target_directory"] = config["root_directory"] + "/" + config["project_name"]

    return config