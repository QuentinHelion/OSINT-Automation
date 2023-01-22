import curses
from curses import wrapper
import time
import os

#---------------Dictionary to store file names---------------
ToolsDocs = {"DNSSCAN":"dnsscan_doc.txt", "SHODAN":"shodan_doc.txt", "THEHARVESTER":"theharvester_doc.txt", "URISCAN":"uriscan_doc.txt"}



#---------------Clear terminal---------------
#def clear():
#    os.system('clear')



#---------------Get text from documentation files---------------
def getDoc(doc):
    with open(doc) as f:
        contents = f.read()
    return contents

def docWin(stdscr):

    curses.curs_set(0)
    h, w = stdscr.getmaxyx()
    text = getDoc(doc)
    while True:
        curses.initscr()
        stdscr.addstr(0, 0, text)
        stdscr.refresh()
        
        if stdscr.getch() == ord('q'):
            break

   
    

#---------------Ncurses menu to read the documentation---------------

def main(stdscr):

    menu = ["DNSCAN", "SHODAN", "THE HARVESTER","URISCAN", "Exit"]
    
    menu_win = curses.newwin(len(menu) + 2, 30, 2, 10) 

    setupMenuWindow(menu_win)
    menu_win.box()
    menu_win.bkgd(" ", curses.color_pair(1))
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
                submenu(menu_win)
            if current_item == 1:
                submenu(menu_win)
            if current_item == 2:
                submenu(menu_win)
            if current_item == 3:
                submenu(menu_win)
            if current_item == 4:
                break
        elif c == 27:
            break


def setupMenuWindow(menuWindowName):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    

def enumAndHL(menuWindowName,menuItemsList,current_item):
    for idx, item in enumerate(menuItemsList):
            if idx == current_item:
                menuWindowName.addstr(idx + 1, 2, item, curses.color_pair(1)| curses.A_REVERSE)
            else:
                menuWindowName.addstr(idx + 1, 2, item, curses.color_pair(1))
    menuWindowName.refresh()

def submenu(menu_win):

    submenu = ["Use tool", "Doc", "Return"]

    submenu_win = curses.newwin(len(submenu)+2, 30, 2, 10) 

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
            #if current_item == 0:
                  
            if current_item == 1:
                doc_win = curses.newwin(50  ,140,0,0 ) 

                setupMenuWindow(doc_win)
                doc_win.bkgd(" ", curses.color_pair(1))
                menu_win.erase()
                menu_win.refresh()
                submenu_win.erase()
                submenu_win.refresh()
                doc_win.scrollok(True)
                doc_win.refresh()
                
                doc= ToolsDocs["DNSSCAN"]
                text = getDoc(doc)
                
                
                current_item = 0
                while True:
                    doc_win.addstr(0, 0, text)
                    #for line in text.split("\n"):
                        #doc_win.addstr(line)
                    doc_win.scroll()
                    doc_win.refresh() 
                    if doc_win.getch() == 27: #escape ASCII value is 27
                        doc_win.erase()
                        doc_win.refresh()
                        submenu_win.box()
                        break
            if current_item == 2:
                menu_win.box()
                break

        elif v == 27: #escape ASCII value is 27
            menu_win.box()
            break



wrapper(main)


"""
Example of how to use config.yaml

with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

dnsscan_doc = config["DOCS"]["DNSCAN"]
shodan_doc = config["DOCS"]["SHODAN"]
theharvester_doc = config["DOCS"]["THEHARVESTER"]
uriscan_doc = config["DOCS"]["URISCAN"]

with open(uriscan_doc) as f:
    contents = f.read()
print(contents)

"""