import tkinter as tk
import tkinter.font as tkFont


class App:
    def __init__(self, root):
        # setting title
        root.title("undefined")
        # setting window size
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_20 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_20["font"] = ft
        GLabel_20["fg"] = "#333333"
        GLabel_20["justify"] = "center"
        GLabel_20["text"] = "label"
        GLabel_20.place(x=110, y=70, width=70, height=25)

        GButton_801 = tk.Button(root)
        GButton_801["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_801["font"] = ft
        GButton_801["fg"] = "#000000"
        GButton_801["justify"] = "center"
        GButton_801["text"] = "Button"
        GButton_801.place(x=140, y=300, width=70, height=25)
        GButton_801["command"] = self.GButton_801_command

        GRadio_645 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        GRadio_645["font"] = ft
        GRadio_645["fg"] = "#333333"
        GRadio_645["justify"] = "center"
        GRadio_645["text"] = "RadioButton"
        GRadio_645.place(x=350, y=170, width=85, height=25)
        GRadio_645["command"] = self.GRadio_645_command

        GMessage_396 = tk.Message(root)
        ft = tkFont.Font(family='Times', size=10)
        GMessage_396["font"] = ft
        GMessage_396["fg"] = "#333333"
        GMessage_396["justify"] = "center"
        GMessage_396["text"] = "Message"
        GMessage_396.place(x=210, y=360, width=80, height=25)

        GButton_455 = tk.Button(root)
        GButton_455["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_455["font"] = ft
        GButton_455["fg"] = "#000000"
        GButton_455["justify"] = "center"
        GButton_455["text"] = "Button"
        GButton_455.place(x=320, y=300, width=70, height=25)
        GButton_455["command"] = self.GButton_455_command

        GLabel_271 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_271["font"] = ft
        GLabel_271["fg"] = "#333333"
        GLabel_271["justify"] = "center"
        GLabel_271["text"] = "label"
        GLabel_271.place(x=340, y=80, width=70, height=25)

        GButton_814 = tk.Button(root)
        GButton_814["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_814["font"] = ft
        GButton_814["fg"] = "#000000"
        GButton_814["justify"] = "center"
        GButton_814["text"] = "Button"
        GButton_814.place(x=200, y=30, width=70, height=25)
        GButton_814["command"] = self.GButton_814_command

        GRadio_20 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        GRadio_20["font"] = ft
        GRadio_20["fg"] = "#333333"
        GRadio_20["justify"] = "center"
        GRadio_20["text"] = "RadioButton"
        GRadio_20.place(x=90, y=170, width=85, height=25)
        GRadio_20["command"] = self.GRadio_20_command

        GLineEdit_295 = tk.Entry(root)
        GLineEdit_295["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GLineEdit_295["font"] = ft
        GLineEdit_295["fg"] = "#333333"
        GLineEdit_295["justify"] = "center"
        GLineEdit_295["text"] = "Entry"
        GLineEdit_295.place(x=220, y=130, width=70, height=25)

        GListBox_190 = tk.Listbox(root)
        GListBox_190["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GListBox_190["font"] = ft
        GListBox_190["fg"] = "#333333"
        GListBox_190["justify"] = "center"
        GListBox_190.place(x=470, y=60, width=80, height=25)

    def GButton_801_command(self):
        print("command")

    def GRadio_645_command(self):
        print("command")

    def GButton_455_command(self):
        print("command")

    def GButton_814_command(self):
        print("command")

    def GRadio_20_command(self):
        print("command")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
