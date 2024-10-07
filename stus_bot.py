import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Логування
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Функція для старту бота
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Привіт! Я бот, який відповідає на питання про Василя Стуса. Запитай мене щось!')

# Функція для обробки повідомлень
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()  # Перетворюємо текст у нижній регістр для простішої обробки

    # Відповіді на питання
    if 'народився' in text:
        await update.message.reply_text('Василь Стус народився 6 січня 1938 року в селі Рахнівка.')
    elif 'помер' in text:
        await update.message.reply_text('Василь Стус помер 4 вересня 1985 року в таборі на Уралі.')
    elif 'арештований' in text or 'арешти' in text:
        await update.message.reply_text('Василь Стус був арештований двічі: у 1972 та 1980 роках за дисидентську діяльність.')
    elif 'вірші' in text:
        await update.message.reply_text('Найвідоміші збірки Василя Стуса: "Зимові дерева", "Палімпсести", "Веселий цвинтар".')
    elif 'премія' in text:
        await update.message.reply_text('Василеві Стусу було посмертно присуджено Шевченківську премію в 1991 році.')
    elif 'син' in text or 'діти' in text:
        await update.message.reply_text('Дмитро́ Васи́льович Стус — український письменник, літературознавець, редактор. Кандидат філологічних наук. Член Асоціації українських письменників. Голова Всеукраїнської творчої спілки «Конгрес літераторів України». Генеральний директор Національного музею Тараса Шевченка.')
    elif 'дитинство' in text:
        await update.message.reply_text('Василь Стус зростав у селянській родині, де вивчав українську мову та літературу.')
    elif 'поезія' in text:
        await update.message.reply_text('Стус вважав поезію своєю місією і використовував її як засіб боротьби за права людини.')
    elif 'філософія' in text:
        await update.message.reply_text('Філософія Стуса була про вільний вибір, гідність і незламність духу, навіть у найскладніші часи.')
    else:
        await update.message.reply_text('Вибач, але я не знаю відповіді на це питання. Спробуй запитати про рік мого народження, арешти, вірші чи деталі з його життя!')

if __name__ == '__main__':
    TOKEN = '7687442452:AAF81vEsVsxgS7xpwipgjMoyu1QhdvgNAqo'  # Вставте ваш токен

    # Створення бота
    application = ApplicationBuilder().token(TOKEN).build()

    # Додаємо обробники команд і повідомлень
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Запускаємо бота
    application.run_polling()
