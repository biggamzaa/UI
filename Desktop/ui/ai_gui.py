import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("관상은 과학")
        self.geometry("720x480")

        # Create three frames
        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=self, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Show the start page
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="짜잔 시작 페이지")
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="남",
                            command=lambda: controller.show_frame("PageOne"))
        button1.pack()

        button2 = tk.Button(self, text="여",
                            command=lambda: controller.show_frame("PageTwo"))
        button2.pack()


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.image_label = None

        label = tk.Label(self, text="남자 얼굴 집어 넣는 페이지")
        label.pack(pady=10, padx=10)

        button_back = tk.Button(self, text="시작 페이지로 돌아가기",
                                command=lambda: controller.show_frame("StartPage"))
        button_back.pack()

        button_image = tk.Button(self, text="이미지 삽입", command=self.insert_image)
        button_image.pack()

    def insert_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])

        if file_path:
            image = Image.open(file_path)
            image = image.resize((200, 200), Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)

            if self.image_label:
                self.image_label.config(image=photo)
                self.image_label.image = photo
            else:
                self.image_label = tk.Label(self, image=photo)
                self.image_label.image = photo
                self.image_label.pack(pady=10)


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.image_label = None

        label = tk.Label(self, text="여자 얼굴 집어 넣는 페이지")
        label.pack(pady=10, padx=10)

        button_back = tk.Button(self, text="시작 페이지로 돌아가기",
                                command=lambda: controller.show_frame("StartPage"))
        button_back.pack()

        button_image = tk.Button(self, text="이미지 삽입", command=self.insert_image)
        button_image.pack()

    def insert_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])

        if file_path:
            image = Image.open(file_path)
            image = image.resize((200, 200), Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)

            if self.image_label:
                self.image_label.config(image=photo)
                self.image_label.image = photo
            else:
                self.image_label = tk.Label(self, image=photo)
                self.image_label.image = photo
                self.image_label.pack(pady=10)


if __name__ == "__main__":
    app = App()
    app.mainloop()
