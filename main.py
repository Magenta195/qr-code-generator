import pyqrcode
import tkinter as tk

text = 'http://kotgam.ivyro.net/2025/h1.17.04jr.mp3'
result_file = 'result'

def create_qrcode():
    txt = urlEntry.get() or 'https://www.naver.com'
    file = resultPathEntry.get() or 'result'

    result = pyqrcode.create(txt)
    result.png(f'./{file}.png', scale=8)

if __name__ == '__main__' :
    window = tk.Tk()
    window.title('qr generator')
    window.geometry("256x256")
    window.resizable(False, False)

    label = tk.Label(window, text='url을 등록해주세요')
    label.pack()

    urlEntry = tk.Entry(window, width=30)
    urlEntry.pack()

    label = tk.Label(window, text='출력할 이미지 경로를 등록해주세요')
    label.pack()

    resultPathEntry = tk.Entry(window, width=30)
    resultPathEntry.pack()

    button = tk.Button(window, width=20, height=3, text='generate QR Code', command=create_qrcode)
    button.pack()

    window.mainloop()
    create_qrcode()