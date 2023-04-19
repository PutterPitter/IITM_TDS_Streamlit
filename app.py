import streamlit as st

def find_largest(a, b, c) :
    largest = a
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    return largest

a = st.number_input("Enter the first number:")
b = st.number_input("Enter the second number:")
c = st.number_input("Enter the third number:")

largest = find_largest(a, b, c)

st.write("The largest number is:", largest)
