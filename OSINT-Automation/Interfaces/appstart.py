import curses
from curses import wrapper
import time
import os
from .theHarvesterMenu import *
from .dnScanMenu import *
from .urlscanMenu import *
from .shodanMenu import *

#---------------Ncurses menu to read the documentation---------------

def mainMenu(stdscr):

    menu = ["DNSCAN", "SHODAN", "THE HARVESTER","URISCAN", "Exit"]
    max_height, max_width = stdscr.getmaxyx()
    menu_win = curses.newwin(max_height, max_width, 0, 0)

    setupMenuWindow(menu_win)
    menu_win.box()
    menu_win.bkgd(0, curses.color_pair(1))
    menu_win.refresh()


    current_item = 0
    while True:

        # Print the main menu
        enumAndHL(menu_win,menu,current_item)

        # Get user input
        c = menu_win.getch()

        if c == ord("z"):
            if current_item > 0:
                current_item -= 1

        elif c == ord("s"):
            if current_item < len(menu) - 1:
                current_item += 1

        elif c == ord("\n"): # ord("\n") is the key code for the enter key
            if current_item == 0:
                submenu(menu_win,max_height,max_width,"DNSCAN")
            if current_item == 1:
                submenu(menu_win,max_height,max_width,"SHODAN")
            if current_item == 2:
                submenu(menu_win,max_height,max_width,"THEHARVESTER")
            if current_item == 3:
                submenu(menu_win,max_height,max_width,"URISCAN")
            if current_item == 4:
                break
        elif c == 27:
            menu_win.erase()
            menu_win.refresh()
            break


def setupMenuWindow(menuWindowName):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)


def enumAndHL(menuWindowName,menuItemsList,current_item):
    for idx, item in enumerate(menuItemsList):
            if idx == current_item:
                menuWindowName.addstr(idx + 1, 2, item, curses.color_pair(1)| curses.A_REVERSE)
            else:
                menuWindowName.addstr(idx + 1, 2, item, curses.color_pair(1))
    menuWindowName.refresh()

def submenu(menu_win,max_height,max_width,tool):

    submenu = ["Start", "Documentation", "Return"]

    submenu_win = curses.newwin(max_height,max_width, 0, 0)

    setupMenuWindow(submenu_win)
    menu_win.erase()
    menu_win.refresh()
    submenu_win.box()
    submenu_win.bkgd(" ", curses.color_pair(1))
    submenu_win.refresh()

    current_item = 0

    while True:

        enumAndHL(submenu_win,submenu,current_item)

        v = submenu_win.getch()

        if v == ord("z"):
            if current_item > 0:
                current_item -= 1

        elif v == ord("s"):
            if current_item < len(submenu) - 1:
                current_item += 1

        elif v == ord("\n"): # ord("\n") is the key code for the enter key
            if current_item == 0:
                match tool:
                    case "DNSCAN":
                        # print("yes dnscan")
                        dnScanMenu(menu_win,max_height,max_width)
                    case "SHODAN":
                        # print("yes shodan")
                        shodanMenu(menu_win,max_height,max_width)
                    case "THEHARVESTER":
                        # print("yes the harvester")
                        theHarvesterMenu(menu_win,max_height,max_width)
                    case "URISCAN":
                        urlscanMenu(menu_win,max_height,max_width)
                        # print("yes uriscan")
            if current_item == 1:
                match tool:
                    case "DNSCAN":
                        os.system("man -l docs/app-dnscan.1")
                    case "SHODAN":
                        os.system("man -l docs/app-shodan.1")
                    case "THEHARVESTER":
                        os.system("man -l docs/app-theharvester.1")
                    case "URISCAN":
                        os.system("man -l docs/app-uriscan.1")

                menu_win.erase()
                menu_win.refresh()
                submenu_win.box()

            if current_item == 2:
                submenu_win.erase()
                submenu_win.refresh()
                menu_win.box()
                break

        elif v == 27: #escape ASCII value is 27
            menu_win.box()
            return "end"
            break



wrapper(mainMenu)
os.system("clear")
