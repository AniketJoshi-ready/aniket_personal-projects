# aniket_personal-projects
# 🏠 Airbnb NYC 2019: Price Prediction and Insights

This project performs exploratory data analysis (EDA), data cleaning, feature engineering, and regression modeling to predict Airbnb listing prices in New York City using the **Airbnb NYC 2019 dataset**.

---

## 📌 Project Objectives

- Analyze NYC Airbnb listings to understand pricing trends.
- Clean and preprocess the data for analysis.
- Perform exploratory data analysis with visualizations.
- Build regression models (Linear Regression & XGBoost) to predict listing prices.
- Provide actionable insights and pricing recommendations for hosts.

---

## 📂 Dataset

**Source**: [Inside Airbnb – NYC 2019] https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data

**File**: `AB_NYC_2019.csv`

**Key Columns**:
- `neighbourhood_group`: Borough of the listing
- `neighbourhood`: District/area within the borough
- `room_type`: Entire home, private room, shared room
- `price`: Price per night
- `minimum_nights`, `availability_365`, `number_of_reviews`, `reviews_per_month`, etc.

---

## 🧹 Data Preprocessing

- Converted `last_review` to datetime
- Filled missing values in `reviews_per_month` with 0
- Dropped listings with missing `name` or `host_name`
- Removed extreme outliers: `price > 1000` and `minimum_nights > 365`
- Created new features:
  - `has_reviews`: Binary indicator if listing has any reviews
  - `active_days_ratio`: Availability normalized over 365 days

---

## 📊 Exploratory Data Analysis (EDA)

Using `matplotlib` and `seaborn`:

- 📌 **Room Type Distribution**
- 📌 **Price Distribution by Neighbourhood Group (Log Scale)**
- 📌 **Listing Location Scatter Plot (5000 sample)**
- 📌 **Boxplot: Price vs Room Type (<$500)**
- 📌 **Heatmap: Correlation of Numerical Features**

---

## 🤖 Regression Modeling

### 1. **Linear Regression**
- **RMSE**: `96.99`
- **R² Score**: `0.303`

### 2. **XGBoost Regressor**
- **RMSE**: `92.40`
- **R² Score**: `0.368`

✅ **XGBoost performed better**, capturing more variance and delivering lower prediction error.

---

## 💡 Key Insights

- **Manhattan** has the highest-priced listings, followed by Brooklyn.
- **Entire homes/apartments** command significantly higher prices.
- Most listings are concentrated in Manhattan and Brooklyn.
- Listings with more availability and reviews tend to earn more.
- Pricing outliers were rare but impactful — removal improved model stability.

---

## 💰 Pricing Recommendations

- Prioritize full-home listings in Manhattan or Brooklyn.
- Use dynamic pricing to adjust for location, seasonality, and demand.
- Avoid overpricing (>$1000) unless offering premium features.
- Encourage reviews to boost listing credibility.
- Maintain high availability throughout the year to maximize booking opportunities.

---

##  Tech Stack

- **Language**: Python 3
- **Libraries**: `pandas`, `numpy`, `matplotlib`, `seaborn`, `xgboost`, `scikit-learn`
- **IDE**: Jupyter Notebook / VS Code

---

##  Getting Started

### Install Dependencies
```bash
pip install pandas matplotlib seaborn xgboost scikit-learn
