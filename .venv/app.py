import streamlit as st
import streamlit_scrollable_textbox as stx
import openai

# Set OpenAI API key
openai.api_key = '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'

st.set_page_config(page_title='Personal Assistant', page_icon='👩‍💻', layout="centered")

st.title("Google Calendar Personal Assistant")
st.write("This is a demo of the Google Calendar Personal Assistant. It is a tool that helps you manage your calendar by automatically scheduling meetings and events for you. It can also help you find the best time to schedule a meeting with someone else.")

# List to store conversation history
conversation_history = []

# Function to schedule events using AI-generated details
def schedule_event(user_input):
    # Generate event details using OpenAI's GPT-3 model
    prompt = f"Schedule event:\n{user_input}\nEvent name: [Event Name]\nEvent date: [Event Date]\nEvent timeframe: [Event Timeframe]\nEvent location: [Event Location]\nEvent priority: [Event Priority]\n"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use an up-to-date model name
        messages=[
            {"role": "system", "content": "You are an AI powered calendar assistant. Given a user's input, you will generate the details of an event and schedule it on their calendar. Return only the generated event information. Return event name, description, date considering today is January 25 2024, timeframe, location considering the user lives in the center of Mexico City, and priority."},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message['content'].strip()

# Text area for user input
user_input = st.text_input("You:", "")

if st.button("Ask Assistant"):
    # Schedule event based on user input
    assistant_response = schedule_event(user_input)
    
    # Append user and assistant messages to the conversation history
    conversation_history.append(("👤 You", user_input))
    conversation_history.append(("👩‍💻 Assistant", assistant_response))
    
    # Clear user input after asking the assistant
    user_input = ""

# Scrollable text box
conversation_text = '\n\n'.join([f"{speaker}: \n {message}" for speaker, message in conversation_history])
stx.scrollableTextbox(conversation_text, height=400)
