LEXICON: dict[str, str] = {
    '/start': '<b>Привет!</b> Я новостной бот.\n\nЧтобы посмотреть '
              'новости, отправьте команду /news\n\nЧтобы управлять рассылкой,'
              'отправьте команду /subscription\n\nЧтобы получить справку по работе бота - отправьте '
              'команду /help\n\nЧтобы получить контактную информацию - отправьте '
              'команду /support\n\nВы всегда сможете найти все команды бота, открыв <b>Меню</b>.',
    '/help': 'Здесь в будущем будет справка по работе бота',
    '/support': 'Если у вас возникли трудности и/или есть предложения по улучшению '
                'бота, напишите на мою почту: chulkovadiana@icloud.com',
    '/news': 'Какие новости вам интересны?',
    '/subscription': 'Выберете действие:',
    'subscribe': 'Рад, что вы решили подписаться на нашу рассылку!',
    'unsubscribe': 'Вы отписаны от рассылки',
    'sub_button': 'Подписаться на рассылку',
    'sub_text': 'Какую категорию новостей вы хотите добавить в рассылку?',
    'unsub_button': 'Отписаться от рассылки',
    'unsub_text': 'От рассылки какой категории новостей вы хотите отписаться?',
    'all_news': 'Все новости',
    'main_news': 'Главные новости',
    'spb_news': 'Санкт-Петербург',
    'int_news': 'Интересное',
    'polit_news': 'Политика',
    'econ_news': 'Экономика',
    'other_answer': 'Извини, увы, это сообщение мне непонятно...'

}
LEXICON_COMMANDS: dict[str, str] = {
    '/news': 'Новости',
    '/subscription': 'Управление рассылкой',
    '/help': 'Справка по работе бота',
    '/support': 'Поддержка'
}