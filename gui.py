import tkinter as tk

from generator import Generator

class GUI:
    def __init__(self, generator: Generator):
        self.window = tk.Tk()
        self.window.title('qr generator')
        self.window.geometry("384x512")
        self.window.resizable(False, False)

        self.generator = generator
        self.url_label = None
        self.url_entry = None
        self.result_path_label = None
        self.result_path_entry = None
        self.generate_button = None
        self.img = None

    def render(self):
        self.url_label = tk.Label(
            self.window,
            text='qr코드로 바꾸고 싶은 url을 등록해주세요'
        )

        self. url_entry = tk.Entry(
            self.window,
            width=30
        )

        self.result_path_label = tk.Label(
            self.window,
            text='출력할 이미지 파일 이름을 등록해주세요'
        )

        self.result_path_entry = tk.Entry(
            master=self.window,
            width=30
        )

        self.img = tk.Label(
            self.window,
            width=296,
            height=296
        )

        self.generate_button = tk.Button(
            master=self.window,
            width=20,
            height=3,
            text='QR Code 생성하기',
            command=lambda : self.generator.generate(
                url_text=self.url_entry.get(),
                result_file=self.result_path_entry.get(),
                img_rendered=self.img
            )
        )

    def pack(self):
        self.url_label.pack()
        self.url_entry.pack()
        self.result_path_label.pack()
        self.result_path_entry.pack()
        self.generate_button.pack()
        self.img.pack()

    def mainloop(self):
        self.window.mainloop()