from google import genai
from dotenv import load_dotenv
import os
import streamlit as st
import google.api_core.exceptions
load_dotenv()

api_key=os.getenv("GEMINI_API_KEY")
client= genai.Client(api_key=api_key)

def issue_generator(images):
    prompt="""Act as a senior software engineer and code reviewer.
    Carefully analyze the uploaded image containing code.
    Your task is to detect and explain issues in the code.
    Provide output in structured format:
    - Issue Summary: Short one-line descriptio
    - Error Category: (Syntax / Runtime / Logical / Performance)
    - Detailed Explanation: What is wrong and why
    - Possible Cause: What might have led to this mistake
    - Severity: (Low / Medium / High)
    Constraints:
    - Do NOT generate corrected code
    - Do NOT suggest fixes
    - Only focus on identifying problems
    - If multiple issues exist, list them separately"""
 
    try:
         response=client.models.generate_content(
                            
              model="gemini-3-flash-preview",
              contents=[images,prompt])
         
         return response.text
    except Exception as e:         
          if "429" in str(e):
               st.error("⚠️ API limit reached. Please wait ~1 minute and try again.")
          else:
               st.error(f"Error: {e}")

  

def solution_generator(image):
    prompt = """
You are a code fixer.

Return ONLY the corrected version of the code from the image.

STRICT RULES:
- Output ONLY code
- Use ```python markdown block
- No explanation
- No issue description
"""
    try:
         
         response = client.models.generate_content(
             model="gemini-3-flash-preview",
             contents=[prompt, image] )
         return response.text
    except Exception as e:         
          if "429" in str(e):
               st.error("⚠️ API limit reached. Please wait ~1 minute and try again.")
          else:
               st.error(f"Error: {e}")


def hint_generator(image):
    prompt = """
Analyze the code and give hints only.

Output:
- Hint
- Direction

Do NOT provide code.
"""
    try:
          response = client.models.generate_content(
               
                model="gemini-3-flash-preview",
                contents=[prompt, image])
          return response.text
    except Exception as e:         
          if "429" in str(e):
               st.error("⚠️ API limit reached. Please wait ~1 minute and try again.")
          else:
               st.error(f"Error: {e}")
