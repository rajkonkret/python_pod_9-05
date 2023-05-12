import tkinter as tk


def on_click():
    print("Przycisk został naciśnięty")


app = tk.Tk()  # utwórz okienko
app.title("Przykład 1")  # nadaj tytuł

button = tk.Button(app, text="Kliknij mnie!", command=on_click)

button.pack()

app.mainloop()