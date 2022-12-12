whatToDoList = []
import os, time

def printWhatToDo():
    time.sleep(0.5)
    os.system("clear")
    print() 
    for item in whatToDoList:
        print(item)
    print() 
while True:
    
    menu = input('ToDo List Manager\nWhat do you want from your What-to-do list - view, add, edit, remove or delete ?\n: ')
    if menu == 'add':
        item = input("What do you want to add?\n ?: ")# .title()
        whatToDoList.append(item)
    elif menu == "remove":
        item = input("What do you want to remove ?: ")# .title()
        check = input("Are you sure you want to remove this?\n")
        if check[0]=="y":
            if item in whatToDoList:
                whatToDoList.remove(list)
            else:
                print(f'{item} was not in the list')
    elif menu=="edit":
        item = input("What do you want to edit?\n")# .title()
        new = input("What do you want to change it to?\n")# .title()
        for i in range(0,len(whatToDoList)):
          if whatToDoList[i] == item:
            whatToDoList[i] = new
    elif menu=="delete":
        check = input("Are you sure you want to remove entire list ?\n")
        if check[0]=="y":
            whatToDoList = []
    else:
        printWhatToDo()
    time.sleep(1)
    os.system('clear')
