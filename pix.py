import curses
import subprocess

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
if result == "AutoSetup":
    subprocess.run(["python3", "src/AutoSetup.py"])
elif result == "Hyprland":
    subprocess.run(["python3", "src/Hyprland.py"])
