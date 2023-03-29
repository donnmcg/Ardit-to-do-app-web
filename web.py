import streamlit as st  # new library easy to create web apps with, works well with graphs
import functions

# Call the get_todos() function to get the list of todos
todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo + "\n")
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

# Create a list of todos
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox: # if any of the todos have been checked (True)
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo] # delete the to-do from the web list
        st.experimental_rerun()

# Create a text input to add new todos
st.text_input(label="Enter a todo:", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")

# st.session_state  # used this to see what was in the dictionary.
