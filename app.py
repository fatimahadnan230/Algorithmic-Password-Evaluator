import streamlit as st
import math
from collections import Counter
import plotly.express as px
import pandas as pd

# Page config for high-end analytics layout
st.set_page_config(
    page_title="Algorithmic Password Intelligence Engine", 
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ADVANCED CYBERSECURITY THEME ENGINE (CSS) ---
st.markdown("""
    <style>
    /* Global Styles */
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Plus+Jakarta+Sans:wght@400;600;800&display=swap');
    
    .stApp { 
        background: radial-gradient(circle at 50% 50%, #0f172a 0%, #020617 100%) !important; 
        color: #f8fafc !important;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    /* Code and Metrics Font */
    code, pre, [data-testid="stMetricValue"] {
        font-family: 'JetBrains Mono', monospace !important;
    }
    
    /* Sidebar Overhaul */
    section[data-testid="stSidebar"] { 
        background-color: #0b1329 !important; 
        border-right: 1px solid #1e293b; 
    }
    
    /* Premium Metric Card Containers */
    div[data-testid="stMetric"] {
        background: rgba(30, 41, 59, 0.4);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 12px;
        padding: 20px 24px;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.2);
        backdrop-filter: blur(5px);
        transition: transform 0.2s, border-color 0.2s;
    }
    div[data-testid="stMetric"]:hover {
        transform: translateY(-2px);
        border-color: rgba(56, 189, 248, 0.3);
    }
    
    /* Section Headings */
    h3 {
        color: #94a3b8 !important;
        font-size: 1.1rem !important;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        font-weight: 700 !important;
        margin-bottom: 15px !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- ALGORITHMIC COMPLEXITY ENGINE ---
def analyze_password(password):
    if not password:
        return 0.0, {}, "EMPTY", "🚨 NO DATA INPUTTED", "#ef4444"
        
    n = len(password)
    # Character frequency tracking - O(N) Time Complexity
    counts = Counter(password)
    
    # Calculate Shannon Entropy: H(X) = -sum(P(xi) * log2(P(xi)))
    entropy = 0.0
    for char, count in counts.items():
        prob = count / n
        entropy -= prob * math.log2(prob)
        
    # Strategic classifications based on cryptographic entropy thresholds
    if entropy < 2.5:
        return round(entropy, 2), counts, "CRITICAL WEAKNESS", "🔴 Highly predictable pattern. Susceptible to trivial dictionary attacks.", "#ef4444"
    elif entropy < 3.5:
        return round(entropy, 2), counts, "MODERATE EXPOSURE", "🟡 Standard alphanumeric structure. Susceptible to targeted brute-forcing.", "#f59e0b"
    else:
        return round(entropy, 2), counts, "CRYPTOGRAPHICALLY SECURE", "🟢 Excellent randomness density. Resilient against standard algorithmic guessing.", "#10b981"

# --- SIDEBAR INTERFACE ---
st.sidebar.markdown('<p style="color: #38bdf8; font-weight: 800; font-size: 0.85rem; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 0;">Control Panel</p>', unsafe_allow_html=True)
st.sidebar.markdown('<h2 style="color: #ffffff; font-weight: 800; font-size: 1.5rem; margin-top: 5px; margin-bottom: 25px;">Input Vector</h2>', unsafe_allow_html=True)

user_input = st.sidebar.text_input("ENTER TARGET STRING:", value="P@ssw0rd123!", type="password")

st.sidebar.markdown("<br><hr style='border-color: #1e293b;'><br>", unsafe_allow_html=True)
st.sidebar.markdown("""
<div style="background: rgba(56, 189, 248, 0.05); border: 1px solid rgba(56, 189, 248, 0.1); padding: 15px; border-radius: 8px;">
    <p style="color: #38bdf8; font-weight: bold; margin-bottom: 5px; font-size:0.9rem;">⚙️ Operational Complexity</p>
    <p style="font-size: 0.85rem; color: #94a3b8; margin: 0; font-family: monospace;">Execution: O(N) Linear Time<br>Space Layout: O(K) Unique Keys</p>
</div>
""", unsafe_allow_html=True)

# --- MAIN DASHBOARD INTERFACE ---
# Header Area
st.markdown('<p style="color: #ef4444; font-weight: 800; font-size: 0.85rem; letter-spacing: 0.15em; text-transform: uppercase; margin-bottom: 0;">SecOps Analytical Engine</p>', unsafe_allow_html=True)
st.markdown('<h1 style="color: #ffffff; font-family: sans-serif; font-weight: 800; font-size: 2.5rem; margin-top: 0; margin-bottom: 10px;">Algorithmic Password Evaluator</h1>', unsafe_allow_html=True)
st.markdown('<p style="color: #94a3b8; font-size: 1.1rem; margin-bottom: 35px;">Real-time execution layer evaluating information density vectors via Shannon Entropy metrics.</p>', unsafe_allow_html=True)

if user_input:
    entropy_score, char_counts, status_tier, feedback, status_color = analyze_password(user_input)
    
    # Big Status Alert Banner
    st.markdown(f"""
    <div style="background: rgba(30, 41, 59, 0.3); border-left: 4px solid {status_color}; padding: 20px; border-radius: 0 12px 12px 0; margin-bottom: 30px;">
        <p style="color: {status_color}; font-weight: 800; font-size: 0.85rem; letter-spacing: 0.1em; margin: 0 0 5px 0;">THREAT LEVEL ASSESSMENT</p>
        <h2 style="color: #ffffff; margin: 0 0 10px 0; font-size: 1.6rem; font-weight: 700;">{status_tier}</h2>
        <p style="color: #cbd5e1; margin: 0; font-size: 0.95rem;">{feedback}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # --- LEVEL 1 METRICS ---
    st.markdown('<h3>Cryptographic Metrics</h3>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="Calculated Shannon Entropy", value=f"{entropy_score} Bits")
    with col2:
        st.metric(label="Total Payload Length", value=f"{len(user_input)} Chars")
    with col3:
        st.metric(label="Unique Character Allocations", value=f"{len(char_counts)}")
        
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- LEVEL 2 ANALYTICS CHART ---
    st.markdown('<h3>Character Distribution Vector</h3>', unsafe_allow_html=True)
    
    # Build frequency Dataframe
    df_freq = pd.DataFrame(list(char_counts.items()), columns=['Character', 'Occurrence Count']).sort_values(by='Occurrence Count', ascending=False)
    
    # Styled High-end Chart
    fig = px.bar(
        df_freq, 
        x='Character', 
        y='Occurrence Count',
        template="plotly_dark",
        color='Occurrence Count',
        color_continuous_scale=['#1e293b', '#38bdf8']
    )
    
    # Flawless Chart Layout Integration
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', 
        plot_bgcolor='rgba(0,0,0,0)',
        coloraxis_showscale=False,
        margin=dict(l=0, r=0, t=10, b=0),
        xaxis=dict(showgrid=False, title_text="Extracted Token Set"),
        yaxis=dict(showgrid=True, gridcolor='#1e293b', title_text="Allocation Frequency", dtick=1)
    )
    fig.update_traces(marker_line_color='rgba(0,0,0,0)', marker_line_width=0)
    
    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
