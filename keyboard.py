from aiogram.utils.keyboard import InlineKeyboardBuilder


def main_screen():
    kb = InlineKeyboardBuilder()
    kb.button(text='💸Купить голду', callback_data='gold')
    kb.button(text='📉Курс', callback_data='course')
    kb.button(text='Отзывы', callback_data='reviews')
    kb.button(text='🧑‍💻Поддержка', callback_data='support')
    kb.adjust(2)
    return kb.as_markup()


def nedofunc():
    kb = InlineKeyboardBuilder()
    kb.button(text='🏠На главную страницу', callback_data='home')
    kb.adjust()
    return kb.as_markup()