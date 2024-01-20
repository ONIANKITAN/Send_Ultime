import telebot
from telebot.types import Message
import re
import time

BOT_TOKEN = '6813590394:AAH5IQcXRKwsq1kBa4BvXArS0Kr8fLwSrnU'
CANAL_USERNAME = 'turbosearch'  # Remplacez par le nom d'utilisateur du canal
CANAL_ID = -1002072366730

# Créez une instance de bot
bot = telebot.TeleBot(BOT_TOKEN)

# Gérez la commande /start
@bot.message_handler(commands=['start'])
def start(message: Message):
    chat_id = message.chat.id
    command_text = message.text.split(' ')[1] if len(message.text.split(' ')) > 1 else ''  # Extraire le texte après /start

    # Utiliser une expression régulière pour extraire l'identifiant du message
    match = re.match(r'^(\d+)$', command_text)

    if match:
        message_id = int(match.group(1))

        # Envoyer 10 documents en utilisant les liens extraits
        for i in range(5000):
            # Construire le lien
            message_link = f"https://t.me/{CANAL_USERNAME}/{message_id + i}"

            try:
                # Vérifier si le message transféré est une photo ou un document
                sent_message = None
                
                sent_message = bot.send_document(chat_id, message_link)
                sent_message = bot.send_document(CANAL_ID, message_link)
               

                if sent_message.sticker:
                    continue
                else:
                    time.sleep(5)

            except telebot.apihelper.ApiException:
                continue
    else:
        # En cas de commande mal formée
        bot.send_message(chat_id, "Commande mal formée. Utilisez /start avec le format : /start=identifiant_message")

# Exécutez le bot
if __name__ == '__main__':
    bot.polling()
