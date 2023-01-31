import tkinter as main
from tkinter import ttk
from tkVideoPlayer import TkinterVideo

class Vdeio(main.Tk):
    def __init__(self) :
        super().__init__()
        self.minsize(250, 150)
        self.maxsize(250, 150)
        self.title('Banka Liiiik')

    def video(self):
        videoplayer = TkinterVideo(master=self, scaled=True)
        videoplayer.load(r"Funny Algerian siger - Cant Stop Laughing.mp4")
        videoplayer.pack(expand=True, fill="both")
        videoplayer.play()

if __name__ == '__main__':
    vd = Vdeio()
    vd.video()
    vd.mainloop()