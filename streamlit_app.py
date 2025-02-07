import streamlit as st
import groq

# Set up Groq API Key
GROQ_API_KEY = "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"

# Initialize Groq client
groq_client = groq.Groq(api_key=GROQ_API_KEY)

# Set up Streamlit UI
st.title("🚀 AI Agent System with Groq API")

# User Inputs
topic = st.text_input("Enter the topic for research:")
language = st.selectbox("Select output language:", ["English", "Spanish", "French"])

# AI Agent Class
class AIAgent:
    def __init__(self, role, task):
        self.role = role
        self.task = task

    def generate_response(self, input_text):
        try:
            response = groq_client.chat.completions.create(
                model="llama3-70b-8192",  # Correct model name
                messages=[
                    {"role": "system", "content": f"You are a {self.role}. Your task is: {self.task}"},
                    {"role": "user", "content": input_text}
                ],
                temperature=0.7,
                max_tokens=2000,
            )
            return response.choices[0].message.content if response.choices else "No response received."

        except Exception as e:
            return f"Error: {e}"

# Define AI Agents
research_agent = AIAgent(
    role="Research Agent",
    task="Retrieve and summarize relevant information about the given topic."
)

blog_writer_agent = AIAgent(
    role="Blog Writer",
    task="Write a structured blog post based on research findings."
)

# Button to execute AI Agents
if st.button("Generate AI Content"):
    if topic:
        st.subheader("📌 Research Agent Output:")
        research_summary = research_agent.generate_response(f"Summarize information on {topic}")
        st.write(research_summary)

        st.subheader("✍️ Blog Writer Output:")
        blog_post = blog_writer_agent.generate_response(f"Write a detailed blog post about {topic} in {language}.")
        st.write(blog_post)
    else:
        st.warning("Please enter a topic before generating content.")



# import streamlit as st
# import requests

# GROQ_API_KEY = "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"
# API_URL = "https://api.groq.com/v1/chat/completions"

# st.title("🚀 AI Agent System with Groq API")

# topic = st.text_input("Enter the topic for research:")
# language = st.selectbox("Select output language:", ["English", "Spanish", "French"])

# if st.button("Generate AI Content"):
#     if topic:
#         st.subheader("📌 Research Agent Output:")

#         headers = {"Authorization": f"Bearer {GROQ_API_KEY}"}
#         data = {
#             "model": "llama3-8b-8192",
#             "messages": [{"role": "user", "content": f"Summarize information on {topic}"}],
#         }

#         response = requests.post(API_URL, json=data, headers=headers)

#         if response.status_code == 200:
#             research_summary = response.json().get("choices", [{}])[0].get("message", {}).get("content", "No response.")
#         else:
#             research_summary = f"API Error: {response.status_code} - {response.json()}"

#         st.write(research_summary)

#     else:
#         st.warning("Please enter a topic before generating content.")
