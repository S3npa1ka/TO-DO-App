import streamlit as st
import functions

todos = functions.get_todos()
st.title("MY TODO APP")
st.subheader("My first web App")
st.write("This app is to increase your productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add a todo...")


