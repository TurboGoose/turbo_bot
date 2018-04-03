from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from Projects.Telegram_API.edit_image import combine, byte_convert
import requests
import os


TOKEN = "508716388:AAGTPYwsumxdmWfuKLVPhFSK9ZpNRBeTIMY"


def send_image(image_name, user_data):
    try:

        combine(image_name, user_data["current_image"], user_data["image_id"])
        image = {"photo": open("temp/{}.jpg".format(user_data["image_id"]), "rb")}
        status = requests.post("https://api.telegram.org/bot{}/sendPhoto?chat_id={}".
                               format(TOKEN, user_data["chat_id"]), files=image)
        # os.remove("temp/{}.jpg".format(user_data["image_id"]))

    except Exception as err:
        print("Sending error: ", err)


# --------------------  DEFAULT -------------------- #
def start(bot, update, user_data):
    update.message.reply_text("Привет, Я - Mr. FanBot ( Мистер Фанбот ).\n"
                              "Похоже, ты пришел по важному делу, проходи.\n"
                              "Чего ты хочешь?", reply_markup=menu_markup)
    user_data["chat_id"] = update.message.chat_id

    return 1


def help(bot, update):
    update.message.reply_text("ПОМОЩЬ")


def stop(bot, update):
    update.message.reply_text("Конец...?", reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END


# --------------------  MENU  -------------------- #
def tell_story(bot, update):
    update.message.reply_text("Переходим к историям...", reply_markup=story_markup)
    return 2


def show_meme(bot, update):
    update.message.reply_text("Переходим к мемам...", reply_markup=meme_markup)
    return 3


def create_image(bot, update):
    update.message.reply_text("Переходим в редактор...", reply_markup=image_markup)
    return 4


def show_place(bot, update):
    update.message.reply_text("Переходим к местам...", reply_markup=place_markup)
    return 5


# --------------------  STORY  -------------------- #
def new_story(bot, update):
    update.message.reply_text("ИСТОРИЯ")


# --------------------  MEME  -------------------- #
def new_meme(bot, update):
    update.message.reply_text("МЕМАС")


# --------------------  IMAGE  -------------------- #
def get_picture(bot, update, user_data):
    try:

        update.message.reply_text("Загрузка фотографии...")

        image_id = update.message.photo[0].file_id
        print("({}, {})".format(update.message.photo[0].width, update.message.photo[0].height))
        user_data["image_id"] = image_id

        path_response = requests.get("https://api.telegram.org/bot{}/getFile?file_id={}".format(TOKEN, image_id))
        print("Request status:", "success" if path_response else "failure")

        path_to_image = path_response.json()["result"]["file_path"]
        print("Path to the file:", path_to_image)

        file_response = requests.get("https://api.telegram.org/file/bot{}/{}".format(TOKEN, path_to_image))
        print("Downloading status:", "success" if file_response else "failure", end="\n----------------------\n\n")

        user_data["current_image"] = byte_convert(file_response.content)
        update.message.reply_text("Фотография загружена.")

    except:
        update.message.reply_text("Технические работы.\n"
                                  "Покиньте эту местнось для избежания травмоопасной ситуации.")


def cancer(bot, update, user_data):
    send_image("cancer", user_data)


def delete(bot, update, user_data):
    send_image("delete", user_data)


def disabilities(bot, update, user_data):
    send_image("disabilities", user_data)


def rip(bot, update, user_data):
    send_image("rip", user_data)


def brazzers(bot, update, user_data):
    send_image("brazzers", user_data)


# --------------------  PLACE  -------------------- #

def new_place(bot, update):
    update.message.reply_text("МЕСТО")


# --------------------  BASE  -------------------- #
def back(bot, update):
    update.message.reply_text("Что ты хочешь от меня?", reply_markup=menu_markup)
    return 1


menu_markup = ReplyKeyboardMarkup([["/story", "/meme"], ["/image", "/place"]])
story_markup = ReplyKeyboardMarkup([["/new_story"], ["/back"]])
meme_markup = ReplyKeyboardMarkup([["/new_meme"], ["/back"]])
image_markup = ReplyKeyboardMarkup([["/cancer", "/delete", "/disabilities"], ["/RIP", "/brazzers", "/back"]])
place_markup = ReplyKeyboardMarkup([["/new_place"], ["/back"]])


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("help", help))

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start, pass_user_data=True)],
        states={
            1: [CommandHandler("story", tell_story),
                CommandHandler("meme", show_meme),
                CommandHandler("image", create_image),
                CommandHandler("place", show_place)],

            2: [CommandHandler("new_story", new_story),
                CommandHandler("back", back)],

            3: [CommandHandler("new_meme", new_meme),
                CommandHandler("back", back)],

            4: [MessageHandler(Filters.photo, get_picture, pass_user_data=True),
                CommandHandler("cancer", cancer, pass_user_data=True),
                CommandHandler("delete", delete, pass_user_data=True),
                CommandHandler("disabilities", disabilities, pass_user_data=True),
                CommandHandler("RIP", rip, pass_user_data=True),
                CommandHandler("brazzers", brazzers, pass_user_data=True),
                CommandHandler("back", back)],

            5: [CommandHandler("new_place", new_place),
                CommandHandler("back", back)]

        },
        fallbacks=[CommandHandler("stop", stop)]
    )

    dp.add_handler(conv_handler)

    print("bot started...\n")

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
