from aiogram import Bot, Dispatcher
import config

print(config.BOT_TOKEN)

bot = Bot(token=config.BOT_TOKEN, parse_mode='html')

dp = Dispatcher(bot=bot)
