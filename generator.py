import os
import sys

import pyqrcode
from PIL import Image, ImageTk

DEFAULT_URL = 'https://www.naver.com'
DEFAULT_FILENAME = 'result'

MAX_WIDTH = 296
MAX_HEIGHT = 296

class Generator:
    @staticmethod
    def get_image_path(image_filename: str) -> str:
        if getattr(sys, 'frozen', False):
            base_path = os.path.sep.join(sys.argv[0].split(os.path.sep)[:-1])
        else:
            base_path = '.'

        image_file_path = os.path.join(base_path, f'{image_filename}.png')
        return image_file_path

    @staticmethod
    def resize_image(image_path):
        img = Image.open(image_path)
        original_width, original_height = img.size
        aspect_ratio = original_width / original_height

        if original_width > MAX_WIDTH or original_height > MAX_HEIGHT:
            if original_width / MAX_WIDTH > original_height / MAX_HEIGHT:
                new_width = MAX_WIDTH
                new_height = int(MAX_WIDTH / aspect_ratio)
            else:
                new_height = MAX_HEIGHT
                new_width = int(MAX_HEIGHT * aspect_ratio)
        else:
            new_width = original_width
            new_height = original_height

        resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

        return ImageTk.PhotoImage(resized_img)

    @staticmethod
    def generate(url_text: str, result_file: str, img_rendered):
        url_text = url_text or DEFAULT_URL
        result_file = result_file or DEFAULT_FILENAME
        result = pyqrcode.create(url_text)

        result_file_path = Generator.get_image_path(result_file)
        result.png(result_file_path, scale=8)

        img_rendered.img = Generator.resize_image(result_file_path)
        img_rendered.config(image = img_rendered.img)
