import streamlit as st
import pickle


file = open("diamondsss.pkl","rb")
model = pickle.load(file)

cla_dic = {'I1': 0,
 'SI2': 1,
 'SI1': 2,
 'VS2': 3,
 'VS1': 4,
 'VVS2': 5,
 'VVS1': 6,
 'IF': 7}
col_dic = {
    'D':6,
    'E':5,
    'F':4,
    'G':3,
    "H":2,
    "I":1,
    "J":0,
    
}

carat = st.number_input("Enter carat",min_value =0.200000,max_value=4.500000 )
clarity = st.selectbox("Eneter clarity",options=cla_dic.keys())
color = st.selectbox("Eneter color",options=col_dic.keys())
x = st.number_input("Enter value of X",min_value =0.200000,max_value=4.500000 )
y = st.number_input("Enter value of Y",min_value =0.200000,max_value=4.500000 )
z = st.number_input("Enter value of Z",min_value =0.200000,max_value=4.500000 )

if st.button("submit"):
    st.subheader(f"{carat} , {clarity} , {color}, {x},{y},{z}")
    st.header(f"{model.predict([[carat,cla_dic[clarity],col_dic[color],x,y,z]])}")

