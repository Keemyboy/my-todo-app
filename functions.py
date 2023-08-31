
FILEPATH = 'todos.txt'

def get_todos(filepath = FILEPATH):
    #The doc string will allow you to create your own documentation to define what a function does.
    """" Read a text file and return the list of
    todo items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg ,filepath = FILEPATH):
    """"Write a todo item list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == '__main__':
    print('Hello')
    print(get_todos('todos.txt'))
