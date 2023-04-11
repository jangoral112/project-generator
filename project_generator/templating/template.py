from dataclasses import dataclass
from enum import Enum

class FileName(Enum):
    JUSTFILE = ".justfile"
    DOT_ENV = ".dist.env"
    APPLICATION_PROPERTIES = "application.properties"
    DOCKER_COMPOSE = "docker-compose.yml"
    DOCKERFILE = "Dockerfile"

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))

# TODO check how to get it without setters
@dataclass
class TemplateConfig:
    file_name: FileName
    template_name: str
    target_location: str # TODO rename to directory location