import streamlit as st

FORMATS_TABLE = [
    ("CSV / TSV", "Comma or tab-separated values, any delimiter", "✅ Full"),
    ("JSON / JSONL", "Nested objects, arrays, JSON Lines", "✅ Full"),
    ("XML", "Any XML with repeated elements as rows", "✅ Full"),
    ("Excel (xlsx, xls, ods)", "All sheets preserved", "✅ Full"),
    ("Parquet / Feather", "Arrow/columnar formats", "✅ Full"),
    ("PDF", "Tables extracted per page; text fallback", "✅ Tables + Text"),
    ("HTML", "All <table> elements extracted", "✅ Full"),
    ("YAML / YML", "Key-value and list structures", "✅ Full"),
    ("SQL Dump", "INSERT INTO statements parsed to rows", "✅ Full"),
    ("HDF5", "All datasets/keys extracted", "✅ Full"),
    ("Avro", "Schema-inferred tabular data", "✅ Full"),
    ("Pickle", "Pandas DataFrames and dicts", "✅ Full"),
    ("Log / TXT", "Structured log parsing, key=value, CSV fallback", "✅ Auto-detect"),
    ("Pasted Text", "Any format pasted directly", "✅ Auto-detect"),
]


def render():
    st.markdown("## ℹ️ About DataForge")
    st.markdown(
        '<p class="hero-sub">DataForge is an open-source universal data converter. '
        'It turns any raw file or pasted data into a clean, formatted Excel workbook — '
        'automatically, with zero configuration.</p>',
        unsafe_allow_html=True,
    )

    st.markdown("---")
    st.markdown("### Supported Formats")

    # Build table
    rows = ""
    for fmt, desc, support in FORMATS_TABLE:
        rows += f"<tr><td><code>{fmt}</code></td><td style='color:#94a3b8'>{desc}</td><td style='color:#00c896'>{support}</td></tr>"

    st.markdown(
        f"""
        <table style="width:100%;border-collapse:collapse;font-size:0.88rem">
          <thead>
            <tr style="border-bottom:1px solid #1e2330">
              <th style="text-align:left;padding:0.5rem;color:#00e5ff">Format</th>
              <th style="text-align:left;padding:0.5rem;color:#00e5ff">Notes</th>
              <th style="text-align:left;padding:0.5rem;color:#00e5ff">Support</th>
            </tr>
          </thead>
          <tbody>{rows}</tbody>
        </table>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")
    st.markdown("### How It Works")
    steps = [
        ("1️⃣", "Upload or paste", "Drop any file or paste raw text. DataForge reads the bytes directly."),
        ("2️⃣", "Smart Detection", "Extension + content sniffing determines the exact format and encoding."),
        ("3️⃣", "Parse", "The right parser is selected automatically — no user config needed."),
        ("4️⃣", "Clean", "Nulls dropped, types cast, headers normalised, duplicates removed."),
        ("5️⃣", "Export", "A formatted Excel workbook is generated with all sheets + a summary tab."),
    ]
    cols = st.columns(5)
    for col, (icon, title, desc) in zip(cols, steps):
        with col:
            st.markdown(
                f'<div class="df-card" style="text-align:center">'
                f'<div style="font-size:1.5rem">{icon}</div>'
                f'<div style="color:#00e5ff;font-weight:700;margin:0.5rem 0 0.25rem">{title}</div>'
                f'<div style="color:#64748b;font-size:0.8rem">{desc}</div></div>',
                unsafe_allow_html=True,
            )

    st.markdown("---")
    st.markdown("### Tech Stack")
    st.markdown(
        """
        | Component | Library |
        |---|---|
        | Web App | Streamlit |
        | Data Processing | Pandas, NumPy |
        | Excel Output | openpyxl |
        | PDF Parsing | pdfplumber |
        | Encoding Detection | chardet |
        | YAML | PyYAML |
        | Avro | fastavro |
        | Parquet | pyarrow |
        """
    )

    st.markdown("---")
    st.markdown(
        '<div style="color:#64748b;font-size:0.85rem">DataForge is open source under MIT license. '
        'Star it on GitHub and contribute!</div>',
        unsafe_allow_html=True,
    )
