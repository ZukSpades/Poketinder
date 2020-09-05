from InternalProcessing.Calc import *
from InternalProcessing.Validation import *
import tkinter as tk

GREEN = "#369457"
RED = "#CC0000"
WINDOW_DICT = {"bg": RED}
SIMPLE_LABEL_DICT = {"bg": RED, "font": ("fixedsys", 9)}
SCREEN_LABEL_DICT = {"bg": GREEN, "wraplength": 200, "padx": 20, "font": ("fixedsys", 9)}
SCREEN_DICT = {"bg": RED}
ENTRY_DICT = {"font": ("fixedsys", 7)}
BTN_DICT = {"font": ("fixedsys", 7), "bg": "white"}


def show_pokemon():
    screen_label['text'] = "Buscando a tu pokémon ideal..."
    date = date_entry.get()[:5]
    name = name_entry.get()
    if date and name:
        if validate_date(date):
            day, month = [int(n) for n in date.split("/")]
            pkm_number = calculate_pokemon(day, month, name)
            pkm_name = get_pokemon_from_pokedex(pkm_number)
            screen_label['text'] = f"¡Enhorabuena! Tu pokémon es {pkm_name} (n {pkm_number})"
            open_pokedex(pkm_name)
        else:
            screen_label['text'] = f"Vamos, {name}, esta es la prueba fácil. ¡Pon la fecha bien!"
    else:
        screen_label['text'] = "Debes rellenar todos los campos, entrenador"


# Main window
root = tk.Tk()
root.title("Pokétinder")
root.geometry("350x500")
root.config(cnf=WINDOW_DICT)
#root.iconbitmap("../images/Pokeball.ico")

# Content
# Date
tk.Label(root, text="Introduce tu fecha de nacimiento (DD/MM)", cnf=SIMPLE_LABEL_DICT).pack(pady=(20, 10))
date_entry = tk.Entry(root, width=5, cnf=ENTRY_DICT)
date_entry.pack(pady=(10, 10))
# Name
tk.Label(root, text="Introduce tu nombre", cnf=SIMPLE_LABEL_DICT).pack(pady=(20, 10))
name_entry = tk.Entry(root, cnf=ENTRY_DICT)
name_entry.pack(pady=(10, 10))
# Screen
screen_frame = tk.Frame(root, width=250, height=200, bg=GREEN, highlightbackground="black", highlightthickness=5, bd=0)
screen_frame.pack(pady=15)
screen_frame.grid_propagate(0)
screen_label = tk.Label(screen_frame, text="Bienvenido, entrenador. Introduce tus datos y te asignaremos a tu primer pokémon", cnf=SCREEN_LABEL_DICT)
screen_label.grid(row=1, column=0, pady=10)
# Button
send_btn = tk.Button(root, command=show_pokemon, text="Enviar", cnf=BTN_DICT)
send_btn.pack(pady=(20, 10))

root.mainloop()

