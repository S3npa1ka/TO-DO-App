import streamlit as st
import functions


todos = functions.get_todos()
def add_todo():
    todo = st.session_state['new_todo'].strip() + "\n"
    todos.append(todo)
    functions.write_todos(todos)



st.title("MY TODO APP")
st.subheader("My first web App")
st.write("This app is to increase your productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add a todo...",
              on_change=add_todo, key='new_todo')

st.session_state


