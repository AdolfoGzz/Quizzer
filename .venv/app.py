import streamlit as st
import openai
import PyPDF2 as pdf

apiKey="sk-<your-key>"
def hello():
    st.write("Hello there")

st.title("Quiz creation app")
st.write("This is a quiz creation app. You can create a quiz based on a pdf file, and choose how many questions.")

uploaded_file = st.file_uploader("Upload a file", type=("pdf"))
question=st.slider("Select the number of questions", 1, 20, 10)

if st.button("Create quiz"):
    try:
        pdf.PdfReader(uploaded_file)
    except:
        st.write("Waiting for correct file upload...")
    else:
        file=pdf.PdfReader(uploaded_file)
        completeText=""
        for page in range(len(file.pages)):
            page=file.pages[page]
            text=page.extract_text()
            completeText=completeText+"\n"+text
    
        openai.api_key = apiKey
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=[
        {
        "role": "system",
        "content": "When I provide you a text and an amount of questions, I need you to create a quiz, in the same language as the text, based on the text with the amount of questions I gave. Add the correct answers at the end of the quiz."
        },
        {
        "role": "user",
        "content": f"{completeText}\n\nQuestions: {question}\n\n"
        },
        
        ],
        max_tokens=4096,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )

        print(response.choices[0])
        st.write(response.choices[0].message.content)
