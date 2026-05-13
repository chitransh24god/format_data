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
        rows += f"<tr style='border-bottom:1px solid #f1f5f9'><td style='padding:0.6rem 0.5rem'><code>{fmt}</code></td><td style='padding:0.6rem 0.5rem;color:#475569'>{desc}</td><td style='padding:0.6rem 0.5rem;color:#059669;font-weight:600'>{support}</td></tr>"

    st.markdown(
        f"""
        <table style="width:100%;border-collapse:collapse;font-size:0.875rem">
          <thead>
            <tr style="border-bottom:2px solid #e2e8f0;background:#f8f9fc">
              <th style="text-align:left;padding:0.7rem 0.5rem;color:#0f172a;font-weight:700">Format</th>
              <th style="text-align:left;padding:0.7rem 0.5rem;color:#0f172a;font-weight:700">Notes</th>
              <th style="text-align:left;padding:0.7rem 0.5rem;color:#0f172a;font-weight:700">Support</th>
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
                f'<div class="df-card" style="text-align:center;padding:1rem">'
                f'<div style="font-size:1.4rem">{icon}</div>'
                f'<div style="color:#2563eb;font-weight:700;margin:0.5rem 0 0.25rem;font-size:0.85rem">{title}</div>'
                f'<div style="color:#64748b;font-size:0.78rem;line-height:1.5">{desc}</div></div>',
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
