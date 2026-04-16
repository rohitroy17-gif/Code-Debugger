import streamlit as st
from PIL import Image
from api_calling import issue_generator, solution_generator, hint_generator
import time

# 🔹 Page Config
st.set_page_config(layout="centered")

# 🔹 Title
st.title("🧠 Code Debugger App")
st.subheader("Upload your code image and detect issues instantly")
st.divider()

# 🔹 Upload
image_file = st.file_uploader(
    "📤 Upload your code image",
    type=['jpg', 'png', 'jpeg']
)

if image_file:

    pil_image = Image.open(image_file)

    # 🔹 Preview
    st.subheader("📷 Preview")
    st.image(pil_image, use_container_width=True)

    # 🔹 Option
    option_bar = st.radio(
        "⚙️ Select mode",
        ["Hints", "solution with code"],
        horizontal=True
    )

    # 🔹 Button
    pressed = st.button("🚀 Run AI Debugger", use_container_width=True)

    # 🔥 MAIN LOGIC
    if pressed:

        # 🔹 STATUS UI
        status = st.status("🚀 Starting AI Debugger...", expanded=True)
        progress = st.progress(0)

        # Step 1
        status.write("📤 Processing image...")
        progress.progress(20)
        time.sleep(0.5)

        # Step 2
        status.write("🔍 Analyzing code issues...")
        progress.progress(50)
        generate_issue = issue_generator(pil_image)

        # Step 3
        status.write("🧠 Generating response...")
        progress.progress(80)
        time.sleep(0.5)

        if option_bar == "solution with code":
            generate_code = solution_generator(pil_image)
        else:
            generate_code = hint_generator(pil_image)

        # Step 4
        progress.progress(100)
        status.update(label="✅ Completed", state="complete")

        # 🔹 OUTPUT
        with st.container(border=True):
            st.subheader("🔍 Issues")
            st.markdown(generate_issue)

        with st.container(border=True):
            st.subheader("💡 Result")
            st.markdown(generate_code)

else:
    st.info("👆 Upload an image to get started")  
