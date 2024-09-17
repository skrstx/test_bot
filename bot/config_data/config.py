from environs import Env
from dataclasses import dataclass


@dataclass
class TgBot:
    token: str


@dataclass
class RedisData:
    host: str
    port: int


@dataclass
class Config:
    tg_bot: TgBot
    redis: RedisData


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)

    return Config(tg_bot=TgBot(token=env("BOT_TOKEN")),
                  redis=RedisData(host=env("REDIS_HOST"),
                                  port=env.int("REDIS_PORT")))
