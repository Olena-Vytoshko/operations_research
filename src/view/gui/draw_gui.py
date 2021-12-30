import tkinter as tk
from tkinter import messagebox, filedialog


def error(message: str):
    messagebox.showinfo(title='Error', message=message)


def button_click(entry, filtering: bool, solve_func):
    try:
        queens_number = int(entry.get())
        if queens_number < 4:
            raise ValueError
        folder_selected = filedialog.askdirectory()
        solve_func(queens_number, folder_selected, filtering)
        messagebox.showinfo(title='Result', message='The output folder with images of chessboard was loaded')

    except ValueError:
        error("Error with number of queen")
    finally:
        entry.delete(0, 'end')


def draw_gui(solve_func):
    window = tk.Tk()
    window.title("Олена Витошко")
    tk.Label(text="Hello! This is the program for solving N-queen task").pack()

    tk.Label(text="Write count of queens (>= 4)").pack()
    entry = tk.Entry()
    entry.pack()
    with_filtering_button = tk.Button(
        text="With filtering",
        command=lambda: button_click(entry, True, solve_func),
        width=25,
        height=5,
        bg="Aqua",
        fg="white",
    ).pack()

    without_filtering_button = tk.Button(
        text="Without filtering",
        command=lambda: button_click(entry, False, solve_func),
        width=25,
        height=5,
        bg="Aqua",
        fg="white",
    ).pack()
    window.mainloop()
