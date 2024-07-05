from flask import Flask, request, jsonify
import pandas as pd
import pickle

app = Flask(__name__)

file_path = 'customer_purchase_data.csv'
customer_data = pd.read_csv(file_path)

# Load the trained RFC model from pickle file
with open('rf_model.pkl', 'rb') as f:
    model = pickle.load(f)

class CustomerRecommendation:
    def __init__(self, data):
        self.data = data  # Assuming data is your DataFrame containing customer data

    def recommend_products(self, return_likelihood, repeat_purchase_likelihood):
        # Recommendation logic based on likelihoods
        # Example logic: recommend products for customers with high likelihoods
        if return_likelihood > 0.5:
            recommended_products = self.data[self.data['ReturnLikelihood'] > 0.5]['ProductCategory'].tolist()
        else:
            recommended_products = []

        return recommended_products

# Initialize CustomerRecommendation with customer_data
customer_rec = CustomerRecommendation(customer_data)

# Define Flask API endpoint for predicting likelihoods
@app.route('/predict_likelihood', methods=['POST'])
def predict_likelihood():
    # Parse JSON request data
    customer_features = request.get_json()
    
    # Extract features for prediction
    features = [
        customer_features['Age'],
        customer_features['Gender'],
        customer_features['AnnualIncome'],
        customer_features['NumberOfPurchases'],
        customer_features['ProductCategory'],
        customer_features['TimeSpentOnWebsite'],
        customer_features['LoyaltyProgram'],  # Include LoyaltyProgram here
        customer_features['DiscountsAvailed'],
    ]
    
    # Predict likelihoods using the RFC model
    likelihoods = model.predict_proba([features])
    return_likelihood = likelihoods[0][0]
    repeat_purchase_likelihood = likelihoods[0][1]

    # Return JSON response with predicted likelihoods
    return jsonify({
        'ReturnLikelihood': return_likelihood,
        'RepeatPurchaseLikelihood': repeat_purchase_likelihood
    })

# Define Flask API endpoint for recommending products
@app.route('/recommend_products', methods=['POST'])
def recommend_products():
    # Parse JSON request data
    customer_features = request.get_json()
    
    # Extract features for recommendation
    return_likelihood = customer_features['ReturnLikelihood']
    repeat_purchase_likelihood = customer_features['RepeatPurchaseLikelihood']
    
    # Get recommended products based on likelihoods
    recommended_products = customer_rec.recommend_products(return_likelihood, repeat_purchase_likelihood)
    
    # Return JSON response with recommended products
    return jsonify({
        'RecommendedProducts': recommended_products
    })

if __name__ == '__main__':
    app.run(debug=True)
