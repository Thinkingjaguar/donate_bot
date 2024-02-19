import asyncio
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters.command import Command
from keyboard import main_screen, nedofunc
from aiogram.types import FSInputFile
from config import TOKEN, ADMINS


bot = Bot(token=TOKEN)
dp = Dispatcher()
admins = ADMINS


@dp.message(Command('start'))
# async def get_id(message: types.Message):
#     await message.delete()
#     await message.answer(str(message.from_user.id))
async def home(message: types.Message):
    await message.delete()
    path = __file__[:__file__.rfind('\\') + 1] + 'logo.jpg'
    await message.answer_photo(FSInputFile(path) , caption='''Приветствовуем вас в нашем телеграм боте GoldSay по продаже голды в STANDOFF 2.

Мы новички в это сфере поэтому мы хотим сделать скидку 40% для всех покупателей. Надеюсь это порадует всех вас и вы будете нас рекомендовать вашим друзьям.''',
                               reply_markup=main_screen())


@dp.callback_query(F.data == 'home')
async def home(callback: types.CallbackQuery):
    await callback.message.delete()
    await sending_main_message(chat_idi=callback.from_user.id, text='Что Вам нужно?')


@dp.callback_query(F.data == 'gold')
async def buy_gold(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text='''Ну что, приступим к оплате:
    - оплата qiwi по нику - RIGHT328
    - оплата переводом - 2200700500402358
📸 После оплаты, отправь сюда, в чат, скриншот оплаты''', reply_markup=nedofunc())
    await callback.answer()


@dp.callback_query(F.data == 'course')
async def see_course(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text='''Курс: 0.65 за 1 G
При скидке мы предложим вам другую стоимость''', reply_markup=nedofunc())
    await callback.answer()


@dp.callback_query(F.data == 'reviews')
async def see_reviewes(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text='💡 Если у вас есть какие-либо сомнения при покупке голды, то вы можете посмотреть отзывы и убедиться в нашей честности.',
                                  reply_markup=nedofunc())
    await callback.answer()


@dp.callback_query(F.data == 'support')
async def call_support(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text='Поддержка - @YzYgApbybalenca', reply_markup=nedofunc())
    await callback.answer()


@dp.message(F.photo)
async def screenshot(message: types.Message):
    await message.delete()
    for admin in admins:
        await bot.send_photo(admin, message.photo[-1].file_id, disable_notification=True)


async def sending_main_message(chat_idi, text):
    await bot.send_message(chat_id=chat_idi, text=text, reply_markup=main_screen())


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
