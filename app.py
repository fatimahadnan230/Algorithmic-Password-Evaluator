import streamlit as st
import math
from collections import Counter
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Password Evaluator", layout="wide")

# --- PREMIUM VISUAL STYLING ---
st.markdown("""
    <style>
    .stApp { background-color: #0f172a !important; color: #f8fafc !important; }
    p, span, label, h3 { color: #cbd5e1 !important; }
    section[data-testid="stSidebar"] { background-color: #1e293b !important; border-right: 1px solid #334155; }
    table { color: #f8fafc !important; background-color: #1e293b !important; border-radius: 8px; width: 100%; }
    th { background-color: #334155 !important; color: #38bdf8 !important; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 style="color: #ef4444; font-family: sans-serif; font-weight: 800;">🔐 Algorithmic Password Evaluator</h1>', unsafe_allow_html=True)
st.markdown("Evaluate string complexity using linear-time Shannon Entropy metrics and token frequency analysis.")
st.markdown("<br>", unsafe_allow_html=True)

# --- ALGORITHMIC EVALUATION ENGINE ---
def analyze_password(password):
    if not password:
        return 0, {}, "Empty input"
        
    n = len(password)
    # Character frequency tracking - O(N) Time Complexity
    counts = Counter(password)
    
    # Calculate Shannon Entropy
    entropy = 0.0
    for char, count in counts.items():
        prob = count / n
        entropy -= prob * math.log2(prob)
        
    if entropy < 2.5:
        strength = "🔴 Weak (Highly Predictable / Repetitive)"
    elif entropy < 3.5:
        strength = "🟡 Moderate (Basic Alphanumeric Mixture)"
    else:
        strength = "🟢 Strong (High Randomness / Cryptographically Sound)"
        
    return round(entropy, 2), counts, strength

# UI Sidebar Layout
st.sidebar.markdown('<h2 style="color: #f8fafc; font-size: 1.5rem;">User Input</h2>', unsafe_allow_html=True)
user_input = st.sidebar.text_input("Enter a password string to test:", value="P@ssw0rd123!", type="password")

if user_input:
    entropy_score, char_counts, strength_rating = analyze_password(user_input)
    
    # --- METRIC CARDS ---
    col1, col2, col3 = st.columns(3)
    col1.metric("Calculated Shannon Entropy", f"{entropy_score} bits")
    col2.metric("String Total Length", f"{len(user_input)} chars")
    col3.metric("Unique Character Sets", f"{len(char_counts)}")
    
    st.markdown(f"### Complexity Tier: {strength_rating}")
    st.markdown("<hr style='border-color: #334155;'>", unsafe_allow_html=True)
    
    # --- VISUALIZATION CHART ---
    st.markdown('<h3>Character Frequency Vector</h3>', unsafe_allow_html=True)
    
    df_freq = pd.DataFrame(list(char_counts.items()), columns=['Character', 'Occurrence Count'])
    
    fig = px.bar(
        df_freq, x='Character', y='Occurrence Count',
        template="plotly_dark",
        color_discrete_sequence=['#38bdf8']
    )
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig, use_container_width=True)
