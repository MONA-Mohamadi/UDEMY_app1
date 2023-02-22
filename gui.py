import PySimpleGUI as sg
import function

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip='Enter to do', key='to_do')
add_button = sg.Button("Add")

window = sg.Window("My TO_Do App",
                   layout=[[label], [input_box], [add_button]],
                   font=('Helvetica',16))
while True:

    event, value = window.read()
    print(event)
    print(value)
    match event:
        case "Add":
            todos = function.get_todos()
            new_todo = value["to_do"] + "\n"
            todos.append(new_todo)
            function.write_todos(todos)
        case sg.WIN_CLOSED:
            break


window.close()
