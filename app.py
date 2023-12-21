#core packages
import streamlit as st
import time

#EDA packages
import pandas as pd
# import plotly.express as px

#database system
import task_db


def main():
    st.title("Stream master TO DO")
    menu = ["Create","Read","Update","Delete","About"]
    choice = st.sidebar.selectbox("Menu",menu)

    task_db.create_table()
    if choice=="Create":
        st.subheader("Add new item")

        col1,col2 = st.columns(2)
        with col1:
            task = st.text_area("Task to do")
        
        with col2:
            task_status = st.selectbox("Status",["To do","Doing","Completed"])
            task_due_date = st.date_input("Due Date")

        if st.button("Add Task"):
            task_db.add_data(task=task,task_status=task_status,task_due_date=task_due_date)
            st.success("Task added")

    elif choice=="Read":
        st.subheader("View all Tasks")
        result = task_db.view_all_data()
        df = pd.DataFrame(result,columns=["Tasks","Status","Due date"])
        with st.expander("View All Data"):
            st.dataframe(df)

        with st.expander("Task Status"):
            task_df = df["Status"].value_counts().to_frame()
            task_df = task_df.reset_index()
            #  st.dataframe(df)
            # p1 = px.pie(task_df,names='Status',values="count")
            # st.plotly_chart(p1)

    elif choice=="Update":
        st.subheader("Modify item")
        result = task_db.view_all_data()
        df = pd.DataFrame(result,columns=["Tasks","Status","Due date"])
        with st.expander("Current Tasks"):
            st.dataframe(df)
        list_of_tasks = [i[0] for i in task_db.view_unique_data()]
        selected_task = st.selectbox("Task to edit",list_of_tasks)
        selected_result = task_db.get_task(selected_task)
        # st.write(selected_result)

        if selected_result:
            s_task = selected_result[0][0]
            s_task_status = selected_result[0][1]
            s_task_due_date = selected_result[0][2]
            col1,col2 = st.columns(2)
            with col1:
                new_task = st.text_area("Task to do",f"{s_task}")
            
            with col2:
                new_task_status = st.selectbox(f"{s_task_status}",["To do","Doing","Completed"])
                new_task_due_date = st.date_input(f"{s_task_due_date}")

            if st.button("Update Task"):
                task_db.edit_task(s_task,s_task_status,s_task_due_date,new_task,new_task_status,new_task_due_date)
                st.success("Task updated")

    elif choice=="Delete":
        st.subheader("Discard items")
        list_of_tasks = [i[0] for i in task_db.view_unique_data()]
        selected_task = st.selectbox("Task to edit",list_of_tasks)
        selected_result = task_db.get_task(selected_task)
        if selected_result:
            o_task = selected_result[0][0]
            o_task_status = selected_result[0][1]
            o_task_due_date = selected_result[0][2]
            col1,col2 = st.columns(2)
            with col1:
                new_task = st.text_area("Task to do",f"{o_task}",disabled=True)
            
            with col2:
                new_task_status = st.selectbox("Task Status",["To do","Doing","Completed"],placeholder=o_task_status,disabled=True)
                st.text("Task Due date")
                new_task_due_date = st.date_input(f"{o_task_due_date}",disabled=True,label_visibility="collapsed")
            
            if st.button("Delete Task"):
                task_db.delete_task(o_task,o_task_status,o_task_due_date)
                with st.spinner('Working on it...'):
                    time.sleep(2)
                    st.success('Done!')

    elif choice=="About":
        st.subheader("About this app")
        st.text("Created By Soham Chakraborty")
        st.text("Linkedin:-")
        st.link_button("Linkedin","https://www.linkedin.com/in/soham-chakraborty-a07b471b0/")
        st.text("Github:-")
        st.link_button("Github","https://github.com/Sohamcodesstuff/stream-master-to-do-app")
        st.text("Version:- 1.1")



    
    pass





if __name__=="__main__":
    main()
