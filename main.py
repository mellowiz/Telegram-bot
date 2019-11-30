import re, requests, uuid
from telegram.ext import Updater, CommandHandler

TOKEN = '<TOKEN>'

def pong(update, context):
    update.message.reply_text('Pong')

def get_image_url():
    allowed_extension = ['jpg', 'jpeg', 'png', 'JPG', 'mp4']
    while True:
        url = requests.get('https://random.dog/woof.json').json()['url']
        file_extension = re.search("([^.]*)$", url).group(1).lower()
        if file_extension in allowed_extension:
            break
    return url

def woof(update, context):
    update.message.reply_photo(photo=get_image_url())

def uuidX(update, context):
    update.message.reply_text(str(uuid.uuid4()))

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('ping', pong))
    dp.add_handler(CommandHandler('woof', woof))
    dp.add_handler(CommandHandler('uuid', uuidX))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
