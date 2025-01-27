import pyqrcode

DEFAULT_URL = 'https://www.naver.com'
DEFAULT_FILENAME = 'result'

class Generator:
    @staticmethod
    def generate(url_text: str, result_file: str):
        url_text = url_text or DEFAULT_URL
        result_file = result_file or DEFAULT_FILENAME
        result = pyqrcode.create(url_text)
        result.png(f'./{result_file}.png', scale=8)
