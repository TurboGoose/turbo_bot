from edit_image import convert_bytes, combine
from all_data import all_data
import requests


def load_image(file_id, user_data):
    try:

        user_data["image_id"] = file_id
        path_response = requests.get("https://api.telegram.org/bot{}/getFile?file_id={}".
                                     format(all_data["TOKEN"], file_id))
        print("Request status     :", "success" if path_response else "failure")

        path_to_image = path_response.json()["result"]["file_path"]
        print("Path to the file   :", path_to_image)

        file_response = requests.get("https://api.telegram.org/file/bot{}/{}".format(all_data["TOKEN"], path_to_image))
        print("Downloading status :", "success" if file_response else "failure", end="\n----------------------\n\n")

        user_data["current_image"] = convert_bytes(file_response.content)
        return True

    except Exception as err:
        print("\n\nDownloading error : ", err)
        return False

        
def send_image(image_name, user_data):
    try:

        combine(image_name, user_data["image_id"], user_data["current_image"])
        image = {"photo": open("temp/{}.jpg".format(user_data["image_id"]), "rb")}
        status = requests.post("https://api.telegram.org/bot{}/sendPhoto?chat_id={}".
                               format(all_data["TOKEN"], user_data["chat_id"]), files=image)
        # os.remove("temp/{}.jpg".format(user_data["image_id"]))
        return True

    except Exception as err:
        print("\n\nUploading error : ", err)
        return False
