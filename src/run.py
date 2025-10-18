import streamlit as st
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

login_option=st.sidebar.radio('login/signup',('login','signup'))
if login_option=='login' :
    st.title('login')
    with st.sidebar.form("login"):
        st.write("login here")
        username=st.text_input("Username")
        password=st.text_input("Password",type='password')
    # Every form must have a submit button.
        submitted = st.form_submit_button("login")
        if submitted:
            pass
else:
    st.title('signup')
    with st.sidebar.form("signup"):
        st.write("signup here")
        username=st.text_input("Username")
        password=st.text_input("Password",type='password')
        email=st.text_input("email")

        # Every form must have a submit button.
        submitted = st.form_submit_button("signup")
        if submitted:
            pass

st.write("Outside the form")
st.image("PythonToolKit_Banner.png",caption="This is a python project")

col1,col2 ,col3 = st.columns(3)
col1.metric(label="my website members",value="4000",delta="50")
col2.metric(label="my telegram groups members",value="300",delta="-10")
col3.metric(label="my instagram folowers",value='5k',delta='1250')


st.title(':zap: pytopia')
st.text("hi")
st.code("x=12")
with st.expander('statistics'):
    fig , ax = plt.subplots(1,1,figsize=(10,5))
    sns.histplot(np.random.randn(100),ax=ax)
    st.pyplot(fig)

with st.expander("user profile"):
    col1 , col2 = st.columns(2)
    col1.text_input('name:')
    col2.text_input("location :")
    st.camera_input('camera input',key= 'camera_input')

