import streamlit as st
import function

todos = function.get_todos()

st.title("My Todo App")
st.subheader("This is my Todo App.")
st.write('This App helps you increase your productivity')

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder='Add a to do ...')