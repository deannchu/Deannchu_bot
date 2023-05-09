from aiogram import Router
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import CallbackQuery, Message
from aiogram.utils.markdown import hbold, hunderline, hcode, hlink
from lexicon_ru import LEXICON
from keyboards import news_kb, sub_unsub_keyboard, sub_keyboard, unsub_keyboard
import json
import asyncio
import re

# ---- Файлы для записи пользователей, подписавшихся на рассылку
joinedFile_all = open("id_all_news.txt","r")
joinedUsers_all = set()
for line in joinedFile_all:
    joinedUsers_all.add(line.strip())
joinedFile_all.close()

joinedFile_main = open("id_main_news.txt","r")
joinedUsers_main = set()
for line in joinedFile_main:
    joinedUsers_main.add(line.strip())
joinedFile_main.close()

joinedFile_spb = open("id_spb_news.txt","r")
joinedUsers_spb = set()
for line in joinedFile_spb:
    joinedUsers_spb.add(line.strip())
joinedFile_spb.close()

joinedFile_int = open("id_int_news.txt","r")
joinedUsers_int = set()
for line in joinedFile_int:
    joinedUsers_int.add(line.strip())
joinedFile_int.close()

joinedFile_polit = open("id_polit_news.txt","r")
joinedUsers_polit = set()
for line in joinedFile_polit:
    joinedUsers_polit.add(line.strip())
joinedFile_polit.close()

joinedFile_econ = open("id_econ_news.txt","r")
joinedUsers_econ = set()
for line in joinedFile_econ:
    joinedUsers_econ.add(line.strip())
joinedFile_econ.close()

router: Router = Router()

# Этот хэндлер будет срабатывать на команду "/start" -
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(LEXICON[message.text])

# Этот хэндлер будет срабатывать на команду "/help"
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(LEXICON[message.text])

# Этот хэндлер будет срабатывать на команду "/contact"
@router.message(Command(commands='contact'))
async def process_contact_command(message: Message):
    await message.answer(LEXICON[message.text])

# Этот хэндлер будет срабатывать на команду "/news"
@router.message(Command(commands='news'))
async def process_news_command(message: Message):
    await message.answer(text=LEXICON[message.text], reply_markup = news_kb)

# Этот хэндлер будет срабатывать на нажатие кнопки "Все новости"
@router.message(Text(text=LEXICON['all_news']))
async def get_all_news(message: Message):
    with open("all_news_dict.json") as file:
        all_news_dict = json.load(file)

    for k, v in reversed(all_news_dict.items()): 
        news = f"{hbold(v['time'])}\n" \
            f"{hlink(v['title'], v['url'])}" 
        await message.answer(news)

# Этот хэндлер будет срабатывать на нажатие кнопки "Главные новости"
@router.message(Text(text=LEXICON['main_news']))
async def get_main_news(message: Message):
    with open("main_news_dict.json") as file:
        main_news_dict = json.load(file)

    for k, v in reversed(main_news_dict.items()):
        news = f"{hlink(v['title'], v['url'])}" 
        await message.answer(news)

# Этот хэндлер будет срабатывать на нажатие кнопки "Санкт-Петурбург"
@router.message(Text(text=LEXICON['spb_news']))
async def get_spb_news(message: Message):
    with open("spb_news_dict.json") as file:
        spb_news_dict = json.load(file)

    for k, v in reversed(spb_news_dict.items()):
        
        news = f"{hbold(v['time'])}\n" \
            f"{hlink(v['title'], v['url'])}\n"\
            f"{v['annotation']}"
        await message.answer(news)
        
# Этот хэндлер будет срабатывать на нажатие кнопки "Интересное"
@router.message(Text(text=LEXICON['int_news']))
async def get_int_news(message: Message):
    with open("interesting_news_dict.json") as file:
        interesting_news_dict = json.load(file)

    for k, v in reversed(interesting_news_dict.items()):
        
        news = f"{hbold(v['time'])}\n" \
            f"{hlink(v['title'], v['url'])}\n"\
            f"{v['annotation']}"
        await message.answer(news)

