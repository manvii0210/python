#streamlit run calculator.py
import streamlit as st
st.title('calculator')
st.markdown('WELCOME TO MY FIRST WEB APP')

c1,c2 = st.columns(2)
fnum = c1.number_input('enter first number', value=0)
snum = c2.number_input('enter second number', value=0)

options = ['addition','subtraction','multiplication','division']
choice = st.radio('select operation', options)

button = st.button('calculate')

result = 0
if button:
    if choice == 'addition':
        result = fnum + snum
    if choice == 'subtraction':
        result = fnum - snum
    if choice == 'multiplication':
        result = fnum * snum
    if choice == 'division':
        result = fnum / snum

st.success(f'The result is {result}')
