import logging
import json


def read_recipe(file_path):
    with open(file_path) as recipe_json_file:
        logging.info(f"Loading recipe from {file_path}")
        return json.load(recipe_json_file)
