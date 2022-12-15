import os
import openai
import telegram
from dotenv import load_dotenv
from telegram.ext import Dispatcher, MessageHandler, Filters, Updater

load_dotenv()
TG_BOT_TOKEN = os.getenv('TG_BOT_TOKEN')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Initialize OpenAI API client
openai.api_key = OPENAI_API_KEY

# Initialize Telegram Bot
bot = telegram.Bot(
    token=TG_BOT_TOKEN)
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher


def chat_ai(input_str):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Human: {input_str} \n AI:",
        temperature=0.5,
        max_tokens=4000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )

    print(response['choices'])
    res = response['choices'][0]['text']
    if res.startswith("？") or res.startswith("?"):
        res = res[1:]
    return res.strip()


def reply_handler(update, bot):
    """Reply message."""
    try:
        text = update.message.text
        print(text)
        res = chat_ai(text)
        print(res)
        bot.bot.send_message(chat_id=update.effective_chat.id, text=res)

    except Exception as e:
        print(e)


dispatcher.add_handler(MessageHandler(Filters.text, reply_handler))
updater.start_polling()
