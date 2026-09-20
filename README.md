# 🏛️ CivicPulse AI — Autonomous Legislative Impact & Provenance Sandbox

[![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![Google Gemini](https://img.shields.io/badge/Google%20Gemini-1.5%20Flash-8E75B2?style=for-the-badge&logo=googlecloud&logoColor=white)](https://ai.google.dev/)
[![LangChain](https://img.shields.io/badge/LangChain-0.1+-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)](https://www.langchain.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

**CivicPulse AI** is an autonomous legislative decision-support system and cryptographically auditable policy sandbox. Designed for parliamentary bodies, civil service analysts, and public policy researchers, CivicPulse AI simulates the economic, regional, and societal impacts of draft statutory clauses *before* they are enacted into law.

---

## 🎯 The Problem & The Solution## **The Problem**
Sluggish Policy Evaluation: Traditional parliamentary impact assessments rely on manual consultations and static reports that take months to complete.
* **Unintended Regional Disparities:** Uniform national policies frequently cause unexpected economic burdens in specific regions or high-growth sectors.
* **Opaque Audit Trails:** Legislative revisions and simulation models lack immutable provenance, creating risk around policy tampering or selective reporting.

### **The Solution**
CivicPulse AI unifies real-time multi-agent LLM deliberations, geospatial heatmaps, civic NLP feedback pipelines, and Web3 state hashing into a single interactive command center.

---

## 🌟 Key Features

* **🤖 Autonomous Multi-Agent War Room:** Evaluates legislative text simultaneously across specialized stakeholder personas (*SME Representative, Macro Economist, Local Council Leader, Green Transition Officer*) using **Google Gemini 1.5 Flash** and **LangChain**.
* **🗺️ Geospatial Impact Mapping:** Renders dynamic 3D UK spatial heatmaps powered by **PyDeck**, visualising regional feasibility gains and regulatory burdens across major hubs (London, Manchester, Newcastle, Edinburgh, Belfast, etc.).
* **🔗 Web3 Cryptographic Provenance:** Calculates a deterministic SHA-256 state hash and Merkle root for every bill version and simulation score, anchoring the policy state on-chain with mobile-scannable QR URI payloads.
* **📊 Public Sentiment Clustering:** Categorizes citizen petitions, select committee submissions, and public feedback into focus clusters using NLP sentiment analysis.
* **📄 Publication-Ready Executive PDF Briefs:** Autonomously compiles executive summary briefs complete with cryptographic state proofs and stakeholder breakdowns using **ReportLab**.

---

## 🏗️ System Architecture

                  +----------------------------------+
                  |   Draft Statutory Clause Input   |
                  +----------------------------------+
                                   |
                                   v
                 +------------------------------------+
                 |  Multi-Agent Simulation Engine     |
                 |  (Gemini 1.5 Flash + LangChain)    |
                 +------------------------------------+
                    /              |               \
                   /               |                \
                  v                v                 v
        +------------------+ +-------------+ +---------------+
        | Regional Feasib. | | Agent Logs  | | Sentiment NLP |
        | Index (PyDeck)   | | Breakdown   | | Clustering    |
        +------------------+ +-------------+ +---------------+
                    \              |                /
                     \             |               /
                      v            v              v
                 +------------------------------------+
                 |    SHA-256 Ledger State Anchor     |
                 |    & Merkle Root Generation        |
                 +------------------------------------+
                                   |
                 +------------------------------------+
                 |   Streamlit Command Center UI      |
                 |   + ReportLab PDF & QR Proofs      |
                 +------------------------------------+

---

## 🛠️ Tech Stack

| Domain | Technologies |
| :--- | :--- |
| **Frontend UI** | Streamlit, HTML5/CSS3 (Custom Parliamentary Theme) |
| **Orchestration & LLM** | LangChain Core, Google Gemini API (`gemini-1.5-flash`) |
| **Geospatial & Analytics** | PyDeck, Plotly Express, Pandas |
| **Cryptography & Verification** | Python `hashlib`, `qrcode`, Data URI Protocols |
| **Document Generation** | ReportLab PDF Toolkit |

---

## ⚡ Quick Start Guide

### **Prerequisites**
* Python 3.10 or higher
* Google Gemini API Key ([Get an API Key here](https://aistudio.google.com/))

### **1. Clone the Repository**
```bash
git clone [https://github.com/your-username/civicpulse-ai.git](https://github.com/your-username/civicpulse-ai.git)
cd civicpulse-ai
2. Set Up Virtual Environment
Bash
# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
3. Install Dependencies
Bash
pip install -r requirements.txt
4. Environment Configuration
Create a .env file in the project root folder:

Code snippet
GOOGLE_API_KEY="your_actual_gemini_api_key_here"
5. Launch Application
Bash
streamlit run app.py
Navigating to http://localhost:8501 will open the application in your browser.

📁 Project Structure
Plaintext
civicpulse-ai/
├── app.py                 # Main Streamlit command application & core engines
├── requirements.txt       # Project dependencies
├── .env.example           # Environment template file
├── README.md              # Project documentation
└── assets/                # Screenshots and documentation media
📜 Example requirements.txt
Plaintext
streamlit>=1.30.0
langchain-google-genai>=0.0.6
langchain-core>=0.1.0
pandas>=2.0.0
pydeck>=0.8.0
plotly>=5.18.0
reportlab>=4.0.0
qrcode>=7.4.2
python-dotenv>=1.0.0
🤝 Contributing
Contributions are welcome! Please feel free to open an Issue or submit a Pull Request:

Fork the Project

Create your Feature Branch (git checkout -b feature/PolicyAgent)

Commit your Changes (git commit -m 'Add new agent persona')

Push to the Branch (git push origin feature/PolicyAgent)

Open a Pull Request

📄 License
Distributed under the MIT License. See LICENSE for more information
