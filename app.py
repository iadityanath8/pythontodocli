from db import Todo_DB
from tabulate import tabulate
from cli import Cli,Color

def status_to_string(data):
    i = 0
    while(i < len(data)):
        if data[i][2] == 0:
            data[i][2] = "Not Completed"
        else:
            data[i][2] = "Completed"
        i += 1

def cli():
    dbins = Todo_DB("todo.db")
    dbins.create_table()
    clins = Cli()

    while True:
        print()
        print(Color.CYAN + "Menus" + Color.RESET)

        clins.show_menus()

        choice = input(Color.BLUE + "Enter your choice: " + Color.RESET)

        if choice == "1":
            todo = dbins.get_todos()
            i = 0
            data = []
            headers = ["id","task","status"]
            print()
            print()

            while i < len(todo):
                data.append(list(todo[i]))
                i+=1

            status_to_string(data)
            clins.add_show_info(headers,data)
            clins.show_custom()

        elif choice == "2":
            print(Color.GREEN + "please enter the todo id you want to be completed -> " + Color.RESET)
            
            a = input()
            if dbins.id_exist(a) == False:
                print(Color.RED + "Id does not exist" + Color.RESET)
            else:
                dbins.add_todo(a)

        elif choice == "3":
            id = int(input(Color.GREEN + "Please provide us the todo id which need to be reomved -> " + Color.RESET))

            if dbins.id_exist(id) == False:
                print(Color.RED + "Id does not exist" + Color.RESET)
            else:
                dbins.delete_todo(id)
        
        elif choice == "4":
            id = int(input(Color.GREEN + "please provide the todo id that need to be marked completed -> " + Color.RESET))
            
            if dbins.id_exist(id) == False:
                print(Color.RED + "Id does not exist" + Color.RESET)
            else:
                dbins.completed(id)

        elif choice == "5":
            break
        else:
            print(Color.RED + "Invalid choice" + Color.RESET)
        pass



if __name__ == "__main__":
    cli()