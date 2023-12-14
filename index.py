import tkinter as tk
from tkinter import ttk
import math

def vypocitej():
    try:
        x = float(vstup_x.get())
        y = float(vstup_y.get())

        if operace.get() == "Sčítání":
            vysledek = x + y
        elif operace.get() == "Odečítání":
            vysledek = x - y
        elif operace.get() == "Násobení":
            vysledek = x * y
        elif operace.get() == "Dělení":
            if y != 0:
                vysledek = x / y
            else:
                vysledek = "Nelze dělit nulou"
        elif operace.get() == "Mocnina":
            vysledek = x ** y
        elif operace.get() == "Odmocnina":
            if y >= 0:
                vysledek = math.pow(x, 1/y)
            else:
                vysledek = "Odmocnina záporného čísla není definovaná"
        else:
            vysledek = "Vyberte operaci"

        vysledek_label.config(text=f"Výsledek: {vysledek}")
    except ValueError:
        vysledek_label.config(text="Chybný vstup")

hlavni_okno = tk.Tk()
hlavni_okno.title("Kalkulačka")
hlavni_okno.geometry("600x600")
hlavni_okno.resizable(False, False)

# Výběr operace - Radiobuttons - První sloupec
operace = tk.StringVar()
operace.set("Sčítání")  # Výchozí operace
scitani_radio = tk.Radiobutton(hlavni_okno, text="Sčítání", variable=operace, value="Sčítání")
odcitani_radio = tk.Radiobutton(hlavni_okno, text="Odečítání", variable=operace, value="Odečítání")
nasobeni_radio = tk.Radiobutton(hlavni_okno, text="Násobení", variable=operace, value="Násobení")
deleni_radio = tk.Radiobutton(hlavni_okno, text="Dělení", variable=operace, value="Dělení")

scitani_radio.grid(row=0, column=0, )
odcitani_radio.grid(row=1, column=0, )
nasobeni_radio.grid(row=2, column=0, )
deleni_radio.grid(row=3, column=0, )

# Výběr operace - Radiobuttons - Druhý sloupec
operace = tk.StringVar()
operace.set("Mocnina")  # Výchozí operace
mocnina_radio = tk.Radiobutton(hlavni_okno, text="Mocnina", variable=operace, value="Mocnina")
odmocnina_radio = tk.Radiobutton(hlavni_okno, text="Odmocnina", variable=operace, value="Odmocnina")

mocnina_radio.grid(row=0, column=1, )
odmocnina_radio.grid(row=1, column=1, )

# Číslo X
vstup_x = tk.Entry(hlavni_okno, font=('Helvetica', 10))
vstup_x.grid(row=4, column=0, )

# Číslo Y
vstup_y = tk.Entry(hlavni_okno, font=('Helvetica', 10))
vstup_y.grid(row=4, column=1, )

# Tlačítko pro výpočet
tlacitko_vypocet = tk.Button(hlavni_okno, text="Spočítej", command=vypocitej)
tlacitko_vypocet.grid(row=5, column=0, columnspan=2)

# Label pro zobrazení výsledku
vysledek_label = tk.Label(hlavni_okno, text="Výsledek: ", font=('Helvetica', 12))
vysledek_label.grid(row=6, column=0, columnspan=2, sticky='w')

# Konfigurace vah řádků a sloupců
hlavni_okno.grid_rowconfigure(4, weight=1)
hlavni_okno.grid_columnconfigure((0, 1), weight=1)

hlavni_okno.mainloop()