from PIL import Image
from io import BytesIO
from Projects.Telegram_API.all_data import all_data


def byte_convert(bytes_stream):
    return Image.open(BytesIO(bytes_stream)).convert("RGBA")


def combine(image_name, other_image, file_id):

    image_data = all_data["images"][image_name]

    if image_data["mode"] == "bg":
        background = Image.open(image_data["path"])
        foreground = other_image.resize(image_data["paste_image_size"])
        pos_to_paste = image_data["pos_to_paste"]

    elif image_data["mode"] == "fg":
        foreground = Image.open(image_data["path"])
        background = other_image

        indent_x, indent_y = image_data["indent_x"], image_data["indent_y"]
        x = background.size[0] - foreground.size[0] + indent_x if indent_x < 0 else indent_x
        y = background.size[1] - foreground.size[1] + indent_y if indent_y < 0 else indent_y
        pos_to_paste = (x, y)

    else:
        return

    background = background.convert("RGBA")
    foreground = foreground.convert("RGBA")

    background.paste(foreground, pos_to_paste, mask=foreground)

    background.convert("RGB").save("temp/{}.jpg".format(file_id), "JPEG")
