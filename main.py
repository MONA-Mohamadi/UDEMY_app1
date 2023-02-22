from function import*
import time

now = time.strftime("%A %B %d, %Y %H:%M:%S")
print('It is ',now)


while True:
    useraction = input(' Show, Add, Edit, Complete, or Exit: ')
    useraction = useraction.strip()

    if useraction.startswith("add"):
        todo = useraction[4:] + '\n'

        todos = get_todos()

        todos.append(todo)

        write_todos(todos)

    elif useraction.startswith('show'):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1}.{item.title()}")

    elif useraction.startswith('edit'):
        try:
            todo_number = int(useraction[5:])

            replaced_todo = input('please replace your new item: ')
            todos = get_todos()

            todos[todo_number - 1] = replaced_todo + '\n'
            write_todos(todos)
        except ValueError:
            print('wrong command')
            continue

    elif useraction.startswith('complete'):
        try:
            todo_number = int(useraction[9:])

            todos = get_todos()

            todos.pop(todo_number - 1)
            write_todos(todos)
        except IndexError:
            print('There is no item with that number')
            continue
        except ValueError:
            print('wrong command')
            continue

    elif 'exit' in useraction:
        break
print('Bye')