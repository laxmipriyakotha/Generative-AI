import streamlit as st
import os
import config  # Import your config.py

from langchain_community.document_loaders import WebBaseLoader

from chains import Chain  # Capital 'C' in Chain
from portfolio import Portfolio
from utils import clean_text

# Set environment variables from config
os.environ["GROQ_API_KEY"] = config.GROQ_API_KEY
os.environ["USER_AGENT"] = config.USER_AGENT

def create_streamlit_app(llm, portfolio, clean_text):
    st.title("📧 Cold Mail Generator")
    url_input = st.text_input("Enter a URL:", value="https://careers.jpmorgan.com/us/en/students/programs/data-analytics-opportunities")
    submit_button = st.button("Submit")

    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            portfolio.load_portfolio()
            jobs = llm.extract_jobs(data)
            for job in jobs:
                skills = job.get('skills', [])
                links = portfolio.query_links(skills)
                email = llm.write_mail(job, links)
                st.code(email, language='markdown')
        except Exception as e:
            st.error(f"An Error Occurred: {e}")

if __name__ == "__main__":
    chain = Chain()  # Capital 'C' here, and no lowercase 'chain' variable
    portfolio = Portfolio()
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    create_streamlit_app(chain, portfolio, clean_text)
