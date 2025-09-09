
**Curia AI**

Curia AI is an **AI-powered meeting summarizer** with **Jira integration**. It helps teams automatically convert meeting transcripts into **actionable tasks**, reducing manual effort and improving productivity.

This is the **beta version**, powered by **LLaMA 3.1**, which processes transcripts into action items.

🔗 **Website:** [curia-ai.netlify.app](https://curia-ai.netlify.app)  

⚠️ **Note:** Backend hosting is pending as AI model training is ongoing.

---

## 📂 Project Structure
```

Curia-AI/
│── backend/          # Flask backend (Jira integration + AI summarizer)
│── backend-node/     # Express.js backend (API layer for frontend)
│── frontend/         # React frontend (UI)
│── samples/          # Example transcripts and outputs
│── texttoaudio/      # Text-to-speech experimentation
│── .gitattributes
│── .DS\_Store

````

---

## 🚀 Features
- 📝 **Meeting Summaries** – Concise summaries from transcripts.  
- ✅ **Action Items Extraction** – Converts discussions into structured tasks.  
- 🔗 **Jira Integration** – Push action items directly into Jira.  
- 🎙️ **Speech Experiments** – Text-to-audio utilities for voice-enabled workflows.  
- ⚡ **LLaMA 3.1** – Used for transcript-to-action conversion.  

---

## 🛠️ Tech Stack
- **Frontend:** React.js  
- **Backend (AI + Jira):** Flask (Python)  
- **Backend (API):** Express.js  
- **AI Model:** LLaMA 3.1 (fine-tuned)  
- **Integration:** Jira REST API  

---

## 📦 Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/curia-ai.git
cd curia-ai
````

### 2. Flask Backend (AI + Jira)

```bash
cd backend
pip install -r requirements.txt
python app.py
```

### 3. Express Backend (API Layer)

```bash
cd backend-node
npm install
npm run dev
```

### 4. React Frontend

```bash
cd frontend
npm install
npm start
```

---

## 🧪 Current Status (Beta)

* ✅ Frontend React app running with mock API.
* ⚙️ Express backend connected for API requests.
* 🔄 Flask backend (AI + Jira) in training & testing phase.
* 🚀 Jira integration functional in test mode.

---
