from aiogram import Dispatcher, Bot
from aiogram.utils import executor
import random

bot = Bot(token="YOUR_BOT_TOKEN")
dp = Dispatcher(bot)
state = {}


def echo_command(msg):
    text = msg['text'].strip()
    response = text[4:].strip()  # Удаляем '/эхо' из текста команды
    bot.send_message(chat_id=msg['chat']['id'], text=response)


def roll_command(msg):
    if 'waiting_for_roll' in state and state['waiting_for_roll']:
        try:
            roll_number = int(msg['text'])
            random_number = random.randint(1, 6)

            if roll_number > random_number:
                winner = 'Вы победили!'
            elif roll_number < random_number:
                winner = 'Bot победил!'
            else:
                winner = 'Ничья!'

            state['waiting_for_roll'] = False
            bot.send_message(chat_id=msg['chat']['id'], text=winner)
        except ValueError:
            state['waiting_for_roll'] = False
            bot.send_message(chat_id=msg['chat']['id'], text='Пожалуйста, введите число.')
    else:
        state['waiting_for_roll'] = True
        bot.send_message(chat_id=msg['chat']['id'], text='Введите число для броска костей.')


def on_message(msg):
    text = msg['text']
    if text.startswith('/эхо'):
        echo_command(msg)
    elif text.startswith('/кости'):
        roll_command(msg)
    else:
        state['waiting_for_roll'] = False
        bot.send_message(chat_id=msg['chat']['id'], text='Еще не научился разговаривать уверенно')


dp.register_message_handler(on_message, content_type='text')


if __name__ == '__main__':  # конструкция для запуска бота.
    executor.start_polling(dp, skip_updates=True)
