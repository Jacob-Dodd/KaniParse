import time
from simple_term_menu import TerminalMenu
import wordList
import Jamdict
import anki

def main():
    main_menu_title = ("""

    
dP     dP                   oo  888888ba                                      
88   .d8'                       88    `8b                                     
88aaa8P'  .d8888b. 88d888b. dP a88aaaa8P' .d8888b. 88d888b. .d8888b. .d8888b. 
88   `8b. 88'  `88 88'  `88 88  88        88'  `88 88'  `88 Y8ooooo. 88ooood8 
88     88 88.  .88 88    88 88  88        88.  .88 88             88 88.  ... 
dP     dP `88888P8 dP    dP dP  dP        `88888P8 dP       `88888P' `88888P' 
oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
                                                                              

Press Q or Esc to quit                                                         

    """)
    
    
    #"  Main Menu.\n  Press Q or Esc to quit. \n"
    main_menu_items = ["Generate Wordlist", "Search JAMdict", "Create Anki deck", "Quit"]
    main_menu_cursor = "> "
    main_menu_cursor_style = ("fg_green", "bold")
    main_menu_style = ("bg_green", "fg_gray")
    main_menu_exit = False

    main_menu = TerminalMenu(
        menu_entries=main_menu_items,
        title=main_menu_title,
        menu_cursor=main_menu_cursor,
        menu_cursor_style=main_menu_cursor_style,
        menu_highlight_style=main_menu_style,
        cycle_cursor=True,
        clear_screen=True,
    )

    edit_menu_title = "  Edit Menu.\n  Press Q or Esc to back to main menu. \n"
    edit_menu_items = ["Edit Config", "Save Settings", "Back to Main Menu"]
    edit_menu_back = False
    edit_menu = TerminalMenu(
        edit_menu_items,
        title=edit_menu_title,
        menu_cursor=main_menu_cursor,
        menu_cursor_style=main_menu_cursor_style,
        menu_highlight_style=main_menu_style,
        cycle_cursor=True,
        clear_screen=True,
    )

    while not main_menu_exit:
        main_sel = main_menu.show()

        if main_sel == 0:
            wordList.readEbook()
        elif main_sel == 1:
            Jamdict.searchDict()
            print("Dictionary entries downloaded to Vocabulary.txt")
        elif main_sel == 2:
            anki.createCards()
            print("Anki deck generated")
            time.sleep(1)
        elif main_sel == 3 or main_sel == None:
            main_menu_exit = True
            print("Quit Selected")


if __name__ == "__main__":
    main()