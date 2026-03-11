import os
import json
import logging
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

logging.basicConfig(
    filename="ai_logs.log",
    level=logging.INFO,
    format="%(asctime)s %(message)s"
)

CATEGORIES = [
    "Apparel", "Electronics", "Home", "Beauty",
    "Accessories", "Footwear", "Food", "Personal Care"
]


# ---------------- MODULE 1 ---------------- #

def classify_product(name, description, materials):

    prompt = f"""
You are an AI product classifier.

Choose category ONLY from this list:
{CATEGORIES}

Return JSON with:
category
subcategory
seo_tags (5-10)
sustainability_filters

Product:
Name: {name}
Description: {description}
Materials: {materials}

Return ONLY JSON:

{{
 "category": "",
 "subcategory": "",
 "seo_tags": [],
 "sustainability_filters": []
}}
"""

    logging.info(f"PROMPT CLASSIFY: {prompt}")

    for attempt in range(2):  # retry mechanism

        try:

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}]
            )

            ai_text = response.choices[0].message.content

            logging.info(f"AI RESPONSE CLASSIFY RAW: {ai_text}")

            # remove markdown formatting
            ai_text = ai_text.replace("```json", "").replace("```", "").strip()

            return json.loads(ai_text)

        except Exception as e:

            logging.error(f"AI PARSE ERROR CLASSIFY (attempt {attempt+1}): {e}")

    # fallback response if AI fails twice
    return {
        "category": "",
        "subcategory": "",
        "seo_tags": [],
        "sustainability_filters": []
    }


# ---------------- MODULE 2 ---------------- #

def generate_proposal(budget, event_type, priority):

    prompt = f"""
You are an AI assistant that creates sustainable B2B product proposals.

Client Event: {event_type}
Budget: {budget}
Priority: {priority}

Return ONLY JSON in this format:

{{
 "product_mix": [],
 "budget_allocation": {{}},
 "estimated_total_cost": 0,
 "impact_summary": ""
}}
"""

    logging.info(f"PROMPT PROPOSAL: {prompt}")

    for attempt in range(2):  # retry mechanism

        try:

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}]
            )

            ai_text = response.choices[0].message.content

            logging.info(f"AI RESPONSE PROPOSAL RAW: {ai_text}")

            # remove markdown formatting
            ai_text = ai_text.replace("```json", "").replace("```", "").strip()

            return json.loads(ai_text)

        except Exception as e:

            logging.error(f"AI PARSE ERROR PROPOSAL (attempt {attempt+1}): {e}")

    # fallback response if AI fails twice
    return {
        "product_mix": [],
        "budget_allocation": {},
        "estimated_total_cost": 0,
        "impact_summary": "AI response parsing failed after retry"
    }