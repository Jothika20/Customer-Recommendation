Here's a basic README file template you can use to explain how to run your Flask API application:

---

# Customer Recommendation API

This project implements a Flask API to predict customer return likelihood, repeat purchase likelihood, and recommend products based on trained machine learning models.

## Prerequisites

- Python 3.x installed
- Python packages listed in `requirements.txt` installed (`pip install -r requirements.txt`)

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your/repository.git
   cd Customer_API
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask API:
   ```bash
   python api.py
   ```

## Usage

### 1. Predict Likelihoods Endpoint

Endpoint URL: `http://127.0.0.1:5000/predict_likelihood`

**Request:**
```bash
curl -X POST -H "Content-Type: application/json" -d "{\"Age\": 30, \"Gender\": 1, \"AnnualIncome\": 50000, \"NumberOfPurchases\": 10, \"ProductCategory\": 1, \"TimeSpentOnWebsite\": 50, \"LoyaltyProgram\": true, \"DiscountsAvailed\": 1}" http://127.0.0.1:5000/predict_likelihood
```

**Response Example:**
```json
{
  "ReturnLikelihood": 0.08,
  "RepeatPurchaseLikelihood": 0.92
}
```

### 2. Recommend Products Endpoint

Endpoint URL: `http://127.0.0.1:5000/recommend_products`

**Request:**
```bash
curl -X POST -H "Content-Type: application/json" -d "{\"ReturnLikelihood\": 0.08, \"RepeatPurchaseLikelihood\": 0.92}" http://127.0.0.1:5000/recommend_products
```

**Response Example:**
```json
{
  "RecommendedProducts": []
}
```

## Notes

- Ensure that all required input features are provided in the JSON request.
- Adjust the recommendation logic in `recommend_products` method of `CustomerRecommendation` class as needed based on data availability and business requirements.

---
