import io
import streamlit as st
from utils.converter import convert, to_excel


def render():
    st.markdown("## ⚡ Convert Data")
    st.markdown('<p style="color:#64748b">Upload a file or paste raw data below. DataForge will auto-detect everything.</p>', unsafe_allow_html=True)

    tab_file, tab_text, tab_bulk = st.tabs(["📁 File Upload", "📝 Paste Text / Raw Data", "📦 Bulk Convert"])

    # ── Single file ────────────────────────────────────────────────────────
    with tab_file:
        uploaded = st.file_uploader(
            "Drop any file here",
            type=[
                "csv", "tsv", "json", "jsonl", "xml", "xlsx", "xls", "ods",
                "parquet", "feather", "html", "htm", "pdf", "txt", "log",
                "yaml", "yml", "sql", "pkl", "pickle", "avro", "h5", "hdf5",
            ],
            help="Supports 40+ formats. Max 200MB on Streamlit Cloud.",
        )

        col1, col2 = st.columns(2)
        with col1:
            include_summary = st.checkbox("Include Summary Sheet", value=True, help="Adds a sheet with column info, types, and stats")
        with col2:
            clean_data = st.checkbox("Auto-Clean Data", value=True, help="Removes duplicates, fixes types, normalises headers")

        if uploaded:
            _process_and_show(uploaded, None, include_summary, clean_data)

    # ── Text paste ─────────────────────────────────────────────────────────
    with tab_text:
        st.markdown("Paste CSV, JSON, XML, YAML, SQL, key=value, logs, or any text:")
        pasted = st.text_area("Paste here", height=300, placeholder='{"name":"Alice","age":30}\n{"name":"Bob","age":25}')
        col1, col2 = st.columns(2)
        with col1:
            include_summary2 = st.checkbox("Include Summary Sheet ", value=True, key="sum2")
        with col2:
            clean_data2 = st.checkbox("Auto-Clean Data ", value=True, key="clean2")

        if st.button("⚡ Convert Pasted Data", use_container_width=True):
            if pasted.strip():
                _process_and_show(None, pasted, include_summary2, clean_data2)
            else:
                st.warning("Paste some data first.")

    # ── Bulk ──────────────────────────────────────────────────────────────
    with tab_bulk:
        st.markdown("Upload multiple files — each becomes its own sheet (or a separate workbook).")
        files = st.file_uploader(
            "Drop multiple files",
            accept_multiple_files=True,
            key="bulk_uploader",
        )
        mode = st.radio("Output mode", ["One workbook, one sheet per file", "Separate workbook per file"], horizontal=True)
        include_summary3 = st.checkbox("Include Summary Sheet  ", value=True, key="sum3")

        if files:
            if st.button("⚡ Convert All Files", use_container_width=True):
                _process_bulk(files, mode, include_summary3)


# ── helpers ───────────────────────────────────────────────────────────────────

def _process_and_show(uploaded, text, include_summary, clean_data):
    with st.spinner("Detecting format and converting…"):
        result = convert(uploaded, text or "")

    if result["errors"]:
        for e in result["errors"]:
            st.markdown(f'<div class="error-box">❌ {e}</div>', unsafe_allow_html=True)
        return

    sheets = result["sheets"]
    if not sheets:
        st.warning("No data found in the file.")
        return

    # Detection badge
    src = result["source_type"]
    fname = result["file_name"]
    total_rows = sum(len(df) for df in sheets.values())
    total_cols = sum(len(df.columns) for df in sheets.values())

    st.markdown(
        f'<div class="success-box">✅ Detected: <b>{src}</b> · '
        f'{len(sheets)} sheet(s) · {total_rows:,} rows · {total_cols} columns</div>',
        unsafe_allow_html=True,
    )

    # Warnings
    for w in result.get("warnings", []):
        st.warning(w)

    # Store in session for preview page
    excel_bytes = to_excel(sheets, include_summary=include_summary)
    st.session_state["last_result"] = result
    st.session_state["last_excel"] = excel_bytes
    st.session_state["last_fname"] = fname

    # Quick inline preview
    st.markdown("#### Preview (first sheet)")
    first_df = next(iter(sheets.values()))
    st.dataframe(first_df.head(50), use_container_width=True)

    # Download
    safe_name = (fname.rsplit(".", 1)[0] if "." in fname else fname) or "dataforge_output"
    st.download_button(
        label="⬇️ Download Excel Workbook",
        data=excel_bytes,
        file_name=f"{safe_name}_converted.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        use_container_width=True,
    )


def _process_bulk(files, mode, include_summary):
    if "one workbook" in mode.lower():
        merged_sheets = {}
        all_results = []
        progress = st.progress(0)
        for i, f in enumerate(files):
            with st.spinner(f"Converting {f.name}…"):
                result = convert(f)
            all_results.append(result)
            for sheet_name, df in result["sheets"].items():
                key = f"{f.name[:15]}_{sheet_name}"[:31]
                merged_sheets[key] = df
            progress.progress((i + 1) / len(files))

        excel_bytes = to_excel(merged_sheets, include_summary=include_summary)
        st.success(f"✅ Merged {len(files)} files into {len(merged_sheets)} sheets.")
        st.download_button(
            "⬇️ Download Merged Workbook",
            data=excel_bytes,
            file_name="dataforge_bulk.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            use_container_width=True,
        )
    else:
        # Separate workbooks — offer as zip
        import zipfile, io as _io
        zip_buf = _io.BytesIO()
        progress = st.progress(0)
        with zipfile.ZipFile(zip_buf, "w", zipfile.ZIP_DEFLATED) as zf:
            for i, f in enumerate(files):
                with st.spinner(f"Converting {f.name}…"):
                    result = convert(f)
                excel_bytes = to_excel(result["sheets"], include_summary=include_summary)
                safe = f.name.rsplit(".", 1)[0] + "_converted.xlsx"
                zf.writestr(safe, excel_bytes)
                progress.progress((i + 1) / len(files))

        st.success(f"✅ Converted {len(files)} files.")
        st.download_button(
            "⬇️ Download All as ZIP",
            data=zip_buf.getvalue(),
            file_name="dataforge_bulk.zip",
            mime="application/zip",
            use_container_width=True,
        )
