from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from lexicon_ru import LEXICON

# ---- Клавиатура, открывающаяся по команде /news ----
button_all: KeyboardButton = KeyboardButton(text=LEXICON['all_news'])
button_main: KeyboardButton = KeyboardButton(text=LEXICON['main_news'])
button_spb: KeyboardButton = KeyboardButton(text=LEXICON['spb_news'])
button_int: KeyboardButton = KeyboardButton(text=LEXICON['int_news'])
button_polit: KeyboardButton = KeyboardButton(text=LEXICON['polit_news'])
button_econ: KeyboardButton = KeyboardButton(text=LEXICON['econ_news'])

kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
kb_builder.row(button_all, button_main, button_spb, button_int, button_polit, button_econ, width=3)
news_kb = kb_builder.as_markup(resize_keyboard=True)

# ---- Инлайн-клавиатура, открывающаяся по команде /subscription ----
# Клавиатура Подписаться/Отписаться
sub_button: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON['sub_button'],
    callback_data='sub_button_pressed')

unsub_button: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON['unsub_button'],
    callback_data='unsub_button_pressed')

sub_unsub_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[sub_button],
                     [unsub_button]])

# Клавиатура выбора категории новостей для подписки
sub_all_button: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON['all_news'],
    callback_data='sub_all_pressed')

sub_main_button: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON['main_news'],
    callback_data='sub_main_pressed')

sub_spb_button: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON['spb_news'],
    callback_data='sub_spb_pressed')

sub_int_button: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON['int_news'],
    callback_data='sub_int_pressed')

sub_polit_button: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON['polit_news'],
    callback_data='sub_polit_pressed')

sub_econ_button: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON['econ_news'],
    callback_data='sub_econ_pressed')

sub_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[sub_all_button],[sub_main_button], [sub_spb_button], [sub_int_button], [sub_polit_button], [sub_econ_button]])

# Клавиатура выбора категории новостей для отписки
unsub_all_button: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON['all_news'],
    callback_data='unsub_all_pressed')

unsub_main_button: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON['main_news'],
    callback_data='unsub_main_pressed')

unsub_spb_button: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON['spb_news'],
    callback_data='unsub_spb_pressed')

unsub_int_button: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON['int_news'],
    callback_data='unsub_int_pressed')

unsub_polit_button: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON['polit_news'],
    callback_data='unsub_polit_pressed')

unsub_econ_button: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON['econ_news'],
    callback_data='unsub_econ_pressed')

unsub_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[unsub_all_button],[unsub_main_button], [unsub_spb_button], [unsub_int_button], [unsub_polit_button], [unsub_econ_button]])
   



