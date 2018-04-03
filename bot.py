from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from all_data import all_data
from edit_image import open_image
from do_requests import load_image, send_image


# --------------------  DEFAULT -------------------- #
def start(bot, update, user_data):
    update.message.reply_text("Привет, Я - Mr. FanBot.\n"
                              "Похоже, ты пришел по важному делу, проходи.\n"
                              "Чего ты хочешь?", reply_markup=menu_markup)
    user_data["chat_id"] = update.message.chat_id

    photo_list = bot.get_user_profile_photos(update.message.from_user.id)["photos"]
    if not photo_list or not load_image(photo_list[0][-1]["file_id"], user_data):
            user_data["current_image"] = open_image("data/patric.jpg")
            user_data["image_id"] = "default"

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
    update.message.reply_text("Загрузка фотографии...")
    if load_image(update.message.photo[0].file_id, user_data):
        update.message.reply_text("Фотография загружена.")
    else:
        update.message.reply_text("Ошибка загрузки.")


def cancer(bot, update, user_data):
    if not send_image("cancer", user_data):
        update.message.reply_text("Ошибка отправки.")


def delete(bot, update, user_data):
    if not send_image("delete", user_data):
        update.message.reply_text("Ошибка отправки.")


def disabilities(bot, update, user_data):
    if not send_image("disabilities", user_data):
        update.message.reply_text("Ошибка отправки.")


def rip(bot, update, user_data):
    if not send_image("rip", user_data):
        update.message.reply_text("Ошибка отправки.")


def brazzers(bot, update, user_data):
    if not send_image("brazzers", user_data):
        update.message.reply_text("Ошибка отправки.")


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
    updater = Updater(all_data["TOKEN"])
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
