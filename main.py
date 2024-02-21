from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token="BOT_TOKEN")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.chat_join_request_handler()
async def start1(update: types.ChatJoinRequest):
    # we accept the user into the channel
    await update.approve()
    # the ability to send a message to the user
    #await bot.send_message(chat_id=update.from_user.id, text="bot message user")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
