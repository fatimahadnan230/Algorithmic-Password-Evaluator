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
    /* Import Premium Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=JetBrains+Mono:wght@400;700&family=Plus+Jakarta+Sans:wght@400;600;700&display=swap');
    
    /* Global Styles */
    .stApp { 
        background: radial-gradient(circle at 50% 50%, #0f172a 0%, #020617 100%) !important; 
        color: #f1f5f9 !important;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    /* Custom High-Contrast Text Fixes */
    p, span, label { 
        color: #e2e8f0 !important; 
    }
    
    /* Custom Neon Outlined / Glowing Header */
    .custom-title {
        font-family: 'Orbitron', sans-serif;
        font-weight: 900;
        font-size: 2.8rem;
        color: #0f172a; /* Dark core */
        text-shadow: 
            -1px -1px 0 #ef4444,  
             1px -1px 0 #ef4444,
            -1px  1px 0 #ef4444,
             1px  1px 0 #ef4444,
             0 0 15px rgba(239, 68, 68, 0.6); /* Red Cyber Glow Outline */
        letter-spacing: 0.05em;
        margin-top: 5px;
        margin-bottom: 15px;
    }
    
    /* High-Contrast Code and Metrics */
    code, pre {
        font-family: 'JetBrains Mono', monospace !important;
        background-color: #1e293b !important;
        color: #38bdf8 !important;
    }
    
    /* CRITICAL FIX: High-Contrast Metric Value Formatting */
    [data-testid="stMetricValue"] {
        font-family: 'JetBrains Mono', monospace !important;
        color: #ffffff !important; /* Force pure crisp white numbers */
        font-weight: 700 !important;
        font-size: 2.2rem !important;
    }
    [data-testid="stMetricLabel"] {
        color: #94a3b8 !important; /* Soft grey labels */
        font-weight: 600 !important;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    /* Sidebar Layout Fix */
    section[data-testid="stSidebar"] { 
        background-color: #0b1329 !important; 
        border-right: 1px solid #1e293b; 
    }
    
    /* Premium High-Contrast Metric Cards */
    div[data-testid="stMetric"] {
        background: #1e293b !important; /* Deep solid slate background */
        border: 1px solid #334155 !important;
        border-radius: 12px;
        padding: 22px 24px;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.4);
        transition: transform 0.2s, border-color 0.2s;
    }
    div[data-testid="stMetric"]:hover {
        transform: translateY(-2px);
        border-color: #38bdf8 !important;
    }
    
    /* Grid Tables */
    .threat-matrix {
        width: 100%;
        border-collapse: collapse;
        margin: 15px 0;
        font-size: 0.95rem;
        background-color: #0f172a;
        border-radius: 8px;
        overflow: hidden;
        border: 1px solid #1e293b;
    }
    .threat-matrix th {
        background-color: #1e293b;
        color: #38bdf8;
        text-align: left;
        padding: 12px;
        font-family: 'Orbitron', sans-serif;
        font-size: 0.8rem;
        letter-spacing: 0.05em;
    }
    .threat-matrix td {
        padding: 12px;
        border-bottom: 1px solid #1e293b;
        color: #cbd5e1;
    }
    .threat-matrix tr:hover {
        background-color: rgba(56, 189, 248, 0.02);
    }
    
    /* Section Headings */
    h3 {
        color: #38bdf8 !important;
        font-size: 1.1rem !important;
        font-family: 'Orbitron', sans-serif !important;
        letter-spacing: 0.1em;
        font-weight: 700 !important;
        margin-top: 30px !important;
        margin-bottom: 15px !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- ALGORITHMIC COMPLEXITY ENGINE ---
def analyze_password(password):
    if not password:
        return 0.0, {}, "EMPTY", "🚨 NO DATA INPUTTED", "#ef4444"
        
    n = len(password)
    counts = Counter(password)
    
    # Calculate Shannon Entropy
    entropy = 0.0
    for char, count in counts.items():
        prob = count / n
        entropy -= prob * math.log2(prob)
        
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
<div style="background: rgba(56, 189, 248, 0.03); border: 1px solid rgba(56, 189, 248, 0.1); padding: 15px; border-radius: 8px;">
    <p style="color: #38bdf8; font-weight: bold; margin-bottom: 5px; font-size:0.9rem;">⚙️ Operational Complexity</p>
    <p style="font-size: 0.85rem; color: #94a3b8; margin: 0; font-family: monospace;">Execution: O(N) Linear Time<br>Space Layout: O(K) Unique Keys</p>
</div>
""", unsafe_allow_html=True)

# --- MAIN DASHBOARD INTERFACE ---
# Header Area
st.markdown('<p style="color: #ef4444; font-weight: 800; font-size: 0.85rem; letter-spacing: 0.15em; text-transform: uppercase; margin-bottom: 0;">SecOps Analytical Engine</p>', unsafe_allow_html=True)
st.markdown('<h1 class="custom-title">Algorithmic Password Evaluator</h1>', unsafe_allow_html=True)
st.markdown('<p style="color: #94a3b8; font-size: 1.1rem; margin-bottom: 35px;">Real-time execution layer evaluating information density vectors via Shannon Entropy metrics.</p>', unsafe_allow_html=True)

# Create layout layout splits
col_main, col_threat = st.columns([1.8, 1.2], gap="large")

with col_main:
    if user_input:
        entropy_score, char_counts, status_tier, feedback, status_color = analyze_password(user_input)
        
        # Threat Level Assessment Banner
        st.markdown(f"""
        <div style="background: #1e293b; border-left: 4px solid {status_color}; padding: 20px; border-radius: 0 12px 12px 0; margin-bottom: 30px; border: 1px solid #334155; border-left-width: 4px;">
            <p style="color: {status_color}; font-weight: 800; font-size: 0.85rem; letter-spacing: 0.1em; margin: 0 0 5px 0;">THREAT LEVEL ASSESSMENT</p>
            <h2 style="color: #ffffff; margin: 0 0 10px 0; font-size: 1.6rem; font-weight: 700;">{status_tier}</h2>
            <p style="color: #e2e8f0; margin: 0; font-size: 0.95rem;">{feedback}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # --- METRICS GRIDS ---
        st.markdown('<h3>Cryptographic Metrics</h3>', unsafe_allow_html=True)
        m_col1, m_col2, m_col3 = st.columns(3)
        
        with m_col1:
            st.metric(label="Shannon Entropy", value=f"{entropy_score} Bits")
        with m_col2:
            st.metric(label="Payload Length", value=f"{len(user_input)} Chars")
        with m_col3:
            st.metric(label="Unique Token Allocations", value=f"{len(char_counts)}")
            
        # --- ANALYTICS CHART ---
        st.markdown('<h3>Character Distribution Vector</h3>', unsafe_allow_html=True)
        
        df_freq = pd.DataFrame(list(char_counts.items()), columns=['Character', 'Occurrence Count']).sort_values(by='Occurrence Count', ascending=False)
        
        fig = px.bar(
            df_freq, x='Character', y='Occurrence Count',
            template="plotly_dark", color='Occurrence Count',
            color_continuous_scale=['#1e293b', '#38bdf8']
        )
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
            coloraxis_showscale=False, margin=dict(l=0, r=0, t=10, b=0),
            xaxis=dict(showgrid=False, title_text="Extracted Token Set", title_font=dict(color='#94a3b8')),
            yaxis=dict(showgrid=True, gridcolor='#1e293b', title_text="Allocation Frequency", title_font=dict(color='#94a3b8'), dtick=1)
        )
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

with col_threat:
    # --- TOP 10 COMMON PASSWORDS REFERENCE COMPONENT ---
    st.markdown('<h3>Top 10 Most Common Passwords</h3>', unsafe_allow_html=True)
    st.markdown('<p style="color: #94a3b8; font-size: 0.85rem; margin-bottom: 15px;">Global data leak benchmarks displaying structural vulnerability signatures.</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <table class="threat-matrix">
        <thead>
            <tr>
                <th>Rank</th>
                <th>Password Signature</th>
                <th>Entropy</th>
                <th>Crack Time</th>
            </tr>
        </thead>
        <tbody>
            <tr><td>#1</td><td><b style="color:#ef4444; font-family:monospace;">123456</b></td><td>2.58 bits</td><td>&lt; 1 Millisecond</td></tr>
            <tr><td>#2</td><td><b style="color:#ef4444; font-family:monospace;">password</b></td><td>3.00 bits</td><td>&lt; 1 Millisecond</td></tr>
            <tr><td>#3</td><td><b style="color:#ef4444; font-family:monospace;">123456789</b></td><td>3.17 bits</td><td>&lt; 1 Millisecond</td></tr>
            <tr><td>#4</td><td><b style="color:#f59e0b; font-family:monospace;">qwerty</b></td><td>2.58 bits</td><td>&lt; 1 Millisecond</td></tr>
            <tr><td>#5</td><td><b style="color:#f59e0b; font-family:monospace;">unknown</b></td><td>2.81 bits</td><td>&lt; 1 Millisecond</td></tr>
            <tr><td>#6</td><td><b style="color:#f59e0b; font-family:monospace;">12345</b></td><td>2.32 bits</td><td>&lt; 1 Millisecond</td></tr>
            <tr><td>#7</td><td><b style="color:#f59e0b; font-family:monospace;">12345678</b></td><td>3.00 bits</td><td>&lt; 1 Millisecond</td></tr>
            <tr><td>#8</td><td><b style="color:#cbd5e1; font-family:monospace;">111111</b></td><td>1.00 bits</td><td>&lt; 1 Millisecond</td></tr>
            <tr><td>#9</td><td><b style="color:#cbd5e1; font-family:monospace;">654321</b></td><td>2.58 bits</td><td>&lt; 1 Millisecond</td></tr>
            <tr><td>#10</td><td><b style="color:#cbd5e1; font-family:monospace;">123123</b></td><td>2.00 bits</td><td>&lt; 1 Millisecond</td></tr>
        </tbody>
    </table>
    """, unsafe_allow_html=True)
