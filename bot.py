import asyncio
import logging

from aiogram import Bot, Dispatcher
from config import token
import handlers
from set_menu import set_menu
from news_every_minute import all_news_every_minute, main_news_every_minute, spb_news_every_minute, int_news_every_minute, polit_news_every_minute, econ_news_every_minute

# Инициализируем логгер
logger = logging.getLogger(__name__)


# Функция конфигурирования и запуска бота
async def main():
    # Конфигурируем логирование
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')

    # Инициализируем бот и диспетчер
    bot: Bot = Bot(token=token, parse_mode='HTML')
    dp: Dispatcher = Dispatcher()

    # Настраиваем главное меню бота
    await set_menu(bot)
    
    # Регистриуем роутер в диспетчере
    dp.include_router(handlers.router)

    loop1 = asyncio.get_event_loop() #создаём петлю
    loop1.create_task(all_news_every_minute(bot))

    loop2 = asyncio.get_event_loop() 
    loop2.create_task(main_news_every_minute(bot))

    loop3 = asyncio.get_event_loop() 
    loop3.create_task(spb_news_every_minute(bot))

    loop4 = asyncio.get_event_loop()
    loop4.create_task(int_news_every_minute(bot))

    loop5 = asyncio.get_event_loop() 
    loop5.create_task(polit_news_every_minute(bot))

    loop6 = asyncio.get_event_loop() 
    loop6.create_task(econ_news_every_minute(bot))
    # Запускаем polling
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())