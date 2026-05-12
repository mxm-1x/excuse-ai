import streamlit as st
import time
# -- MONKEYPATCH FOR PYTHON 3.14 + STREAMLIT CLOUD + CHROMADB BUG --
import sys
import os

# Streamlit Cloud uses Python 3.14 which breaks Pydantic v1 (used by ChromaDB/CrewAI).
# This patch forces Pydantic v1 to understand the type of `env_file_encoding`.
try:
    import pydantic.v1.fields
    original_infer = pydantic.v1.fields.ModelField.infer
    def patched_infer(*args, **kwargs):
        if kwargs.get('name') == 'env_file_encoding' or (args and args[0] == 'env_file_encoding'):
            kwargs['annotation'] = str
        return original_infer(*args, **kwargs)
    pydantic.v1.fields.ModelField.infer = patched_infer
except ImportError:
    pass
# -------------------------------------------------------------------

# Add the backend directory to path so we can import the crew
sys.path.append(os.path.join(os.path.dirname(__file__), "backend"))

from app.crew.crew import ExcuseCrew

# Page Config
st.set_page_config(
    page_title="ExcuseAI",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main {
        background-color: #0a0a0f;
        color: white;
    }
    h1, h2, h3 {
        color: #d8b4fe;
    }
    .stButton>button {
        background-color: #8b5cf6;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 24px;
        font-weight: 600;
        width: 100%;
        transition: background-color 0.3s;
    }
    .stButton>button:hover {
        background-color: #7c3aed;
    }
    .result-box {
        background-color: #18181b;
        border: 1px solid #27272a;
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 20px;
    }
    .risk-score {
        font-size: 24px;
        font-weight: bold;
        color: #f87171;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.title("⚡ ExcuseAI")
st.markdown("The **slightly unethical** AI tool that generates the perfect excuse for any situation. Powered by CrewAI.")

# Form Input
with st.container():
    st.markdown("### 📝 Generate Your Excuse")
    
    situation = st.text_area("What is the situation?", placeholder="E.g., I missed the 9 AM team meeting because I overslept...")
    
    col1, col2 = st.columns(2)
    with col1:
        relationship = st.selectbox("Who are you giving the excuse to?", ["Boss", "Teacher", "Partner", "Friend", "Parent"])
        urgency = st.slider("Urgency level", 1, 100, 50)
    with col2:
        tone = st.selectbox("Tone of the excuse", ["Professional", "Casual", "Dramatic", "Emotional", "Funny"])
    
    generate_btn = st.button("Generate Excuse")

# Generation Logic
if generate_btn:
    if not situation:
        st.warning("Please describe the situation first!")
    else:
        st.markdown("---")
        
        # Display simulated loading steps for UX
        status_text = st.empty()
        progress_bar = st.progress(0)
        
        status_text.text("🤖 Waking up AI agents...")
        progress_bar.progress(10)
        time.sleep(1)
        
        status_text.text("🔍 Analyzing the situation and relationship...")
        progress_bar.progress(30)
        
        try:
            # Run the actual CrewAI logic
            crew = ExcuseCrew(
                situation=situation,
                relationship=relationship,
                tone=tone,
                urgency=urgency
            )
            
            result = crew.run()
            
            progress_bar.progress(100)
            status_text.text("✅ Excuse generated successfully!")
            
            # Extract output
            output = None
            if hasattr(result, 'pydantic') and result.pydantic:
                output = result.pydantic
            
            if output:
                st.markdown("## Your Excuse Package")
                
                st.markdown('<div class="result-box">', unsafe_allow_html=True)
                st.subheader("⚠️ Main Excuse")
                st.write(output.main_excuse)
                st.markdown('</div>', unsafe_allow_html=True)
                
                st.markdown('<div class="result-box">', unsafe_allow_html=True)
                st.subheader("💭 Emotional Justification")
                st.write(output.emotional_reasoning)
                st.markdown('</div>', unsafe_allow_html=True)
                
                col3, col4 = st.columns(2)
                with col3:
                    st.markdown('<div class="result-box">', unsafe_allow_html=True)
                    st.subheader("📱 WhatsApp Message")
                    st.write(output.whatsapp_message)
                    st.markdown('</div>', unsafe_allow_html=True)
                with col4:
                    st.markdown('<div class="result-box">', unsafe_allow_html=True)
                    st.subheader("✉️ Email Version")
                    st.write(output.email_message)
                    st.markdown('</div>', unsafe_allow_html=True)
                
                st.markdown('<div class="result-box">', unsafe_allow_html=True)
                st.subheader("🔮 Follow-up Answers (If they ask)")
                for ans in output.follow_up_answers:
                    st.markdown(f"- {ans}")
                st.markdown('</div>', unsafe_allow_html=True)
                
                st.markdown('<div class="result-box" style="text-align: center;">', unsafe_allow_html=True)
                st.subheader("🚨 Risk Score")
                st.markdown(f'<span class="risk-score">{output.risk_score} / 10</span>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
                
            else:
                st.error("Failed to generate structured response. Raw output:")
                st.write(result.raw)
                
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
