#
#
# Day 14
#
#


# # create a function to get the todos
# def get_todos(filepath="files/todos.txt"):  # note filepath is a parameter. Make it default.
#     """ Read a text file and return the list of
#     to-do items.
#     """
#     with open(filepath, "r") as file_local:  # use with to open todos file
#         todos_local = file_local.readlines()  # creates a list from each line of the text file read
#     return todos_local
#
#
# # create a function to write the todos
# def write_todos(todos_arg, filepath="files/todos.txt"):  # filepath and todos_arg are parameters.
#     """ Write the to-do items list in the text file."""
#     with open(filepath, "w") as file_local:
#         file_local.writelines(todos_arg)  # write to the file
#
#
# if __name__ == "__main__": # Can control when this section is run.
#     print("Hello")
#     print(get_todos())

#
#
# Day 15
#
#

# # Added a Filepath variable.
#
# FILEPATH = "files/todos.txt" # Define variables considered constants at top of function file in capitals.
#
#
# # create a function to get the todos
# def get_todos(filepath=FILEPATH):  # note filepath is a parameter. Make it default.
#     """ Read a text file and return the list of
#     to-do items.
#     """
#     with open(filepath, "r") as file_local:  # use with to open todos file
#         todos_local = file_local.readlines()  # creates a list from each line of the text file read
#     return todos_local
#
#
# # create a function to write the todos
# def write_todos(todos_arg, filepath=FILEPATH):  # filepath and todos_arg are parameters.
#     """ Write the to-do items list in the text file."""
#     with open(filepath, "w") as file_local:
#         file_local.writelines(todos_arg)  # write to the file
#
#
# if __name__ == "__main__":  # Can control when this section is run.
#     print("Hello")
#     print(get_todos())


#
#
# Day 16, 17
#
#

# no changes

FILEPATH = "todos.txt" # Define variables considered constants at top of function file in capitals.


# create a function to get the todos
def get_todos(filepath=FILEPATH):  # note filepath is a parameter. Make it default.
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, "r") as file_local:  # use with to open todos file
        todos_local = file_local.readlines()  # creates a list from each line of the text file read
    return todos_local


# create a function to write the todos
def write_todos(todos_arg, filepath=FILEPATH):  # filepath and todos_arg are parameters.
    """ Write the to-do items list in the text file."""
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)  # write to the file


if __name__ == "__main__":  # Can control when this section is run.
    print("Hello")
    print(get_todos())