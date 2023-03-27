from .template import FileName
from .template import TemplateConfig

import yaml
import logging


def load_templates_conifg():
    logging.info("Loading templates configs")

    templates_config_file = open("resources/config/templates.yml")
    config_as_yaml = yaml.safe_load(templates_config_file)
    templates_config_file.close()

    templates_configs = list(map(dict_to_template_config, config_as_yaml["templates"]))

    logging.info("Verifing existance of configs for available files")
    verify_configuration_for_files_exist(templates_configs)

    logging.info("Done with loading configs")
    return templates_configs
    
def verify_configuration_for_files_exist(templates_config):
    for file_name in FileName.list():
        found_file_configurations = list(filter(lambda template_config: template_config.file_name == file_name, templates_config))

        if len(found_file_configurations) != 1:
            raise ConfigurationValidationError(f"Invalid number of configurations for file {file_name}, there should be only 1: {len(found_file_configurations)}")

def dict_to_template_config(input_dict):
    return TemplateConfig(input_dict["file_name"], input_dict["template_name"], input_dict["target_location"])

class ConfigurationValidationError(Exception):
    def __init__(self, message):            
        super().__init__(message)