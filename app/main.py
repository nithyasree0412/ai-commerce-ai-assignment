from fastapi import FastAPI
from bson import ObjectId
from app.models import ProductInput, ProposalInput
from app.ai_service import classify_product, generate_proposal
from app.database import products_collection, proposals_collection

app = FastAPI(title="AI Commerce API")


def validate_ai_output(output: dict):

    keys = ["category", "subcategory", "seo_tags", "sustainability_filters"]

    for key in keys:
        if key not in output:
            output[key] = [] if key.endswith("_tags") or key.endswith("_filters") else ""

    return output


@app.get("/")
def home():
    return {"message": "AI Commerce API running"}


# -------- MODULE 1 -------- #

@app.post("/classify-product")
def classify(product: ProductInput):

    try:

        result = classify_product(
            product.name,
            product.description,
            product.materials
        )

        result = validate_ai_output(result)

        product_data = {
            "name": product.name,
            "description": product.description,
            "materials": product.materials,
            "ai_result": result
        }

        inserted = products_collection.insert_one(product_data)

        product_data["_id"] = str(inserted.inserted_id)

        return product_data

    except Exception as e:

        return {"error": str(e)}


@app.get("/products")
def get_products():

    products = []

    for product in products_collection.find():
        product["_id"] = str(product["_id"])
        products.append(product)

    return products


@app.get("/products/{product_id}")
def get_product(product_id: str):

    try:

        product = products_collection.find_one(
            {"_id": ObjectId(product_id)}
        )

        if product:
            product["_id"] = str(product["_id"])
            return product

        return {"error": "Product not found"}

    except Exception as e:

        return {"error": str(e)}


# -------- MODULE 2 -------- #

@app.post("/generate-proposal")
def create_proposal(request: ProposalInput):

    try:

        result = generate_proposal(
            request.budget,
            request.event_type,
            request.priority
        )

        proposal_data = {
            "budget": request.budget,
            "event_type": request.event_type,
            "priority": request.priority,
            "ai_result": result
        }

        inserted = proposals_collection.insert_one(proposal_data)

        proposal_data["_id"] = str(inserted.inserted_id)

        return proposal_data

    except Exception as e:

        return {"error": str(e)}


@app.get("/proposals")
def get_proposals():

    proposals = []

    for proposal in proposals_collection.find():
        proposal["_id"] = str(proposal["_id"])
        proposals.append(proposal)

    return proposals