from aiogram import Bot, Dispatcher, executor, types

from sertgen import gen_sert

API_TOKEN = '5107384529:AAGbGtZ22lUKB08CYAYkJJJ3Ghb3QsMgqSk'

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_cert(message: types.Message):
    """
    This handler will be called when user sends `/start` command
    """
    try:
        await message.bot.send_document(message.chat.id, gen_sert(message.from_user.id))
    except Exception as ex:
        await message.bot.send_message(message.chat.id, str(ex))


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/help` command
    """
    await message.bot.send_message(message.chat.id, "Скачайте OpenVpn, получите файл и подключите его в приложении "
                                                    "OpenVpn")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
