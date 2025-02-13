import streamlit as st
from modules.pdf_chat import chat_with_pdf
from modules.image_captioning import image_captioning
from modules.summarization import text_summarization

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="AI Multi-Service App 🚀",
    layout="wide",
    page_icon="🤖",
    initial_sidebar_state="expanded",
)

# --- CUSTOM CSS STYLES ---
st.markdown("""
    <style>
        /* Sidebar customization */
        [data-testid="stSidebar"] {
            background-color: #1e293b;
            color: white;
        }
        [data-testid="stSidebarNav"] ul {
            padding-left: 10px;
        }
        /* Main content */
        .main-title {
            font-size: 40px;
            font-weight: bold;
            color: #ff6600;
            text-align: center;
        }
        .sub-header {
            font-size: 20px;
            color: #4b5563;
            text-align: center;
            margin-bottom: 20px;
        }
        .footer {
            font-size: 14px;
            color: #94a3b8;
            text-align: center;
            margin-top: 50px;
        }
        /* Buttons */
        .stButton>button {
            background-color: #ff6600 !important;
            color: white !important;
            border-radius: 10px;
            font-size: 18px;
            padding: 10px;
        }
        /* Animations */
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        .fade-in {
            animation: fadeIn 1s;
        }
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<h1 class="main-title">AI Multi-Service App 🚀</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Empowering AI services in one place</p>', unsafe_allow_html=True)


menu = st.sidebar.radio(
    "🔍 Choose a Service",
    ["📄 Chat with PDF", "🖼️ Image Captioning", "📜 Summarization"]
)

# --- PAGE CONTENT ---
st.markdown('<div class="fade-in">', unsafe_allow_html=True)  # Add fade-in animation
if menu == "📄 Chat with PDF":
    chat_with_pdf()
elif menu == "🖼️ Image Captioning":
    image_captioning()
elif menu == "📜 Summarization":
    text_summarization()
st.markdown('</div>', unsafe_allow_html=True)  # Close fade-in div

# --- FOOTER ---
st.markdown('<p class="footer">© 2025 AI Multi-Service App | Built with ❤️ using Streamlit</p>', unsafe_allow_html=True)
