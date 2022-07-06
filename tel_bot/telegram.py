import json
import os
import requests
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token="TokenBot")
dp = Dispatcher(bot, storage=MemoryStorage())

url = "DomainUrl"


class Reg(StatesGroup):
    login = State()
    password = State()


@dp.message_handler(commands=['start'], state='*')
async def process_start_command(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton(text="Начать регистрацию")
    keyboard.add(button_1)
    await message.reply("Привет!\n Нажми на кнопку регистрации!", reply_markup=keyboard)


@dp.message_handler(state=Reg.login)
async def echo_message(msg: types.Message, state: FSMContext):
    res = requests.get(f'{url}/api/names/?search={msg.text}')
    if res.text == '[]':
        await bot.send_message(msg.from_user.id, 'Логин верний. \nВведите пароль')
        await state.update_data(username=msg.text)
        await Reg.password.set()
    else:
        await bot.send_message(msg.from_user.id, 'Такой логин уже зареестрований')


@dp.message_handler(state=Reg.password)
async def echo_message(msg: types.Message, state: FSMContext):
    if len(msg.text) >= 8:
        await state.update_data(password=msg.text)
        user_data = await state.get_data()
        print(user_data)
        res = requests.post(f'{url}/api/register/', data=user_data)
        if res.status_code == 201:
            data = {}
            data['user'] = json.loads(res.text)['id']
            data['name'] = msg.chat.first_name
            data['user_name'] = msg.chat.username
            data['user_telegram_id'] = msg.chat.id
            res = requests.post(f'{url}/api/register-info/', data=data)
            await bot.send_message(msg.from_user.id, 'Регистрация пройдена!')
        else:
            if res.text:
                await bot.send_message(msg.from_user.id, f'Ошибка\n {res.text} \n Попробуйте заново')
            else:
                await bot.send_message(msg.from_user.id, f'Ошибка , не здавайся пробуй еще!')
        await state.finish()
    elif len(msg.text) < 6:
        await bot.send_message(msg.from_user.id, 'Пароль слишком короткий')


@dp.message_handler(lambda message: message.text == "Начать регистрацию", state='*', )
async def echo_message(msg: types.Message, state: FSMContext):
    await bot.send_message(msg.from_user.id, "Придумайте логин")
    await Reg.login.set()


@dp.message_handler(state='*', )
async def echo_message(msg: types.Message, state: FSMContext):
    await bot.send_message(msg.from_user.id, "Я не понимаю, выберите команду")


if __name__ == '__main__':
    executor.start_polling(dp)
