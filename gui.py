import PySimpleGUI as sg
import function
import time
sg.theme('Black')
clock = sg.Text("", key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip='Enter to do', key='to_do')
add_button = sg.Button(size=50,image_source='add.png',mouseover_colors='LightBlue4',
                       tooltip='Add todo', key='Add')
list_box = sg.Listbox(values=function.get_todos(),
                      key='todos', enable_events=True, size=[45, 10])
edit_button = sg.Button('Edit')
complete_button = sg.Button(size = 50,image_source='complete.png',mouseover_colors='LightBlue4',
                            tooltip='Check a todo',key="Complete")
exit_button = sg.Button('Exit')

window = sg.Window("My TO_Do App",
                   layout=[[clock],
                           [label],
                           [input_box,add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 16))
while True:
    event, value = window.read(timeout=3000)
    window['clock'].update(value=time.strftime("%A %B %d, %Y %H:%M"))
    print(1, event)
    print(2, value)
    print(3, value['todos'])
    match event:
        case "Add":
            todos = function.get_todos()
            new_todo = value["to_do"] + "\n"
            todos.append(new_todo)
            function.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = value['todos'][0]
                new_todo = value["to_do"]

                todos = function.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + '\n'
                function.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup('First select an item', font=('Helvetica', 20))
        case 'Complete':
            try:
                todo_to_complete = value['todos'][0]
                todos = function.get_todos()
                todos.remove(todo_to_complete)
                function.write_todos(todos)
                window['todos'].update(values=todos)
                window['to_do'].update(value="")
            except IndexError:
                sg.popup('First select an item', font=('Helvetica', 20))
        case "todos":
            window['to_do'].update(value=value['todos'][0])
        case "Exit":
            break

        case sg.WIN_CLOSED:
            break

window.close()
