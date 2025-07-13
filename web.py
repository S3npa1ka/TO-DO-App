import streamlit as st


import functions


todos = functions.get_todos()


def add_todo():
    todo = st.session_state['new_todo'].strip() + "\n"
    todos.append(todo)
    functions.write_todos(todos)


def complete_todo(index: int, todo_text: str) -> None:
    """Remove the selected todo item once the user confirms."""
    todos.pop(index)
    functions.write_todos(todos)
    del st.session_state[todo_text]
    st.rerun()


st.title("MY TODO APP")
st.subheader("My first web App")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        st.button(
            "Complete",
            key=f"complete_{index}",
            on_click=complete_todo,
            args=(index, todo),
        )

st.text_input(label="", placeholder="Add a todo...", on_change=add_todo, key="new_todo")

st.session_state


