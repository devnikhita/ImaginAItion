import streamlit as st
import requests
from PIL import Image
import io

# FastAPI backend URL
API_URL = "http://127.0.0.1:8000"

# Streamlit App Customization
st.set_page_config(
    page_title="ImaginAItion",
    page_icon="🎨",
    layout="wide",
)

# Custom CSS for Styling
st.markdown(
    """
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f9f9f9;
        }
        .main-title {
            text-align: center;
            font-size: 48px;
            color: #6200ea;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .subtitle {
            text-align: center;
            font-size: 20px;
            color: #555;
            margin-bottom: 40px;
        }
        .text-input {
            font-size: 16px !important;
            height: 80px !important;
        }
        .history-image {
            max-height: 150px;
            max-width: 150px;
            margin: 5px;
        }
        .stButton > button {
            background-color: #6200ea;
            color: white;
            border-radius: 8px;
            padding: 10px;
        }
        .stButton > button:hover {
            background-color: #3700b3;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# App Title
st.markdown('<h1 class="main-title">🎨 ImaginAItion</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Where words shape worlds—craft captivating visuals with the art of AI.</p>', unsafe_allow_html=True)


# Sidebar: Service Status
st.sidebar.header("Service Status")
try:
    health_response = requests.get(f"{API_URL}/health")
    if health_response.status_code == 200:
        health_status = health_response.json()
        st.sidebar.success(f"✅ {health_status['status']} on {health_status['device'].upper()}")
    else:
        st.sidebar.error("❌ Service is unavailable.")
except requests.exceptions.RequestException:
    st.sidebar.error("❌ Failed to connect to the backend.")

# Generate New Image
st.markdown("### 📝 Enter the prompt:")
prompt = st.text_area(
    "",
    placeholder="E.g., A futuristic cityscape at sunset 🌃",
    height=150,
)
generate_button = st.button("✨ Generate Image")

if generate_button:
    if prompt.strip():
        with st.spinner("Generating image... ⏳"):
            try:
                response = requests.get(f"{API_URL}/generate", params={"prompt": prompt})
                if response.status_code == 200:
                    image = Image.open(io.BytesIO(response.content))
                    st.image(image, caption="Generated Image", use_column_width=True)
                    # Add download button
                    st.download_button(
                        label="⬇️ Download Image",
                        data=io.BytesIO(response.content),
                        file_name="generated_image.png",
                        mime="image/png",
                    )
                else:
                    st.error("⚠️ Failed to generate the image.")
            except requests.exceptions.RequestException as e:
                st.error(f"⚠️ Error: {e}")
    else:
        st.warning("⚠️ Please enter a prompt.")

# Display History
st.markdown("### 🗂️ Prompt History:")
try:
    history_response = requests.get(f"{API_URL}/history")
    if history_response.status_code == 200:
        history = history_response.json()
        if history:
            cols = st.columns(3)  # Arrange images in a grid
            for idx, entry in enumerate(history):
                with cols[idx % 3]:
                    st.image(entry["image_path"], caption=entry["prompt"], use_column_width=True)
        else:
            st.info("No history found.")
    else:
        st.error("⚠️ Failed to fetch history.")
except requests.exceptions.RequestException as e:
    st.error(f"⚠️ Error: {e}")

# Clear History
st.markdown("### 🔄 Clear History:")
clear_history = st.button("🗑️ Clear Prompt History")
if clear_history:
    try:
        clear_response = requests.delete(f"{API_URL}/history")
        if clear_response.status_code == 200:
            st.success("✅ History cleared successfully!")
        else:
            st.error("⚠️ Failed to clear history.")
    except requests.exceptions.RequestException as e:
        st.error(f"⚠️ Error: {e}")
