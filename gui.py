from time import strftime

import functions
import FreeSimpleGUI as sg
import time


sg.theme("DarkPurple4")
clock_label = (sg.Text('', key='Clock'))
label = sg.Text("Type in a to-do")
inputBox = sg.InputText(tooltip="Enter to do", key="todo")
add_button = sg.Button("Add")
exit_button = sg.Button("Exit")
complete_button = sg.Button("Complete")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
layout = [[label, clock_label],
          [inputBox, add_button],
          [list_box, edit_button, complete_button],
          [exit_button]]
window = sg.Window('My TO-DO App',
                   layout=layout,
                   font=('Helvetica', 20))
while True:
    event, values = window.read(timeout=200)
    window['Clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S") )
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + "\n"
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select item first", font=('Helvetica', 16))
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break
        case 'Complete':
            try:
                todos = functions.get_todos()
                todo_to_delete = values['todos'][0]
                todos.remove(todo_to_delete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select item first", font=('Helvetica',16))
        case 'Exit':
            break


window.close()

