from .config import load_templates_conifg

from jinja2 import Environment, FileSystemLoader
import logging
import os

from pprint import pprint

templates_configs = load_templates_conifg()

pprint(templates_configs)

file_loader = FileSystemLoader('resources/templates')
env = Environment(loader=file_loader)

def create_file_from_template(config, file_name):
    file_name = file_name.value

    logging.info(f"Creating {file_name} file")
    
    template_config = find_template_config(file_name)

    template = env.get_template(template_config.template_name)
    file_content = template.render(config)

    target_file_location = config["target_directory"] + "/" + template_config.target_location + "/" + file_name

    os.makedirs(os.path.dirname(target_file_location), exist_ok=True)

    with open(target_file_location, "w") as file:
        file.write(file_content)

    logging.info(f"Created {file_name} file")

def find_template_config(file_name):
    return [template_config for template_config in templates_configs if template_config.file_name == file_name][0]

def filename_to_template_name(filename):
    return filename + ".j2"