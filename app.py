import streamlit as st

st.set_page_config(
    page_title="DataForge — Universal Data Converter",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Inject global CSS
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

from pages import home, converter, preview, about

PAGES = {
    "🏠 Home": home,
    "⚡ Convert": converter,
    "👁️ Preview & Download": preview,
    "ℹ️ About": about,
}

with st.sidebar:
    st.markdown('<div class="sidebar-logo">⚡ DataForge</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-tagline">Universal Data → Excel</div>', unsafe_allow_html=True)
    st.markdown("---")
    selection = st.radio("Navigation", list(PAGES.keys()), label_visibility="collapsed")
    st.markdown("---")
    st.markdown(
        '<div class="sidebar-footer">Built with ❤️ · Open Source</div>',
        unsafe_allow_html=True,
    )

PAGES[selection].render()
