from dataclasses import dataclass
from enum import Enum

class FileName(Enum):
    JUSTFILE = ".justfile"
    DOT_ENV = ".dist.env"
    DOCKER_COMPOSE = "docker-compose.yml"
    DOCKERFILE = "Dockerfile"

@dataclass
class Template:
    filename: FileName
    template_name: str
    target_location: str