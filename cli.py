from tabulate import tabulate

class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'    

class Cli:
    def __init__(self) -> None:
        self.menu_option = [
            ["1.", "Display Todo List"],
            ["2.", "Add Todo Item"],
            ["3.", "Remove Todo Item"],
            ["4.", "Flag completed"],
            ["5.", "Exit the application"]
        ]
         
        self.header = []
        self.metadata = None
    
    def show_menus(self):
        print(tabulate(self.menu_option,tablefmt="github"))

    def add_show_info(self,head,metadata):
        self.header = head
        self.metadata = metadata
    
    def show_custom(self):
        print(tabulate(self.metadata,headers=self.header,tablefmt='grid'))
        print()