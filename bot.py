from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from all_data import all_data
from image_module import open_image
from geo_module import geocode, static
from request_module import send_image, load_image, delete_temp_image
import os


# --------------------  DEFAULT -------------------- #
def start(bot, update, user_data):
    update.message.reply_text("Привет, Я - Mr. FanBot.\n"
                              "Похоже, ты пришел по важному делу, проходи.\n"
                              "Чего ты хочешь?", reply_markup=menu_markup)
    user_data["chat_id"] = update.message.chat_id

    photo_list = bot.get_user_profile_photos(update.message.from_user.id)["photos"]
    if not photo_list or not load_image(photo_list[0][-1], user_data):
        user_data["current_image"] = open_image("data/patric.jpg")
        user_data["image_id"] = "default"

    return 1


def help(bot, update):
    update.message.reply_text(
        "МУЛЬТИМЕДИА-БОТ\n\n"
        "На данный момент доступно 2 основных функции:\n"
        "1) Работа с изображениями - /image\n"
        "2) Работа с географическими объектами - /place\n\n"
        "ИЗОБРАЖЕНИЯ:\n"
        "При работе с изображениями по умолчанию берется фотография с"
        "аватарки и выборочно преобразуется за счет встроенных фильтров."
        "Кроме того пользователь может загрузить любое изображение и в дальнейшем"
        "все преобразования будут проходить именно с ним (от сжатия никто не застрахован).\n\n"
        "ГЕОГРАФИЯ:\n"
        "При работе с геграфическими объектами вы можете выбрать 2 режима:\n\n"
        "1) Географический тест\n"
        "    Тест на знание географии.\n"
        "2) Поиск геграфических объектов\n"
        "    Поиск введенного геграфического объекта (из сообщения).\n"
        "    В случае успеха бот присылает картинку объекта и краткое\n"
        "    описание.\n\n"
        "Используемые API :\n"
        ">>> Telegram API\n"
        ">>> Yandex Maps API"
        )


def stop(bot, update):
    update.message.reply_text("Конец...?", reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END


# --------------------  MENU  -------------------- #
def create_image(bot, update):
    update.message.reply_text("Переходим в редактор...", reply_markup=image_markup)
    return 2


def place_menu(bot, update):
    update.message.reply_text("Что предпочитаете: тест или небольшую прогулку?", reply_markup=place_markup)
    return 3


def back_to_menu(bot, update):
    update.message.reply_text("Что ты хочешь от меня?", reply_markup=menu_markup)
    return 1


# --------------------  IMAGE  -------------------- #
def get_picture(bot, update, user_data):
    update.message.reply_text("Загрузка фотографии...")
    delete_temp_image(user_data)
    if load_image(update.message.photo[0], user_data):
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


def ban(bot, update, user_data):
    if not send_image("ban", user_data):
        update.message.reply_text("Ошибка отправки.")


# --------------------  PLACE  -------------------- #
#    >>>--------  MENU  --------<<<
def start_test(bot, update, user_data):
    update.message.reply_text("Вы уверены, что хотите начать тестирование?", reply_markup=test_markup)
    user_data["cur_question"] = 0
    user_data["test_score"] = 0
    return 5


def find_place(bot, update):
    update.message.reply_text("Куда пойдем?", reply_markup=geo_markup)
    return 4


def back_to_place_menu(bot, update):
    update.message.reply_text("Возвращаемся...", reply_markup=place_markup)
    return 3


#    >>>--------  GEO TEST  --------<<<
def ask_question(bot, update, user_data):
    cur_question = user_data["cur_question"]
    if cur_question < len(all_data["geo_test"]["questions"]):
        question_data = all_data["geo_test"]["questions"][cur_question]
        user_data["true_answer"] = question_data["true_answer"]
        answers_markup = ReplyKeyboardMarkup([[q]for q in question_data["answers"]])
        bot.sendPhoto(update.message.chat.id, static(question_data["params"]))
        update.message.reply_text("      ВОПРОС №{}\n{}\nВаш ответ :\n"
                                  .format(cur_question + 1, question_data["question"]),
                                  reply_markup=answers_markup)
        return 6
    else:
        result_markup = ReplyKeyboardMarkup([["/show_result", "/back"]])
        update.message.reply_text("Поздравляю, вы прошли тест!", reply_markup=result_markup)
        return 7


def check_answer(bot, update, user_data):
    user_answer = update.message.text
    if user_data["true_answer"].lower() in user_answer.lower():
        update.message.reply_text("Отлично! Это правильный ответ.\nПродолжаем?", reply_markup=test_markup)
        user_data["test_score"] += 1
    else:
        update.message.reply_text("К сожалению, это неверный ответ.\nПравильный ответ : {}\nПродолжаем?"
                                  .format(user_data["true_answer"]), reply_markup=test_markup)
    user_data["cur_question"] += 1
    return 5


def show_result(bot, update, user_data):
    smiles = "\U0001F64A" * (user_data["test_score"]) if user_data["test_score"] > 0 else "\U0001F621"
    update.message.reply_text("Ваш результат: " + smiles + "/10")


#    >>>--------  FIND PLACE  --------<<<
def new_place(bot, update):
    place = update.message.text
    update.message.reply_text("Выдвигаемся...")
    params, annotation = geocode(place, True)
    bot.sendPhoto(update.message.chat.id, static(params), caption=annotation)


menu_markup = ReplyKeyboardMarkup([["/image"], ["/place"]])
image_markup = ReplyKeyboardMarkup([["/cancer", "/delete", "/disabilities"],
                                    ["/RIP", "/ban"], ["/menu"]])
place_markup = ReplyKeyboardMarkup([["/geo_test", "/walk"], ["/menu"]])
geo_markup = ReplyKeyboardMarkup([["/back"]])
test_markup = markup = ReplyKeyboardMarkup([["/yes", "/no"]])


def main():
    updater = Updater(all_data["TOKEN"])
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("help", help))

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start, pass_user_data=True)],
        states={
            1: [CommandHandler("image", create_image),
                CommandHandler("place", place_menu)],

            2: [MessageHandler(Filters.photo, get_picture, pass_user_data=True),
                CommandHandler("cancer", cancer, pass_user_data=True),
                CommandHandler("delete", delete, pass_user_data=True),
                CommandHandler("disabilities", disabilities, pass_user_data=True),
                CommandHandler("RIP", rip, pass_user_data=True),
                CommandHandler("ban", ban, pass_user_data=True),
                CommandHandler("menu", back_to_menu)],

            3: [CommandHandler("geo_test", start_test, pass_user_data=True),
                CommandHandler("walk", find_place),
                CommandHandler("menu", back_to_menu)],

            4: [MessageHandler(Filters.text, new_place),
                CommandHandler("back", back_to_place_menu)],

            5: [CommandHandler("yes", ask_question, pass_user_data=True),
                CommandHandler("no", back_to_place_menu)],

            6: [MessageHandler(Filters.text, check_answer, pass_user_data=True)],

            7: [CommandHandler("show_result", show_result, pass_user_data=True),
                CommandHandler("back", back_to_menu)]

        },
        fallbacks=[CommandHandler("stop", stop)]
    )

    dp.add_handler(conv_handler)

    print("bot started...\n")
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    if "temp" not in os.listdir("."):
        os.mkdir("temp")
    else:
        for file in os.listdir("temp"):
            os.remove("temp/" + file)
    main()
