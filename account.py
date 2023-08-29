import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
import streamlit as st
import os

cert_path = '/Users/aryanwarathe/Downloads/minor-streamlit1-17ffe31ca84e.json'
print("Absolute path:", os.path.abspath(cert_path))
cert = credentials.Certificate(os.path.abspath(cert_path))
cred = credentials.Certificate('/Users/aryanwarathe/Downloads/minor-streamlit1-17ffe31ca84e.json')
firebase_admin.initialize_app(cred)


def app():
 
   choice = st.selectbox('Login/Signup',['Login','Sign Up'])
   if choice =='Login':
     
     email=st.text_input('Email Address')
     password = st.text_input('Password',type = 'password')

     st.button('Login')

   else:

      email=st.text_input('Email Address')
      password = st.text_input('Password',type ='password')

      username =st.text_input('enter your name') 

      if st.button('Create my account'):
        user =auth.create_user(email = email, password =password, uid = username) 

        st.success('Account created successfully!')
        st.markdown('Please Login using your RVCE email id and password')
        st.balloons()