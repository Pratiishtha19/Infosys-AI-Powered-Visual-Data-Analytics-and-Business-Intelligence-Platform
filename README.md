# 🦺 AI-Powered Visual Data Analytics and Business Intelligence Platform

An AI-powered platform that combines **computer vision, data analytics, and business intelligence** to transform visual and structured data into meaningful insights.

This project was developed as part of the **Infosys Springboard Internship**, covering multiple milestones that progressively build the platform from AI-based image analysis to data-driven business insights.

---

## 🚀 Project Overview

The **AI-Powered Visual Data Analytics and Business Intelligence Platform** is designed to help users analyze images, extract useful information, and visualize data through an interactive interface.

The project integrates:

* 🤖 **Artificial Intelligence**
* 👁️ **Computer Vision**
* 📊 **Data Analytics**
* 📈 **Business Intelligence**
* 📄 **Document Intelligence**
* 🔍 **Retrieval-Augmented Generation (RAG)**
* 🗄️ **Database Management**
* 🌐 **Interactive Web Interface**

The platform demonstrates how AI can be combined with analytics and visualization to support faster and more informed decision-making.

---

## 🎯 Objectives

* Detect and analyze objects in images using AI.
* Identify safety equipment such as PPE in construction environments.
* Extract useful information from documents.
* Enable users to ask questions about uploaded documents.
* Store and manage application data using a database.
* Provide visual analytics and business insights.
* Build an integrated AI-powered platform using multiple technologies.

---

## 🧩 Project Milestones

### 🔹 Milestone 1 — AI Visual Analytics

The first milestone focuses on **object detection using YOLOv8**.

The application allows users to upload an image and detects objects present in the image using a pretrained YOLO model.

**Key Features:**

* Image upload
* YOLOv8 object detection
* Detected object identification
* Confidence score display
* Visualized detection results

**Technologies:**

* Python
* YOLOv8
* Ultralytics
* OpenCV
* Streamlit
* Pillow

---

### 🔹 Milestone 2 — PPE Detection

The second milestone extends computer vision toward **construction-site safety**.

The model detects Personal Protective Equipment (PPE) from construction worker images.

**Key Features:**

* Upload construction worker images
* Detect PPE equipment
* Display detected classes
* Show confidence scores
* Visualize detection results

**Technologies:**

* Python
* YOLOv8
* Ultralytics
* Streamlit
* Pillow
* NumPy

---

### 🔹 Milestone 3 — Document Intelligence & RAG

The third milestone introduces **document processing and Retrieval-Augmented Generation (RAG)**.

Users can process documents and retrieve relevant information from them using vector embeddings and similarity search.

**Workflow:**

```text
Document
   ↓
Document Loading
   ↓
Text Extraction
   ↓
Text Chunking
   ↓
Embeddings
   ↓
Vector Database
   ↓
Similarity Search
   ↓
Relevant Context
   ↓
LLM
   ↓
Generated Answer
```

**Key Technologies:**

* Python
* PyMuPDF
* LangChain
* FAISS
* Hugging Face
* Embeddings
* Large Language Models

---

### 🔹 Milestone 4 — Data Analytics & Business Intelligence

The final milestone focuses on converting data into meaningful **visual insights and business intelligence**.

The platform can be extended with interactive dashboards and analytical visualizations to help users understand patterns and trends in their data.

**Tools & Technologies:**

* R
* Power BI
* Tableau
* Python
* Data Visualization
* Data Analytics

---

## 🏗️ Overall System Architecture

```text
                    ┌──────────────────────┐
                    │        User          │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Streamlit UI       │
                    └──────────┬───────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
       Image Analysis     PPE Detection    Document Analysis
              │                │                │
              ▼                ▼                ▼
           YOLOv8           YOLOv8          PyMuPDF
                                                │
                                                ▼
                                           Text Chunking
                                                │
                                                ▼
                                           Embeddings
                                                │
                                                ▼
                                             FAISS
                                                │
                                                ▼
                                               LLM
                                                │
                                                ▼
                                          AI Response
                              
                               ┌─────────────────┐
                               │ Data Analytics   │
                               │ & BI Dashboard   │
                               └────────┬────────┘
                                        │
                                        ▼
                               Business Insights
```

---

## 🛠️ Technology Stack

