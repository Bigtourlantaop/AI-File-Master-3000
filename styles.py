import streamlit as st


def apply_custom_css():
    st.markdown("""
    <style>
    /* ── Google Fonts ── */
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600;700&family=DM+Mono:wght@400;500&display=swap');

    /* ── Root Variables ── */
    :root {
        --primary:       #2563EB;
        --primary-light: #EFF6FF;
        --primary-dark:  #1D4ED8;
        --accent:        #0EA5E9;
        --success:       #10B981;
        --warning:       #F59E0B;
        --danger:        #EF4444;

        --bg:            #F8FAFC;
        --surface:       #FFFFFF;
        --surface-2:     #F1F5F9;
        --border:        #E2E8F0;
        --border-strong: #CBD5E1;

        --text-primary:  #0F172A;
        --text-secondary:#475569;
        --text-muted:    #94A3B8;

        --radius-sm:     6px;
        --radius:        12px;
        --radius-lg:     18px;
        --shadow-sm:     0 1px 3px rgba(0,0,0,.06), 0 1px 2px rgba(0,0,0,.04);
        --shadow:        0 4px 16px rgba(0,0,0,.08);
        --shadow-lg:     0 12px 40px rgba(0,0,0,.12);
        --transition:    all .2s cubic-bezier(.4,0,.2,1);
    }

    /* ── Base ── */
    html, body, [class*="css"] {
        font-family: 'DM Sans', sans-serif !important;
        color: var(--text-primary);
    }
    .stApp {
        background: var(--bg);
    }

    /* ── Hide Streamlit Branding ── */
    #MainMenu, footer, header { visibility: hidden; }

    /* ── Sidebar ── */
    [data-testid="stSidebar"] {
        background: var(--surface) !important;
        border-right: 1px solid var(--border) !important;
        padding-top: 1.5rem;
    }
    [data-testid="stSidebar"] .block-container {
        padding: 0 1rem;
    }
    /* Sidebar nav items */
    [data-testid="stSidebarNav"] a {
        border-radius: var(--radius-sm);
        padding: 0.5rem 0.75rem;
        margin-bottom: 2px;
        transition: var(--transition);
        font-weight: 500;
        font-size: 0.9rem;
        color: var(--text-secondary) !important;
        text-decoration: none;
    }
    [data-testid="stSidebarNav"] a:hover {
        background: var(--primary-light);
        color: var(--primary) !important;
    }
    [data-testid="stSidebarNav"] a[aria-selected="true"] {
        background: var(--primary-light);
        color: var(--primary) !important;
        font-weight: 600;
    }

    /* ── Main Content ── */
    .block-container {
        padding: 2.5rem 3rem !important;
        max-width: 1100px;
    }

    /* ── Headings ── */
    h1 {
        font-size: 2rem !important;
        font-weight: 700 !important;
        color: var(--text-primary) !important;
        letter-spacing: -0.02em;
        margin-bottom: 0.25rem !important;
    }
    h2 {
        font-size: 1.4rem !important;
        font-weight: 600 !important;
        color: var(--text-primary) !important;
        margin-top: 2rem !important;
    }
    h3 {
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        color: var(--text-secondary) !important;
    }

    /* ── Buttons ── */
    .stButton > button {
        background: var(--primary) !important;
        color: #fff !important;
        border: none !important;
        border-radius: var(--radius-sm) !important;
        padding: 0.55rem 1.4rem !important;
        font-family: 'DM Sans', sans-serif !important;
        font-weight: 600 !important;
        font-size: 0.9rem !important;
        letter-spacing: 0.01em;
        box-shadow: 0 1px 4px rgba(37,99,235,.25) !important;
        transition: var(--transition) !important;
        cursor: pointer;
    }
    .stButton > button:hover {
        background: var(--primary-dark) !important;
        box-shadow: 0 4px 12px rgba(37,99,235,.35) !important;
        transform: translateY(-1px);
    }
    .stButton > button:active {
        transform: translateY(0);
    }
    /* Secondary button (outlined) */
    .stButton > button[kind="secondary"] {
        background: transparent !important;
        color: var(--primary) !important;
        border: 1.5px solid var(--primary) !important;
        box-shadow: none !important;
    }
    .stButton > button[kind="secondary"]:hover {
        background: var(--primary-light) !important;
    }

    /* ── Inputs & Selects ── */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stSelectbox > div > div > div,
    .stMultiSelect > div > div > div,
    .stNumberInput > div > div > input {
        border: 1.5px solid var(--border) !important;
        border-radius: var(--radius-sm) !important;
        background: var(--surface) !important;
        color: var(--text-primary) !important;
        font-family: 'DM Sans', sans-serif !important;
        font-size: 0.9rem !important;
        padding: 0.5rem 0.75rem !important;
        transition: var(--transition) !important;
    }
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: var(--primary) !important;
        box-shadow: 0 0 0 3px rgba(37,99,235,.12) !important;
        outline: none !important;
    }
    /* Input label */
    .stTextInput label, .stTextArea label,
    .stSelectbox label, .stMultiSelect label,
    .stNumberInput label {
        font-weight: 600 !important;
        font-size: 0.82rem !important;
        color: var(--text-secondary) !important;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 4px !important;
    }

    /* ── Metric Cards ── */
    [data-testid="metric-container"] {
        background: var(--surface);
        border: 1px solid var(--border);
        border-radius: var(--radius);
        padding: 1.25rem 1.5rem;
        box-shadow: var(--shadow-sm);
        transition: var(--transition);
    }
    [data-testid="metric-container"]:hover {
        box-shadow: var(--shadow);
        transform: translateY(-2px);
    }
    [data-testid="metric-container"] [data-testid="stMetricLabel"] {
        font-size: 0.78rem !important;
        font-weight: 600 !important;
        color: var(--text-muted) !important;
        text-transform: uppercase;
        letter-spacing: 0.08em;
    }
    [data-testid="metric-container"] [data-testid="stMetricValue"] {
        font-size: 2rem !important;
        font-weight: 700 !important;
        color: var(--text-primary) !important;
    }

    /* ── Dataframe / Table ── */
    .stDataFrame {
        border: 1px solid var(--border) !important;
        border-radius: var(--radius) !important;
        overflow: hidden;
        box-shadow: var(--shadow-sm);
    }
    .stDataFrame thead th {
        background: var(--surface-2) !important;
        font-weight: 600 !important;
        font-size: 0.82rem !important;
        color: var(--text-secondary) !important;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    /* ── Expander ── */
    .streamlit-expanderHeader {
        background: var(--surface) !important;
        border: 1px solid var(--border) !important;
        border-radius: var(--radius-sm) !important;
        font-weight: 600 !important;
        color: var(--text-primary) !important;
        transition: var(--transition) !important;
    }
    .streamlit-expanderHeader:hover {
        background: var(--primary-light) !important;
        border-color: var(--primary) !important;
        color: var(--primary) !important;
    }

    /* ── Tabs ── */
    .stTabs [data-baseweb="tab-list"] {
        border-bottom: 2px solid var(--border) !important;
        gap: 0;
    }
    .stTabs [data-baseweb="tab"] {
        font-family: 'DM Sans', sans-serif !important;
        font-weight: 600 !important;
        font-size: 0.9rem !important;
        color: var(--text-muted) !important;
        padding: 0.6rem 1.2rem !important;
        border-radius: var(--radius-sm) var(--radius-sm) 0 0 !important;
        transition: var(--transition) !important;
    }
    .stTabs [aria-selected="true"] {
        color: var(--primary) !important;
        border-bottom: 2px solid var(--primary) !important;
        background: var(--primary-light) !important;
    }

    /* ── File Uploader ── */
    [data-testid="stFileUploader"] {
        border: 2px dashed var(--border-strong) !important;
        border-radius: var(--radius) !important;
        background: var(--surface) !important;
        transition: var(--transition) !important;
        padding: 1rem !important;
    }
    [data-testid="stFileUploader"]:hover {
        border-color: var(--primary) !important;
        background: var(--primary-light) !important;
    }

    /* ── Alert / Info boxes ── */
    .stAlert {
        border-radius: var(--radius-sm) !important;
        border-left-width: 4px !important;
        font-size: 0.9rem !important;
    }

    /* ── Scrollbar ── */
    ::-webkit-scrollbar { width: 6px; height: 6px; }
    ::-webkit-scrollbar-track { background: transparent; }
    ::-webkit-scrollbar-thumb {
        background: var(--border-strong);
        border-radius: 99px;
    }
    ::-webkit-scrollbar-thumb:hover { background: var(--text-muted); }

    /* ── Divider ── */
    hr {
        border: none !important;
        border-top: 1px solid var(--border) !important;
        margin: 1.5rem 0 !important;
    }

    /* ── Spinner ── */
    .stSpinner > div {
        border-top-color: var(--primary) !important;
    }

    /* ── Progress bar ── */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, var(--primary), var(--accent)) !important;
        border-radius: 99px !important;
    }
    .stProgress > div > div > div {
        border-radius: 99px !important;
        background: var(--border) !important;
    }

    </style>
    """, unsafe_allow_html=True)
