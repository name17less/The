import logging

from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware


class LoggingMiddleware(BaseMiddleware):

    @staticmethod
    async def logmessage(update: types.message):
        user = update.from_user.id
        text = update.text
        logging.info(f"{user}: {text}")

    async def on_process_message(self, message, data):
        await self.logmessage(message)
