FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """Read a text file and return list of
    to-do items
    """
    with open(filepath, 'r') as file:
        todos_value = file.readlines()
    return todos_value


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write a to-do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

