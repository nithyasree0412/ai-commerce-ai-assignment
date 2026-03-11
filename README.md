🌱 AI Commerce Backend System

An AI-powered backend system for sustainable e-commerce automation that intelligently classifies products and generates eco-friendly B2B product proposals using Large Language Models.

This system demonstrates how AI can enhance product discovery, sustainability tagging, and automated business proposals for modern commerce platforms.

🚀 Project Overview

This backend service provides two intelligent AI modules:
## 🎥 Demo Video

A short demo showing the working of the **AI Commerce Backend System**.

🔗 **Watch / Download Demo Video**  
[https://drive.google.com/your-video-link](https://drive.google.com/file/d/1jMGafb1ZuG0cZ4brodthdPn7H44q-oM6/view?usp=sharing)

⚠️ Note:  
If the preview shows **"This video file is still being processed for playback"**,  
please use the **Download option in Google Drive** to download and watch the video locally.

### Demo Highlights

- Product classification using AI
- Automatic category and SEO tag generation
- Sustainable product proposal generation
- Budget allocation logic
- AI retry mechanism for response reliability

🧠 Module 1 — AI Product Classification

Automatically analyzes product information and generates:

Product Category

Subcategory

SEO Tags for search optimization

Sustainability Filters

This helps e-commerce platforms improve product discoverability and sustainability indexing.

📊 Module 2 — AI Sustainable Proposal Generator

Generates eco-friendly product bundles for corporate or B2B events based on:

Event type

Budget

Sustainability priority

Outputs include:

Product mix

Budget allocation

Estimated total cost

Sustainability impact summary

This enables automated sustainable procurement recommendations.

🏗 System Architecture
```
Client Request
⬇
FastAPI Backend
⬇
AI Processing Layer
⬇
Groq LLM (Llama 3.3 70B)
⬇
Structured JSON Response
⬇
Stored in Database
``` 
🛠 Tech Stack
Technology	Purpose
Python	    Core backend language
FastAPI	    High-performance API framework
Groq LLM	  AI inference engine
MongoDB	    Data storage
Pydantic   	Request validation
Logging	    Debugging and monitoring
Dotenv	    Secure environment configuration
📂 Project Structure
```
ai-commerce-ai-assignment
│
├── app
│   ├── main.py
│   ├── ai_service.py
│   ├── database.py
│   ├── models.py
│   └── schemas.py
│
├── requirements.txt
├── README.md
├── .gitignore
└── .env (not uploaded for security)
```
🧠 AI Model Used

Model:
```

Llama-3.3-70B-Versatile
```
Provider:
```
Groq AI
```
The model is used for:

Product classification

Proposal generation

Sustainability reasoning

Structured JSON outputs

🔁 Retry Mechanism (AI Reliability)

AI systems may sometimes return invalid JSON responses.

To ensure robustness, the system implements a retry mechanism:

The AI request is attempted up to 2 times

If parsing fails, the system retries automatically

Prevents API crashes due to malformed responses

This improves production-level reliability.

📊 Example — Module 1

Input
``` json
{
 "name": "Organic Cotton T-Shirt",
 "description": "Soft breathable t-shirt made from organic cotton",
 "materials": "100% organic cotton"
} 
```
Output
``` json
{
 "category": "Apparel",
 "subcategory": "Tops",
 "seo_tags": [
  "organic cotton",
  "eco-friendly",
  "breathable",
  "sustainable fashion"
 ],
 "sustainability_filters": [
  "organic materials",
  "eco-friendly production"
 ]
}
```
📊 Example — Module 2
Input
``` json
{
 "budget": 5000,
 "event_type": "Corporate sustainability event",
 "priority": "plastic-free"
}
```
Output
``` json
{
 "product_mix": [
  {"name": "Reusable Bamboo Pens", "quantity": 200},
  {"name": "Recycled Paper Notebooks", "quantity": 100},
  {"name": "Stainless Steel Water Bottles", "quantity": 50}
 ],
 "budget_allocation": {
  "Reusable Bamboo Pens": 1200,
  "Recycled Paper Notebooks": 800,
  "Stainless Steel Water Bottles": 1500
 },
 "estimated_total_cost": 3500,
 "impact_summary": "Reduced plastic usage and promoted sustainable materials for corporate events."
}
```
⚙ Installation Guide
1️⃣ Clone the repository
```
git clone https://github.com/nithyasree0412/ai-commerce-ai-assignment.git
```
2️⃣ Install dependencies
```
pip install -r requirements.txt
```
3️⃣ Setup environment variables

Create .env file:
```
GROQ_API_KEY=your_api_key_here
```
4️⃣ Run the API
```
uvicorn app.main:app --reload
```
5️⃣ Open API documentation
```
http://127.0.0.1:8000/docs
```
FastAPI automatically provides an interactive Swagger UI.

🔍 Logging System

All AI interactions are logged in:
```
ai_logs.log
```
This includes:

AI prompts

Raw responses

Parsing errors

Retry attempts

Useful for debugging and AI monitoring.

🔒 Security Considerations

API keys stored using .env

Sensitive files excluded via .gitignore

Structured JSON validation prevents runtime errors

🌍 Real World Applications

This system can be integrated into:

E-commerce platforms

Sustainable product marketplaces

Corporate procurement systems

Green supply chain automation

✨ Future Improvements

Possible enhancements:

AI-powered product recommendations

Carbon footprint calculation

Multi-language product classification

Vector search with semantic embeddings

Sustainability scoring engine

👩‍💻 Author

Nithyasree

AI Commerce Backend Assignment
