import curses
import time
import os

#---------------Dictionary to store file names---------------
ToolsDocs = {"DNSSCAN":"dnsscan_doc.txt", "SHODAN":"shodan_doc.txt", "THEHARVESTER":"theharvester_doc.txt", "URISCAN":"uriscan_doc.txt"}



#---------------Clear terminal---------------
def clear():
    os.system('clear')



#---------------Get text from documentation files---------------
def getDoc(doc):
    with open(doc) as f:
        contents = f.read()
    return contents



#---------------Ncurses menu to read the documentation---------------
def main(stdscr):

    curses.curs_set(0)
    h, w = stdscr.getmaxyx()
    text = getDoc(doc)

    x = 0
    y = 0

    while True:
        curses.initscr()
        stdscr.addstr(y, x, text)
        stdscr.refresh()
        
        if stdscr.getch() == ord('q'):
            break



#---------------Basic Menu---------------
def menu():
    clear()
    print("Choose a tool :")
    print("1- DNSSCAN")
    print("2- SHODAN")
    print("3- THE HARVESTER")
    print("4- URISCAN")
    print("0- EXIT")


#---------------START---------------
while True:
    menu()
    try:
        option = int(input())
    except ValueError:
        print("Wrong choice")
        continue
    if (option ==1 ):
        doc= ToolsDocs["DNSSCAN"]
        curses.wrapper(main)
        continue
    if (option ==2 ):
        doc= ToolsDocs["SHODAN"]
        curses.wrapper(main)
        continue
    if (option ==3 ):
        doc= ToolsDocs["THEHARVESTER"]
        curses.wrapper(main)
        continue
    if (option ==4 ):
        doc= ToolsDocs["URISCAN"]
        curses.wrapper(main)
        continue
    if (option ==0 ):
        break
    else:
        print("Wrong choice")