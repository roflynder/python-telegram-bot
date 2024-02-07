import os

from telebot import TeleBot
from telebot import types

from database import User

bot = TeleBot(os.getenv("BOT_TOKEN"))


@bot.message_handler(commands=["start"])
def start_bot(message: types.Message):
    """Run bot
    """

    user = User().create(
        id=message.from_user.id,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
        username=message.from_user.username
    )

    print(user)

    text = "Welcome"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=["users"])
def get_users(message: types.Message):
    """
    Get Users
    """
    users = User().get_all()
    text = "\n".join(users)

    bot.send_message(message.chat.id, text)


if __name__ == "__main__":
    bot.polling()