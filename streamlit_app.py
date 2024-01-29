import streamlit as st


def main():
    st.title("Welcome to Streamlit!")

    st.write("This is a simple Streamlit app that welcomes you.")

    name = st.text_input("What's your name?")
    if name:
        st.write(f"Hello, {name}! Welcome to your first Streamlit app.")


if __name__ == "__main__":
    main()
