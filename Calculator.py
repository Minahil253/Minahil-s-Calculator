


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y



def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    return x / y


import streamlit as st


def main():
    st.title("Calculator")
    num1 = st.number_input("Enter first number")
    operator = st.selectbox("Select operator", ["+", "-", "*", "/"])
    num2 = st.number_input("Enter second number")
    if st.button("Calculate"):
        if operator == "+":
            result = add(num1, num2)
        elif operator == "-":
            result = subtract(num1, num2)
        elif operator == "*":
            result = multiply(num1, num2)
        elif operator == "/":
            result = divide(num1, num2)
        st.write("Result:", result)
        choice = st.selectbox("Quit? (Y/N)", ["Y", "N"])
        if choice == "Y":
            st.write("Goodbye!")
            st.stop()

if __name__ == "__main__":
    main()


