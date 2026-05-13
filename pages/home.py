import streamlit as st


FORMATS = [
    ".csv", ".tsv", ".json", ".jsonl", ".xml", ".xlsx", ".xls", ".ods",
    ".parquet", ".feather", ".html", ".pdf", ".txt", ".log",
    ".yaml", ".yml", ".sql", ".avro", ".hdf5", ".pickle",
    "Plain Text", "Pasted Data",
]

FEATURES = [
    ("🧠", "Smart Detection", "Auto-detects file type, encoding, delimiter, and data shape — no manual config needed."),
    ("🔄", "40+ Formats", "CSV, JSON, XML, PDF, Parquet, SQL dumps, HTML tables, YAML, logs, and raw text."),
    ("🧹", "Auto Clean", "Strips nulls, fixes types, normalises headers, deduplicates rows automatically."),
    ("📊", "Multi-sheet", "Splits data into organised Excel sheets with summaries and type-info tabs."),
    ("⚡", "Fast & Local", "All processing in-memory. Your data never leaves your browser session."),
    ("📥", "Bulk Upload", "Process multiple files at once and merge or keep them as separate sheets."),
]


def render():
    st.markdown('<div class="hero-title">Turn Any Data<br>Into Excel. Instantly.</div>', unsafe_allow_html=True)
    st.markdown(
        '<p class="hero-sub">DataForge auto-detects your file type, cleans the mess, '
        'and exports a perfectly structured Excel workbook — no config, no code.</p>',
        unsafe_allow_html=True,
    )

    col1, col2, col3, col4 = st.columns(4)
    for col, (num, label) in zip(
        [col1, col2, col3, col4],
        [("40+", "Formats"), ("∞", "File Size*"), ("0", "Config Needed"), ("100%", "Private")],
    ):
        with col:
            st.markdown(
                f'<div class="df-stat"><div class="df-stat-num">{num}</div>'
                f'<div class="df-stat-label">{label}</div></div>',
                unsafe_allow_html=True,
            )

    st.markdown("---")
    st.markdown("### Supported Input Formats")
    chips = "".join(f'<span class="format-chip">{f}</span>' for f in FORMATS)
    st.markdown(f'<div class="format-grid">{chips}</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### Why DataForge?")
    cols = st.columns(3)
    for i, (icon, title, desc) in enumerate(FEATURES):
        with cols[i % 3]:
            st.markdown(
                f'<div class="df-card"><div style="font-size:1.8rem">{icon}</div>'
                f'<h4 style="color:#00e5ff;margin:0.5rem 0 0.3rem">{title}</h4>'
                f'<p style="color:#64748b;font-size:0.88rem;line-height:1.6">{desc}</p></div>',
                unsafe_allow_html=True,
            )

    st.markdown("---")
    st.markdown(
        '<p style="color:#64748b;font-size:0.75rem">* Large files may be slow depending on your machine. '
        'Streamlit Cloud has a 200 MB upload limit.</p>',
        unsafe_allow_html=True,
    )
