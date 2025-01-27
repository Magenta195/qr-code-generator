import pyqrcode

def create_qrcode(
        text: str = 'https://www.naver.com',
        result_path: str = './result.svg'
):
    result = pyqrcode.create(text)
    result.svg(result_path, scale=8)

if __name__ == '__main__' :
    create_qrcode()