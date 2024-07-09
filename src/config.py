import logging.config
import os

from decouple import config  # type: ignore

from src.common.utils.singleton import Singleton


class Config(metaclass=Singleton):
    DATABASE_URL = config("DATABASE_URL", cast=str)
    LOG_LEVEL = config("LOG_LEVEL", default="INFO", cast=str)
    TITLE = "FastAPI Clean Architecture"
    VERSION: str = "0.1.0"
    OPENAPI_URL: str = "/openapi.json"
    DOCS_URL: str = "/docs"
    REDOC_URL: str = "/redoc"
    ROOT_PATH: str = "/"


class DevelopmentConfig(Config):
    LOG_LEVEL = config("LOG_LEVEL", default="DEBUG", cast=str)


class StagingConfig(Config):
    pass


class ProductionConfig(Config):
    pass


def config_factory(environment: str) -> type[Config]:
    configs = {
        "development": DevelopmentConfig,
        "staging": StagingConfig,
        "production": ProductionConfig,
    }
    return configs[environment]


def get_config() -> type[Config]:
    environment = os.getenv("ENVIRONMENT", "development")
    app_config = config_factory(environment)

    LOGGING = {
        "version": 1,
        "disable_existing_loggers": True,
        "formatters": {
            "standard": {
                "format": (
                    "[%(asctime)s] %(levelname)s "
                    "[%(name)s.%(funcName)s:%(lineno)d] "
                    "%(message)s"
                ),
                "datefmt": "%Y-%m-%d %H:%M:%s",
            }
        },
        "handlers": {
            "stdout_logger": {
                "formatter": "standard",
                "class": "logging.StreamHandler",
            }
        },
        "loggers": {
            "": {  # root
                "level": app_config.LOG_LEVEL,
                "handlers": ["stdout_logger"],
                "propagate": False,
            }
        },
    }
    logging.config.dictConfig(LOGGING)
    return app_config
