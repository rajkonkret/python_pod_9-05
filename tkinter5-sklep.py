import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class Sklep:
    def __init__(self, master):
        self.master = master
        self.master.title("Gra Sklep")

        self.produkty = {
            "Chleb": 3,
            "Mleko": 2,
            "Jajka": 5
        }

        self.zakupy = {}
        ttk.Label(self.master, text="Produkty w sklepie").grid(column=0, row=0, pady=5)

        for index, product in enumerate(self.produkty):
            ttk.Label(self.master, text=f"{product}: {self.produkty[product]} zł").grid(
                column=0, row=index + 1, padx=5, pady=5
            )

            self.zakupy[product] = tk.IntVar()
            ttk.Entry(self.master, textvariable=self.zakupy[product], width=5).grid(
                column=1, row=index + 1, padx=5, pady=5
            )

        ttk.Button(self.master, text="żłóz zamówienie", command=self.zloz_zamowienie).grid(
            column=0, row=4, padx=5, pady=5
        )

    def zloz_zamowienie(self):
        suma = 0
        for produkt in self.produkty:
            # get() bo uzywamy IntVar
            ilosc = self.zakupy[produkt].get()
            cena = self.produkty[produkt] * ilosc
            suma += cena

        tk.messagebox.showinfo("Podsumawanie zamówienia", f"Koszt: {suma} zł")


okno = tk.Tk()
sklep = Sklep(okno)
okno.mainloop()
# 13:30
# hackerrank