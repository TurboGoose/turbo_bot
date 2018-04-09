from image_module import convert_bytes, combine
from all_data import all_data
import requests
import os


def load_image(image, user_data):
    try:

        user_data["image_id"] = image.file_id
        user_data["current_image"] = convert_bytes(image.get_file().download_as_bytearray())
        return True

    except Exception as err:
        print("\n\nDownloading error : ", err)
        return False

        
def send_image(image_name, user_data):
    try:

        combine(image_name, user_data["image_id"], user_data["current_image"])
        image = {"photo": open("temp/{}.jpg".format(user_data["image_id"]), "rb")}

        requests.post("https://api.telegram.org/bot{}/sendPhoto?chat_id={}".
                               format(all_data["TOKEN"], user_data["chat_id"]), files=image)
        return True

    except Exception as err:
        print("\n\nUploading error : ", err)
        return False


def delete_temp_image(user_data):
    os.remove("temp/{}.jpg".format(user_data["image_id"]))
    user_data["image_id"] = None
