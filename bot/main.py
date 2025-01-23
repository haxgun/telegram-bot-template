import asyncio
import datetime

from aiogram.types import BotCommand, BotCommandScopeDefault
from loguru import logger
from bot.config import bot, admins, dp
from bot.handlers import register_handler

# Function to set up the command menu (default for all users)
async def set_commands() -> None:
    """
    Sets the default command for all users when they start the bot.
    """
    commands = [BotCommand(command='start', description='Start')]
    await bot.set_my_commands(commands, BotCommandScopeDefault())

# Function that will execute when the bot starts
async def start_bot() -> None:
    """
    Sends a message to the admins when the bot starts.
    Also sets up the default commands.
    """
    await set_commands()
    await register_handler(dp)
    for admin_id in admins:
        try:
            message = (f'🤖 Hello! I am running 🥳\n'
                       f'⏰ Launched in {datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")}\n')
            await bot.send_message(admin_id, message)
        except Exception as e:
            logger.error(f"Failed to send message to admin {admin_id}: {e}")
            pass
    logger.info("Bot successfully started.")

# Function that will execute when the bot stops
async def stop_bot() -> None:
    """
    Sends a message to the admins when the bot stops.
    """
    try:
        for admin_id in admins:
            message = (f'🤖 Bot is stopped. Why? 😔\n'
                       f'⏰ Launched in {datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")}\n')
            await bot.send_message(admin_id, message)
    except Exception as e:
        logger.error(f"Failed to send message to admin {admin_id}: {e}")
        pass
    logger.error("Bot stopped!")

async def main() -> None:
    """
    Registers startup and shutdown functions and starts the bot with long polling.
    """
    # Registering the startup and shutdown functions
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    # Starting the bot with long polling
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await bot.session.close()

if __name__ == "__main__":
    # Run the main async function
    asyncio.run(main())