| Category            | Technologies                 |
| ------------------- | ---------------------------- |
| Programming         | Python                       |
| Computer Vision     | YOLOv8, OpenCV               |
| AI/ML               | YOLO, Hugging Face, LLMs     |
| RAG                 | LangChain, FAISS, Embeddings |
| Document Processing | PyMuPDF                      |
| Web Interface       | Streamlit                    |
| Data Analytics      | Python, R                    |
| Visualization       | Power BI, Tableau            |
| Database            | MySQL                        |
| Version Control     | Git & GitHub                 |

---

## 📁 Project Structure

```text
AI-Powered-Visual-Data-Analytics-and-Business-Intelligence-Platform/
│
├── milestone1/
│   ├── milestone1.py
│   └── README.md
│
├── milestone2/
│   ├── app.py
│   ├── best.pt
│   └── README.md
│
├── milestone3/
│   ├── milestone3_practice.py
│   ├── data/
│   │   └── safety_manual.pdf
│   └── README.md
│
├── milestone4/
│   ├── analytics/
│   ├── dashboards/
│   └── README.md
│
├── requirements.txt
├── .gitignore
└── README.md
```

> The folder structure can be adjusted according to the actual files in the repository.

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Pratiishtha19/Infosys-AI-Powered-Visual-Data-Analytics-and-Business-Intelligence-Platform.git
```

### 2. Navigate to the Project

```bash
cd Infosys-AI-Powered-Visual-Data-Analytics-and-Business-Intelligence-Platform
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
.venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

For Streamlit-based milestones:

```bash
python -m streamlit run app.py
```

If a milestone has a different Python file:

```bash
python milestone1.py
```

or

```bash
python milestone3_practice.py
```

---

## 🔐 Environment Variables

Some AI features may require API credentials.

Create a `.env` file in the project directory:

```env
OPENAI_API_KEY=your_api_key_here
```

**Important:** Never upload API keys, passwords, or other sensitive credentials to GitHub.

Add `.env` to `.gitignore`:

```text
.env
.venv/
__pycache__/
*.pyc
```

---

## 📊 Key Features

### 👁️ AI-Based Image Analysis

Upload images and use YOLOv8 to identify objects automatically.

### 🦺 PPE Detection

Analyze construction-site images and detect safety equipment using a custom YOLO model.

### 📄 Document Intelligence

Process PDF documents and extract useful information from them.

### 🔍 RAG-Based Question Answering

Retrieve relevant information from documents and provide AI-generated responses.

### 📈 Data Visualization

Transform datasets into charts, dashboards, and meaningful business insights.

### 🗄️ Database Integration

Store and manage relevant application information using a database.

### 🌐 Interactive Interface

Streamlit provides an easy-to-use interface for interacting with the AI and analytics components.

---

## 🔄 RAG Workflow

The document-question-answering component follows this process:

```text
Upload Document
       ↓
Extract Text
       ↓
Split Text into Chunks
       ↓
Generate Embeddings
       ↓
Store Embeddings in FAISS
       ↓
User Question
       ↓
Convert Question into Embedding
       ↓
Similarity Search
       ↓
Retrieve Relevant Chunks
       ↓
Send Context + Question to LLM
       ↓
Generate Answer
```

This allows the system to retrieve relevant information from the uploaded documents before generating a response.

---

## 📌 Applications

This platform can be useful in areas such as:

* 🏗️ Construction safety monitoring
* 👷 PPE compliance monitoring
* 📄 Document analysis
* 📊 Business analytics
* 🔎 Knowledge retrieval
* 🤖 AI-assisted decision support
* 📈 Data-driven reporting

---

## 🔮 Future Enhancements

* Real-time CCTV-based PPE monitoring
* Support for additional document formats
* Advanced AI-powered analytics
* Automated business reports
* Cloud deployment
* Role-based user authentication
* Real-time dashboards
* More advanced RAG capabilities
* Integration with additional databases
* Mobile-friendly interface

---

**Computer Vision → PPE Detection → Document Intelligence & RAG → Data Analytics & Business Intelligence**

---

## 👩‍💻 Author

**Pratishtha Gadwanshi**

## ⭐ Acknowledgements

* Ultralytics YOLO
* LangChain
* FAISS
* Hugging Face
* Streamlit
* Python Community
