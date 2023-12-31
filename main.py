import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=300)

with col2:
    st.title("Matan Moshe")
    content = """
An IT and Cyber Security professional with a passion for learning and growing in the fields of cloud and Cyber Security. I'm motivated, a self-learner, and Dedicated to my work. A solid understanding of network defense strategies and the attack life cycle as well as hands-on experience with many security and SIEM products. 
Scripting experience in PowerShell and Bash on Linux environment. 
Familiar with networking protocols and organizational architecture. 
I'm a third-year student of Information Systems B.Sc. with a GPA of 87
"""
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=",")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")