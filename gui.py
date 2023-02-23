import PySimpleGUI as sg
import function

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip='Enter to do', key='to_do')
add_button = sg.Button("Add")
list_box = sg.Listbox(values=function.get_todos(),
                      key='todos', enable_events=True, size=[45, 10])
edit_button = sg.Button('Edit')

window = sg.Window("My TO_Do App",
                   layout=[[label], [input_box], [add_button],
                           [list_box, edit_button]],
                   font=('Helvetica', 16))
while True:

    event, value = window.read()
    print(1,event)
    print(2,value)
    print(3,value['todos'])
    match event:
        case "Add":
            todos = function.get_todos()
            new_todo = value["to_do"] + "\n"
            todos.append(new_todo)
            function.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = value['todos'][0]
            new_todo = value["to_do"]

            todos = function.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            function.write_todos(todos)
            window['todos'].update(values=todos)

        case "todos":
         window['to_do'].update(value=value['todos'][0])





        case sg.WIN_CLOSED:
            break

window.close()
