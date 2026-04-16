import google.generativeai as genai
from dotenv import load_dotenv
import os
import streamlit as st

# 🔹 Load API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

# 🔹 Use model once (efficient)
model = genai.GenerativeModel("gemini-1.5-flash")


# 🔍 ISSUE GENERATOR
def issue_generator(image):
    prompt = """Act as a senior software engineer and code reviewer.
Analyze the uploaded image containing code.

Output format:
- Issue Summary
- Error Category
- Detailed Explanation
- Possible Cause
- Severity

Rules:
- DO NOT generate code
- DO NOT suggest fixes
"""

    try:
        response = model.generate_content([prompt, image])
        return response.text

    except Exception as e:
        if "429" in str(e):
            st.error("⚠️ API limit reached. Please wait ~1 minute.")
        else:
            st.error(f"Error: {e}")


# 💡 SOLUTION GENERATOR
def solution_generator(image):
    prompt = """
Return ONLY the corrected version of the code.

Rules:
- Output ONLY code
- Use ```python block
- No explanation
"""

    try:
        response = model.generate_content([prompt, image])
        return response.text

    except Exception as e:
        if "429" in str(e):
            st.error("⚠️ API limit reached. Please wait ~1 minute.")
        else:
            st.error(f"Error: {e}")


# 🧠 HINT GENERATOR
def hint_generator(image):
    prompt = """
Analyze the code and give hints only.

Output:
- Hint
- Direction

Do NOT provide code.
"""

    try:
        response = model.generate_content([prompt, image])
        return response.text

    except Exception as e:
        if "429" in str(e):
            st.error("⚠️ API limit reached. Please wait ~1 minute.")
        else:
            st.error(f"Error: {e}")
