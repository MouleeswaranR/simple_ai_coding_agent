# 🚀 Simple Coding Agent

A simple AI-powered coding agent built using **Google Gemini API**.  
This agent can analyze code, answer repository questions, write files, and fix bugs using natural language prompts.

---

## 📦 Project Info

- **Name:** coding-agent  
- **Version:** 0.1.0  
- **Python Version:** `>=3.13`  
- **Dependencies:**
  - `google-genai==1.12.1`
  - `python-dotenv==1.1.0`

---

## 🛠 Installation Guide

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-url>
cd coding-agent
```

---

### 2️⃣ Install `uv` (if not installed)

```bash
pip install uv
```

---

### 3️⃣ Install Dependencies

Using `uv` (recommended):

```bash
uv sync
```

Or manually using pip:

```bash
pip install google-genai==1.12.1 python-dotenv==1.1.0
```

---

## 🔐 Environment Setup

Create a `.env` file in the **root folder** of the project.

### 📄 `.env`

```
GEMINI_API_KEY=your_key_here
```

Replace `your_key_here` with your actual Gemini API key.

---

## ▶️ How to Run

Use `uv run` to execute the agent.

Example:

```bash
uv run main.py "your question here"
```

---

## 🧪 Example Commands to Try

```bash
uv run main.py "what is in the tests.py?"
```

```bash
uv run main.py "write hello world to a new greeting.txt file?"
```

```bash
uv run main.py "how does the calculator render results to the console, you are in the calulator directory for your function calls"
```

```bash
uv run main.py "fix the bug: 3 + 7 * 2 should not be 20"
```

---

## 📁 Project Structure (Example)

```
coding-agent/
│── main.py
│── tests.py
│── functions
│── calculator/
│── README.md
│── .env
│── pyproject.toml
```

---

## 💡 What This Agent Can Do

- 🔍 Read and explain files in your project  
- ✍️ Create or modify files  
- 🐞 Detect and fix logical bugs  
- 🧮 Debug calculation errors  
- 📂 Work context-aware within directories  

---

## ⚠️ Notes

- This project is for **educational purposes only**.  
- Do not expose your API key publicly.  
- Make sure your `.env` file is **not committed** to GitHub.  
- Add `.env` to your `.gitignore`.  
- Requires Python `3.13+`.

---
```
