import curses
from .urlscanio import *

def urlscanMenu(menu_win,max_height,max_width):
    # submenu_win = curses.newwin(max_height,max_width, 0, 0)

    submenu_win = curses.newwin(max_height,max_width, 0, 0)

    # setupMenuWindow(submenu_win)
    # menu_win.erase()
    # menu_win.refresh()
    # submenu_win.box()
    # submenu_win.bkgd(" ", curses.color_pair(1))
    # submenu_win.refresh()

    menu_win.clear()
    menu_win.addstr("Domaine : ")
    curses.echo()
    domain = menu_win.getstr().decode()
    curses.noecho()
    menu_win.erase()
    menu_win.clear()
    menu_win.refresh()
    uri = Urlscanio()
    # curses.wrapper(theHarvesterMenu)
    uri.scan(domain)
    menu_win.refresh()
    menu_win.getkey()
