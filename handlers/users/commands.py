import time
import asyncio
from aiogram.types import Message
from loader import dp
from keyboards.inline.menu import menu


@dp.message_handler(commands=['start'])
async def message_on(msg: Message):
    await msg.answer('Лови саламчик!', reply_markup=menu)


@dp.message_handler()
async def check_commands(msg: Message):
    await send_schedule_lessons(msg)
    await send_time_before_call(msg)


async def send_time_before_call(msg: Message):
    if msg.text == '🔔🔔🔔Через сколько звонок?🔔🔔🔔':
        time_H = int(time.strftime('%H'))
        time_M = int(time.strftime('%M'))
        with open('./time_call.txt') as file:
            lessons = file.readlines()
        i = 1
        for lesson in lessons:
            print(lesson, lesson.strip(), lesson.split())
            print(lesson.strip().split('/')[0], lesson.strip().split('/')[1])
            t = 60*int(lesson.strip().split('/')[0])+int(lesson.split('/')[1])
            t2 = 60*int(lesson.strip().split('/')[2])+int(lesson.split('/')[3])
            t3 = 60*time_H+time_M
            if t - t2 <= 15 and t - t2 > 0:
                await msg.answer(f'Звонок через {t - t3} минут на {i} урок')
                return
            elif t2 - t3 <= 45 and t2 - t3 > 0:
                await msg.answer(f'Звонок через {t2 - t3} минут на перемену {i+1} урока')
                return
            i+=1




async def send_schedule_lessons(msg: Message):
    pass

