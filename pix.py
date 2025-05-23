import curses
import os
import platform
import subprocess

if platform.system() == "FreeBSD":
    os.system('alias python3=python3.11')

os.mkdir('src')
prwd = subprocess.run(["pwd"], capture_output=True, text=True).stdout.strip()

menu = ["AutoSetup", "Hyprland", "Exit"]

def draw_menu(stdscr, selected_row_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    
    for idx, row in enumerate(menu):
        x = w // 2 - len(row) // 2
        y = h // 2 - len(menu) // 2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.A_REVERSE)
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.A_REVERSE)
        else:
            stdscr.addstr(y, x, row)

    stdscr.refresh()

def main(stdscr):
    curses.curs_set(0)
    stdscr.keypad(True)
    selected_row_idx = 0

    while True:
        draw_menu(stdscr, selected_row_idx)
        key = stdscr.getch()

        if key == curses.KEY_UP and selected_row_idx > 0:
            selected_row_idx -= 1
        elif key == curses.KEY_DOWN and selected_row_idx < len(menu) - 1:
            selected_row_idx += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if menu[selected_row_idx] == "Exit":
                break
            elif menu[selected_row_idx] == "AutoSetup":
                return "AutoSetup"
            elif menu[selected_row_idx] == "Hyprland":
                return "Hyprland"
result = curses.wrapper(main)
os.chdir(f"{prwd}/src")
if result == "AutoSetup":
    os.system('curl -O https://pixbahaa.github.io/src/AutoSetup.py')
    os.system('python3 AutoSetup.py')
elif result == "Hyprland":
    os.system('curl -O https://pixbahaa.github.io/src/Hyprland.py')
    os.system('python3 Hyprland.py')
