import tkinter as tk
import cv2
from PIL import Image, ImageTk
from tkinter import PhotoImage, messagebox
import detect_customA as detect

class MainForm(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set window size and position
        self.title("Computer Vision-based Counting of Chickens and Ducks")
        self.geometry("1024x580+0+0")
        self.resizable(False,False)
        #self.overrideredirect(True)
        self.center_window()

        self.background_image = PhotoImage(file="bg1.png")
        self.background_label = tk.Label(self, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create button
        self.button = tk.Button(self, text="START", command=self.open_camera, font=("Quicksand-regular", 16), relief=tk.GROOVE, width=15, height=2, bg="#100c1d", fg="white")
        self.button.place(relx=0.5, rely=0.60, anchor=tk.CENTER)

    def center_window(self):
        # Get screen width and height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calculate position x and y for center alignment
        x = (screen_width - 1024) // 2
        y = (screen_height - 600) // 2

        self.geometry("1024x600+{}+{}".format(x, y))

    def open_camera(self):
        detect.run()
        self.destroy()

if __name__ == "__main__":
    app = MainForm()
    app.mainloop()
