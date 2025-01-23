import importlib
import os
from pathlib import Path
from typing import List

from aiogram import Dispatcher
from bot.config import BASE_DIR

# Directory where handler modules are stored
HANDLERS_DIR = BASE_DIR / "bot" / "handlers"


def get_files(directory: Path) -> List[str]:
    """
    Retrieves the list of Python files (excluding __init__.py) in the given directory.

    Args:
        directory (Path): The directory to scan for Python files.

    Returns:
        List[str]: A list of filenames (without extensions) of the Python files in the directory.
    """
    return [
        file.split('.py')[0]
        for file in os.listdir(directory)
        if file.endswith('.py') and file != '__init__.py'
    ]


async def register_handler(dp: Dispatcher) -> None:
    """
    Dynamically imports and registers all handlers found in the HANDLERS_DIR directory.

    Args:
        dp (Dispatcher): The Dispatcher instance to which the routers should be included.
    """
    handlers = get_files(HANDLERS_DIR)

    for handler_name in handlers:
        # Build the module path based on the handler file name
        module_path = f"app.handlers.{handler_name}"

        # Dynamically import the handler module
        module = importlib.import_module(module_path)

        # Check if the module has a 'router' attribute and include it in the dispatcher
        if hasattr(module, "router"):
            dp.include_router(module.router)
