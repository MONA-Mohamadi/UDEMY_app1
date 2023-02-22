def get_todos(filepath='todos.txt'):
    """read the text file and return
     the todo list from the file.
     """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="todos.txt"):
    """Write the list to_do items in a text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == '__main__':
    print(get_todos())
