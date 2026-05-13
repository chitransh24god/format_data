import streamlit as st
import pandas as pd


def render():
    st.markdown("## 👁️ Preview & Download")

    if "last_result" not in st.session_state:
        st.info("Nothing converted yet. Go to **⚡ Convert** to upload a file first.")
        return

    result = st.session_state["last_result"]
    excel_bytes = st.session_state["last_excel"]
    fname = st.session_state.get("last_fname", "output")
    sheets = result["sheets"]

    # Header info
    src = result["source_type"]
    total_rows = sum(len(df) for df in sheets.values())
    st.markdown(
        f'<div class="df-card"><b style="color:#00e5ff">{fname}</b> · '
        f'<span class="df-badge badge-info">{src}</span> · '
        f'{len(sheets)} sheet(s) · {total_rows:,} total rows</div>',
        unsafe_allow_html=True,
    )

    # Sheet selector
    sheet_name = st.selectbox("Select sheet to preview", list(sheets.keys()))
    df = sheets[sheet_name]

    # Stats row
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f'<div class="df-stat"><div class="df-stat-num">{len(df):,}</div><div class="df-stat-label">Rows</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="df-stat"><div class="df-stat-num">{len(df.columns)}</div><div class="df-stat-label">Columns</div></div>', unsafe_allow_html=True)
    with col3:
        nulls = df.isna().sum().sum()
        st.markdown(f'<div class="df-stat"><div class="df-stat-num">{nulls:,}</div><div class="df-stat-label">Null Cells</div></div>', unsafe_allow_html=True)
    with col4:
        dupes = df.duplicated().sum()
        st.markdown(f'<div class="df-stat"><div class="df-stat-num">{dupes:,}</div><div class="df-stat-label">Duplicates</div></div>', unsafe_allow_html=True)

    st.markdown("")

    # Column type badges
    st.markdown("**Column types:**")
    badges = ""
    for col in df.columns:
        dtype = str(df[col].dtype)
        cls = "badge-success" if "int" in dtype or "float" in dtype else \
              "badge-info" if "datetime" in dtype else \
              "badge-purple" if "bool" in dtype else "badge-warning"
        badges += f'<span class="df-badge {cls}">{col}: {dtype}</span> '
    st.markdown(badges, unsafe_allow_html=True)

    st.markdown("---")

    # Filters
    with st.expander("🔍 Filter & Search", expanded=False):
        search = st.text_input("Search all columns (contains):")
        if search:
            mask = df.apply(lambda col: col.astype(str).str.contains(search, case=False, na=False))
            df = df[mask.any(axis=1)]
            st.caption(f"{len(df):,} matching rows")

        col_filter = st.multiselect("Show only columns:", df.columns.tolist(), default=df.columns.tolist())
        if col_filter:
            df = df[col_filter]

        max_rows = st.slider("Rows to preview", 10, min(1000, len(df)), min(100, len(df)))
        df = df.head(max_rows)

    # Data table
    st.dataframe(df, use_container_width=True, height=450)

    st.markdown("---")

    # Describe
    with st.expander("📊 Statistical Summary", expanded=False):
        try:
            st.dataframe(sheets[sheet_name].describe(include="all").T, use_container_width=True)
        except Exception as e:
            st.warning(f"Could not compute stats: {e}")

    # Download
    safe_name = fname.rsplit(".", 1)[0] if "." in fname else fname
    st.download_button(
        label="⬇️ Download Excel Workbook",
        data=excel_bytes,
        file_name=f"{safe_name}_converted.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        use_container_width=True,
    )
