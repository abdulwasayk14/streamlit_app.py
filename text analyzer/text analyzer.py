import streamlit as st

st.title("Text Analyzer App")
st.write("Enter your text below to analyze it")

user_text = st.text_area("Enter your text here:" "")

if user_text:
    st.write("You entered:", user_text)

    st.subheader("Total Characters:", len(user_text))

    st.write("Total Words:" , len(user_text.split()))

    st.write("UppercaseText:", user_text.upper())

    st.write("Lowercase Text:", user_text.lower())

    st.write("Text without Extra Spaces:", " ".join(user_text.split()))

    st.write("Text Case:", user_text.title())

    st.write("Swapped Case:", user_text.swapcase())

    st.write("Is the text numeric?", user_text.isnumeric())

    st.write("Text Reversed:", user_text[::-1])

    repeat_times = st.slider("How many times to repeat text?", 1,5,1)

    st.write("Repeated Text:", user_text * repeat_times)

    if st.checkbox("Convert text to UPPERCASE"):
        st.write("Uppercase Text:", user_text.upper())

        word_count = len(user_text.split())
        char_count = len(user_text)

        st.write(f"Word Count: {word_count}")
        st.write(f"Character Count: {char_count}")