# Этот хэндлер будет срабатывать на нажатие кнопки "Политика"
@router.message(Text(text=LEXICON['polit_news']))
async def get_polit_news(message: Message):
    with open("political_news_dict.json") as file:
        political_news_dict = json.load(file)

    for k, v in reversed(political_news_dict.items()):
        
        news = f"{hbold(v['time'])}\n" \
            f"{hlink(v['title'], v['url'])}\n"\
            f"{v['annotation']}"
        await message.answer(news)

# Этот хэндлер будет срабатывать на нажатие кнопки "Экономика"
@router.message(Text(text=LEXICON['econ_news']))
async def get_econ_news(message: Message):
    with open("econ_news_dict.json") as file:
        econ_news_dict = json.load(file)

    for k, v in reversed(econ_news_dict.items()):
        
        news = f"{hbold(v['time'])}\n" \
            f"{hlink(v['title'], v['url'])}\n"\
            f"{v['annotation']}"
        await message.answer(news)

# Этот хэндлер будет срабатывать на команду "/subscription"
@router.message(Command(commands='subscription'))
async def process_subscription_command(message: Message):
    await message.answer(LEXICON[message.text], reply_markup = sub_unsub_keyboard)

# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "Подписаться"
@router.callback_query(Text(text='sub_button_pressed'))
async def process_sub_press(callback: CallbackQuery):
    await callback.message.edit_text(text=LEXICON['sub_text'], reply_markup = sub_keyboard)
    await callback.answer()

# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "Все новости"
@router.callback_query(Text(text='sub_all_pressed'))
async def sub_all_press(callback: CallbackQuery):
    #Добавляю id пользователя в txt файл
    joinedFile_all = open("id_all_news.txt", "a")
    joinedFile_all.write(str(callback.message.chat.id)+"\n")
    joinedUsers_all.add(callback.message.chat.id)
    await callback.message.edit_text(text=LEXICON['subscribe'])
    await callback.answer()

# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "Главные новости"
@router.callback_query(Text(text='sub_main_pressed'))
async def sub_main_press(callback: CallbackQuery):
    joinedFile_main = open("id_main_news.txt", "a")
    joinedFile_main.write(str(callback.message.chat.id)+"\n")
    joinedUsers_main.add(callback.message.chat.id)
    await callback.message.edit_text(text=LEXICON['subscribe'])
    await callback.answer()

# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "Санкт-Петербург"
@router.callback_query(Text(text='sub_spb_pressed'))
async def sub_spb_press(callback: CallbackQuery):
    joinedFile_spb = open("id_spb_news.txt", "a")
    joinedFile_spb.write(str(callback.message.chat.id)+"\n")
    joinedUsers_spb.add(callback.message.chat.id)
    await callback.message.edit_text(text=LEXICON['subscribe'])
    await callback.answer()

# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "Интересное"
@router.callback_query(Text(text='sub_int_pressed'))
async def sub_int_press(callback: CallbackQuery):
    joinedFile_int = open("id_int_news.txt", "a")
    joinedFile_int.write(str(callback.message.chat.id)+"\n")
    joinedUsers_int.add(callback.message.chat.id)
    await callback.message.edit_text(text=LEXICON['subscribe'])
    await callback.answer()

# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "Политика"
@router.callback_query(Text(text='sub_polit_pressed'))
async def sub_polit_press(callback: CallbackQuery):
    joinedFile_polit = open("id_polit_news.txt", "a")
    joinedFile_polit.write(str(callback.message.chat.id)+"\n")
    joinedUsers_polit.add(callback.message.chat.id)
    await callback.message.edit_text(text=LEXICON['subscribe'])
    await callback.answer()

# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "Экономика"
@router.callback_query(Text(text='sub_econ_pressed'))
async def sub_econ_press(callback: CallbackQuery):
    joinedFile_econ = open("id_econ_news.txt", "a")
    joinedFile_econ.write(str(callback.message.chat.id)+"\n")
    joinedUsers_econ.add(callback.message.chat.id)
    await callback.message.edit_text(text=LEXICON['subscribe'])
    await callback.answer()

# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "Отписаться"
@router.callback_query(Text(text='unsub_button_pressed'))
async def process_unsub_press(callback: CallbackQuery):
    await callback.message.edit_text(text=LEXICON['unsub_text'], reply_markup = unsub_keyboard)
    await callback.answer()

@router.callback_query(Text(text='unsub_all_pressed'))
async def unsub_all_press(callback: CallbackQuery):
    with open('id_all_news.txt') as f:
        lines = f.readlines()
    user_id = str(callback.message.chat.id)
    pattern = re.compile(re.escape(user_id))
    with open('id_all_news.txt', 'w') as f:
        for line in lines:
            result = pattern.search(line)
            if result is None:
                f.write(line)
    await callback.message.edit_text(text=LEXICON['unsubscribe'])
    await callback.answer()

@router.callback_query(Text(text='unsub_main_pressed'))
async def unsub_main_press(callback: CallbackQuery):
    with open('id_main_news.txt') as f:
        lines = f.readlines()
    user_id = str(callback.message.chat.id)
    pattern = re.compile(re.escape(user_id))
    with open('id_main_news.txt', 'w') as f:
        for line in lines:
            result = pattern.search(line)
            if result is None:
                f.write(line)
    await callback.message.edit_text(text=LEXICON['unsubscribe'])
    await callback.answer()

@router.callback_query(Text(text='unsub_spb_pressed'))
async def unsub_spb_press(callback: CallbackQuery):
    with open('id_spb_news.txt') as f:
        lines = f.readlines()
    user_id = str(callback.message.chat.id)
    pattern = re.compile(re.escape(user_id))
    with open('id_spb_news.txt', 'w') as f:
        for line in lines:
            result = pattern.search(line)
            if result is None:
                f.write(line)
    await callback.message.edit_text(text=LEXICON['unsubscribe'])
    await callback.answer()

@router.callback_query(Text(text='unsub_int_pressed'))
async def unsub_int_press(callback: CallbackQuery):
    with open('id_int_news.txt') as f:
        lines = f.readlines()
    user_id = str(callback.message.chat.id)
    pattern = re.compile(re.escape(user_id))
    with open('id_int_news.txt', 'w') as f:
        for line in lines:
            result = pattern.search(line)
            if result is None:
                f.write(line)
    await callback.message.edit_text(text=LEXICON['unsubscribe'])
    await callback.answer()

@router.callback_query(Text(text='unsub_polit_pressed'))
async def unsub_polit_press(callback: CallbackQuery):
    with open('id_polit_news.txt') as f:
        lines = f.readlines()
    user_id = str(callback.message.chat.id)
    pattern = re.compile(re.escape(user_id))
    with open('id_polit_news.txt', 'w') as f:
        for line in lines:
            result = pattern.search(line)
            if result is None:
                f.write(line)
    await callback.message.edit_text(text=LEXICON['unsubscribe'])
    await callback.answer()

@router.callback_query(Text(text='unsub_econ_pressed'))
async def unsub_econ_press(callback: CallbackQuery):
    with open('id_econ_news.txt') as f:
        lines = f.readlines()
    user_id = str(callback.message.chat.id)
    pattern = re.compile(re.escape(user_id))
    with open('id_econ_news.txt', 'w') as f:
        for line in lines:
            result = pattern.search(line)
            if result is None:
                f.write(line)
    await callback.message.edit_text(text=LEXICON['unsubscribe'])
    await callback.answer()

# Хэндлер для сообщений, которые не попали в другие хэндлеры
@router.message()
async def send_answer(message: Message):
    await message.answer(text=LEXICON_RU['other_answer'])

