from check_news_update import all_news_update, main_news_update, spb_news_update, interesting_news_update, political_news_update, economics_news_update
from handlers import joinedUsers_all, joinedUsers_main, joinedUsers_spb, joinedUsers_int,joinedUsers_polit, joinedUsers_econ
from aiogram.utils.markdown import hbold, hunderline, hcode, hlink
from aiogram import Bot
import asyncio

#Рассылка Всех новостей каждую минуту
async def all_news_every_minute(bot: Bot):
    for user in joinedUsers_all:
        while True:
            all_fresh_news = all_news_update()
            if len(all_fresh_news) >= 1:
                for k, v in reversed(all_fresh_news.items()):
                    news = f"{hbold(v['time'])}\n" \
                        f"{hlink(v['title'],v['url'])}" 
                    await bot.send_message(user, news)
            else: 
                await bot.send_message(user, "Пока нет свежих новостей", disable_notification=True)
            await asyncio.sleep(60)

#Рассылка Главных новостей каждую минуту
async def main_news_every_minute(bot: Bot):
    for user in joinedUsers_main:
        while True:
            main_fresh_news = main_news_update()
            if len(main_fresh_news) >= 1:
                for k, v in reversed(main_fresh_news.items()):
                    news = f"{hlink(v['title'],v['url'])}" 
                    await bot.send_message(user, news)
            else: 
                await bot.send_message(user, "Пока нет свежих новостей", disable_notification=True)
            await asyncio.sleep(60)

#Рассылка новостей категории "Санкт-Петербург" каждую минуту
async def spb_news_every_minute(bot: Bot):
    for user in joinedUsers_spb:
        while True:
            spb_fresh_news = spb_news_update()
            if len(spb_fresh_news) >= 1:
                for k, v in reversed(spb_fresh_news.items()):
                    news = f"{hbold(v['time'])}\n" \
                        f"{hlink(v['title'],v['url'])}" 
                    await bot.send_message(user, news)
            else: 
                await bot.send_message(user, "Пока нет свежих новостей", disable_notification=True)
            await asyncio.sleep(60)

#Рассылка новостей категории "Интересное" каждую минуту
async def int_news_every_minute(bot: Bot):
    for user in joinedUsers_int:
        while True:
            int_fresh_news = interesting_news_update()
            if len(int_fresh_news) >= 1:
                for k, v in reversed(int_fresh_news.items()):
                    news = f"{hbold(v['time'])}\n" \
                        f"{hlink(v['title'],v['url'])}" 
                    await bot.send_message(user, news)
            else: 
                await bot.send_message(user, "Пока нет свежих новостей", disable_notification=True)
            await asyncio.sleep(60)
            
#Рассылка новостей категории "Политика" каждую минуту
async def polit_news_every_minute(bot: Bot):
    for user in joinedUsers_polit:
        while True:
            political_fresh_news = political_news_update()
            if len(political_fresh_news) >= 1:
                for k, v in reversed(political_fresh_news.items()):
                    news = f"{hbold(v['time'])}\n" \
                        f"{hlink(v['title'],v['url'])}" 
                    await bot.send_message(user, news)
            else: 
                await bot.send_message(user, "Пока нет свежих новостей", disable_notification=True)
            await asyncio.sleep(60)

#Рассылка новостей категории "Экономика" каждую минуту
async def econ_news_every_minute(bot: Bot):
    for user in joinedUsers_econ:
        while True:
            econ_fresh_news = economics_news_update()
            if len(econ_fresh_news) >= 1:
                for k, v in reversed(econ_fresh_news.items()):
                    news = f"{hbold(v['time'])}\n" \
                        f"{hlink(v['title'],v['url'])}" 
                    await bot.send_message(user, news)
            else: 
                await bot.send_message(user, "Пока нет свежих новостей", disable_notification=True)
            await asyncio.sleep(60)
