<!DOCTYPE html>
<html lang="en">

<body>

<h1>📧 AI Powered Email Generator</h1>
<p>Welcome to the <strong>AI Powered Email Generator</strong>, a project designed to automate the process of crafting personalized cold emails for job opportunities.AI-Powered Cold Email Generator is a smart tool that helps job seekers craft professional cold emails tailored to specific job postings. By entering a job URL, the system scrapes the job description, extracts required skills, and matches them with the user's portfolio. Using a powerful Large Language Model (LLM), it then generates a personalized cold email highlighting relevant skills and experience. This automation saves time, ensures relevance, and increases the chances of getting noticed. The intuitive interface requires minimal input, making it user-friendly. </p>
<p>This tool combines <strong>web scraping</strong>, <strong>NLP techniques</strong>, and <strong>AI-powered text generation</strong> to create tailored emails based on job descriptions and portfolio skills.</p>

<div class="section">
    <h2>🏗️ Architecture Overview</h2>
    <img src="https://github.com/laxmipriyakotha/Generative-AI/blob/main/img/Architecture.png?raw=true" alt="Architecture">

   ### 🏗️ Architecture Overview

**Explanation:**

- **User Input:** Provide a job posting URL (example: careers page of JPMorgan).
- **Web Scraping:** The system loads and processes the job description from the URL.
- **Data Cleaning:** Irrelevant text is removed using custom text cleaning functions.
- **Skill Matching:** Extracted job skills are matched with the skills available in your portfolio.
- **AI Email Generation:** Based on the job role, required skills, and your portfolio, the system generates a professional cold email using an **LLM (Large Language Model)**.
- **Output:** The personalized email is displayed for easy copy-paste.

</div>

<div class="section">
    <h2>💻 Interface - How It Looks</h2>
    <img src="https://github.com/laxmipriyakotha/Generative-AI/blob/main/img/interface.png?raw=true" alt="Interface">

  **Explanation:**

- **Simple UI:** Enter the job posting URL into the input box.
- **One-Click Processing:** Just click on `Submit` to trigger the scraping, processing, and email generation.
- **AI Power:** Behind the scenes, the system uses powerful language models (LLM) to draft the email for you.

</div>

<div class="section">
    <h2>📩 Generated Email Output</h2>
    <img src="https://github.com/laxmipriyakotha/Generative-AI/blob/main/img/result.png?raw=true" alt="Generated Email">

    
### Explanation (Email Features)

- **Professional Format:** The generated email follows a structured, formal format suitable for cold outreach.
- **Skill Highlight:** Relevant skills from your portfolio are highlighted, demonstrating your suitability for the role.
- **Custom Tailoring:** Each email is unique to the job description and the portfolio data, ensuring relevance and personalization.
</div>

<div class="section">
    <h2>🚀 Technologies Used</h2>
    <ul>
        <li>Python</li>
        <li>Streamlit (for UI)</li>
        <li>LangChain (for LLM integration)</li>
        <li>BeautifulSoup / Requests (for Web Scraping)</li>
        <li>Environment Variables (for managing sensitive keys)</li>
    </ul>
</div>

<div class="section">
    <h2>⚙️ How to Run</h2>
    <p>Follow these steps to get started:</p>
    <pre>
1. Clone the repository.
2. Set your environment variables (GROQ_API_KEY, etc.) directly in your code or using os.environ if needed.
3. Run the Streamlit app:
   streamlit run app.py
4. Enter any job posting URL and generate your personalized email.
    </pre>
</div>

<div class="section">
    <h2>📌 Future Enhancements</h2>
    <ul>
        <li>Adding support for multiple job postings at once.</li>
        <li>Allowing users to upload their resume/portfolio directly.</li>
        <li>Integrating with LinkedIn to pull job descriptions automatically.</li>
    </ul>
</div>

<div class="section">
    <h2>💡 Inspiration</h2>
    <p>Job hunting can be stressful, and writing personalized emails for each job takes a lot of time. This AI-powered tool speeds up that process, helping job seekers send thoughtful, targeted emails without compromising quality.</p>
</div>

</body>
</html>
