import base64
from io import BytesIO
from PIL import Image
# from secrets import token_hex


def create(base64_string: str) -> str:
    """Преоброзование base64 в png"""

    # Decode the Base64 string
    image_data = base64.b64decode(base64_string)

    # Create a BytesIO object to work with PIL
    image_buffer = BytesIO(image_data)

    # Open the image using PIL (Python Imaging Library)
    image = Image.open(image_buffer)

    # Save the image as a PNG file
    file_name = "face.png" #token_hex(6) + ".png"
    image.save(file_name, "PNG")

    # Close the BytesIO buffer
    image_buffer.close()
    return file_name
