
while True:
    useraction=input(' Show, Add, Edit, Complete, or Exit: ')
    useraction=useraction.strip()


    if 'add' in useraction or 'new' in useraction:
      todo = useraction[4:]+"\n"


      with open('files/todos.txt', 'r') as file:
           todos=file.readlines()

      todos.append(todo)


      with open('files/todos.txt', 'w') as file:
          file.writelines(todos)




    elif 'show' in useraction:
        with open('files/todos.txt', 'r') as file:
             todos=file.readlines()


        for index,item in enumerate(todos):
            item=item.strip('\n')
            print(f"{index+1}.{item.title()}")

    elif 'edit' in useraction:
       todo_number= int(useraction[5:])

       replaced_todo=input('please replace your new todo: ')
       with open('files/todos.txt', 'r') as file:
           todos = file.readlines()

       todos[todo_number-1]= replaced_todo+'\n'
       with open('files/todos.txt', 'w') as file:
           file.writelines(todos)

    elif 'complete' in useraction:
       todo_number = int(useraction[9:])
       with open('files/todos.txt', 'r') as file:
           todos = file.readlines()

       todos.pop(todo_number-1)
       with open('files/todos.txt', 'w') as file:
           file.writelines(todos)


    elif 'exit' in useraction:
      break
print('Bye')