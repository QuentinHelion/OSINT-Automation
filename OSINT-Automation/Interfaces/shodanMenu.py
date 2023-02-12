import curses
from .Appshodan import *

def shodanMenu(menu_win,max_height,max_width):
    submenu_win = curses.newwin(max_height,max_width, 0, 0)

    menu_win.clear()
    menu_win.addstr("Domaine : ")
    domain = menu_win.getstr().decode()
    menu_win.erase()
    menu_win.clear()
    menu_win.refresh()
    shodan = Appshodan()
    shodan.shodan_domain_info(domain)
    menu_win.refresh()
    menu_win.getkey()
