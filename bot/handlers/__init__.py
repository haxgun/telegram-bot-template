import importlib
import os
from pathlib import Path
from typing import List

from aiogram import Dispatcher

from bot.config import BASE_DIR

HANDLERS_DIR = BASE_DIR / "bot" / "handlers"


def get_files(directory: Path) -> List[str]:
    return [
        file.split('.py')[0]
        for file in os.listdir(directory)
        if file.endswith('.py') and file != '__init__.py'
    ]


async def register_handler(dp: Dispatcher) -> None:
    handlers = get_files(HANDLERS_DIR)

    for handler_name in handlers:
        module_path = f"app.handlers.{handler_name}"
        module = importlib.import_module(module_path)

        if hasattr(module, "router"):
            dp.include_router(module.router)
