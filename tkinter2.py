import tkinter as tk


def show_text():
    text = entry.get()
    print(f"Wprowadzony tekst: {text}")


app = tk.Tk()
app.title("Przykład 2")
entry = tk.Entry(app)

entry.pack()

# command=show_text - tu przekazujemy adres funkcji, nie wywołujemy funkcji
button = tk.Button(app, text="Pokaż tekst", command=show_text)
button.pack()

app.mainloop()