#from functions import get_todos, write_todos

import functions
import time

now = time.strftime("%b %d, %Y %H:%M")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip().lower()


    if user_action.startswith('add') or user_action.startswith('new'):

        todo = user_action[4:] + '\n'

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)


    elif user_action.startswith('show'):

        todos = functions.get_todos()

            # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}.{item}"
            print(row.title())

    elif user_action.startswith('edit') :
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Please enter new todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)
        except ValueError:
            print("You entered wrong command")
            continue


    elif user_action.startswith('complete') :
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')

            todos.pop(number-1)

            functions.write_todos(todos)
            message = f"Todo &{todo_to_remove.title()}& was deleted as complete"
            print(message)
        except IndexError:
            print("You chose TODO which does not exist")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid, please choose from comands down below: \n")
print("Bye! ")

