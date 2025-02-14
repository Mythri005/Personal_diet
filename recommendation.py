from flask import Blueprint, request, jsonify
from ml_model.diet_recommendation import recommend_diet

recommendation_bp = Blueprint("recommendation", __name__)

@recommendation_bp.route("/api/recommend", methods=["POST"])
def get_diet_recommendation():
    data = request.get_json()

    # ✅ Check if required fields (age & gender) are provided
    if "age" not in data or "gender" not in data:
        return jsonify({"error": "Missing required fields: age and gender are mandatory"}), 400

    # ✅ Optional fields: Fill only with provided values
    user_data = {
        "age": data["age"],
        "gender": data["gender"]
    }

    optional_fields = ["weight", "low_bp", "high_bp", "sugar", "diabetes", "heart_disease", "menstrual_health"]
    for field in optional_fields:
        if field in data:  # Only add if user provided
            user_data[field] = data[field]

    # ✅ Generate the personalized diet plan
    diet_plan = recommend_diet(user_data)

    # ✅ Ensure proper JSON formatting
    return jsonify({"recommended_30_day_diet": list(diet_plan.values())})  # Convert dict values to list
