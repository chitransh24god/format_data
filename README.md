# ⚡ DataForge — Universal Data → Excel Converter

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/Streamlit-1.35%2B-red?style=flat-square" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" />
  <img src="https://img.shields.io/badge/Formats-40%2B-purple?style=flat-square" />
</p>

> Turn **any raw data** into a clean, formatted Excel workbook — instantly, with zero configuration.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🧠 Smart Detection | Auto-detects file type, encoding, delimiter, and data shape |
| 🔄 40+ Formats | CSV, JSON, XML, PDF, Parquet, SQL, HTML, YAML, logs, and more |
| 🧹 Auto-Clean | Strips nulls, fixes types, normalises headers, deduplicates |
| 📊 Multi-sheet | Splits data into organised Excel sheets with a Summary tab |
| 📦 Bulk Convert | Upload multiple files → one merged workbook or separate ZIPs |
| 📝 Paste Mode | Paste raw text directly — JSON, CSV, logs, key=value, anything |
| ⚡ Fast & Local | All processing in-memory; your data never leaves the session |

---

## 🗂️ Supported Input Formats

```
CSV · TSV · JSON · JSONL · XML · XLSX · XLS · ODS
Parquet · Feather · HDF5 · Avro · Pickle
PDF · HTML · SQL Dump · YAML · YML
TXT · LOG · Key=Value · Pasted Text
```

---

## 🚀 Quick Start

### Local

```bash
git clone https://github.com/YOUR_USERNAME/dataforge.git
cd dataforge
pip install -r requirements.txt
streamlit run app.py
```

### Deploy to Streamlit Cloud (free)

1. Push this repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click **New app** → select your repo → set main file to `app.py`
4. Click **Deploy** — done!

---

## 📁 Project Structure

```
dataforge/
├── app.py                  # Entry point
├── requirements.txt        # Dependencies
├── .streamlit/
│   └── config.toml         # Theme + server config
├── assets/
│   └── style.css           # Global dark-mode styles
├── pages/
│   ├── __init__.py
│   ├── home.py             # Landing page
│   ├── converter.py        # Upload + convert UI
│   ├── preview.py          # Data preview + download
│   └── about.py            # Format table + tech stack
└── utils/
    ├── __init__.py
    └── converter.py        # Core detection + conversion engine
```

---

## 🧠 How It Works

```
Upload / Paste
     │
     ▼
Extension + Content Sniffing
     │
     ▼
Smart Parser Selected  ←── JSON / XML / YAML / CSV / PDF / SQL / Parquet / …
     │
     ▼
Auto-Clean  ←── drop nulls · fix types · normalise headers · deduplicate
     │
     ▼
Excel Workbook  ←── formatted sheets + Summary tab
     │
     ▼
Download ⬇️
```

---

## 🛠️ Tech Stack

- **Streamlit** — web UI
- **Pandas / NumPy** — data processing
- **openpyxl** — Excel generation with formatting
- **pdfplumber** — PDF table extraction
- **chardet** — encoding detection
- **PyYAML** — YAML parsing
- **fastavro** — Avro parsing
- **pyarrow** — Parquet / Feather

---

## 🤝 Contributing

PRs welcome! Ideas for new formats, better parsing, or UI improvements are all great.

1. Fork the repo
2. Create a feature branch: `git checkout -b feat/my-format`
3. Commit: `git commit -m "Add support for XYZ"`
4. Push and open a PR

---

## 📄 License

MIT — free to use, modify, and distribute.
