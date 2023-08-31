import streamlit as st
#to get the function apps import it, then create a varibale todos and set it equal to get todos
import

todos = functions.get_todos()

#this below is how we will get the todo enter and add it to the list
def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_todos(todos)



st.title('My Todo App')
#Below is a sub header
st.subheader("This is my todo app")
#below is a simple sentence
st.write('This app is to increase your productivity')

#Next create a loop that will set the check box to the todos.
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        #this is remove the index value the things in that index
        todos.pop(index)
        #then we write the new list in the functions code
        functions.write_todos(todos)
        #this will delete the session state which will delete the pair from the window dictionary.
        del st.session_state[todo]
        #this will rerun the code. this is needed for check boxes.
        st.experimental_rerun()

#add textbox to add to the list
st.text_input(label='Enter a todo: ', placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

#to run this app go to terminal and type streamlit run filename.py

