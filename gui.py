import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
inputBox = sg.InputText(tooltip= " Enter to do")
add_button = sg.Button("Add")

window = sg.Window('My TO-DO App', layout=[[label], [inputBox, add_button]])
window.read()
window.close()

