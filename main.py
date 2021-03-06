from tkinter import Tk, Frame, BOTH
from tkinter.ttk import Frame, Button, Style

class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.parent.title("Centered")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()
        self.exitButton()

    def exitButton(self):
        self.style = Style()
        self.style.theme_use("default")

        quitButton = Button(self, text="Close window", command=self.quit)
        quitButton.place(x=200, y=100)

    def centerWindow(self):

        w = 290
        h = 150

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w)/2
        y = (sh -h)/2

        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))


def main():

    root = Tk()
    app = Example(root)
    root.mainloop()

if __name__ == '__main__':
    main()