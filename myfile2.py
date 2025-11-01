import pickle
import streamlit as st


model1=pickle.load(open("areapricebedage.pkl","rb"))
def mydeploy():
    st.title("area price prediction on criteria")
    a=st.number_input("enter area")
    b=st.number_input("enter bedroom")
    age=st.number_input("enter age")
    pred=st.button("predict")

    if pred :
        x=model1.predict([[a,b,age]])
        st.write("price of given area is ", x[0])



mydeploy()
