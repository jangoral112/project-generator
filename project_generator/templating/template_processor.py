from jinja2 import Environment, FileSystemLoader
import logging


file_loader = FileSystemLoader('resources/templates')
env = Environment(loader=file_loader)

def create_file_from_template(config, filename):
    logging.info(f"Creating {filename} file")

    template_name = filename_to_template_name(filename)
    template = env.get_template(template_name)
    file_content = template.render(config)

    with open(config["target_directory"] + "/" + filename, "w") as file:
        file.write(file_content)

    logging.info(f"Created {filename} file")

def filename_to_template_name(filename):
    return filename + ".j2"