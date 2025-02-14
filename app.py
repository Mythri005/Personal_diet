from flask import Flask, request, jsonify
from flask_cors import CORS
from routes.recommendation import recommendation_bp  # Import the blueprint

app = Flask(__name__)
CORS(app)  # Enable CORS to allow browser access

# ✅ Register the blueprint here
app.register_blueprint(recommendation_bp)  

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Personalized Diet Recommendation API!", "usage": "Send a POST request to /api/recommend with user details."})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
