# aniket_personal-projects

PROJECT 1


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
```

PROJECT 2


🧹 Automated Directory Duplicate File Cleaner with Logging and Email Alerts
This Python script automates the process of detecting and removing duplicate files from a specified directory. It periodically scans the directory, removes detected duplicate files, logs the deleted files in a log file, and sends the log file via email.

📁 Project Structure

marvellous/
├── marvellous.txt       # Log file generated automatically
cleaner_script.py        # Main Python script
🔧 Features
✅ Scans a given directory (recursively) to find duplicate files based on file checksum (MD5).

🧹 Automatically deletes duplicate files.

📝 Maintains a detailed log of all deleted files with timestamps.

📧 Sends the log file via email to the user or client.

🔁 Supports automation using custom time intervals (in minutes).

🚀 How to Use
🖥️ Command Line Usage
python cleaner_script.py <DirectoryPath> <TimeIntervalInMinutes>

🆘 Help and Usage Flags

python cleaner_script.py --h  # Display help message
python cleaner_script.py --u  # Display usage instructions
📌 Example
bash
Copy
Edit
python cleaner_script.py demo 50
This will:

Monitor the folder named demo (relative or absolute path supported)

Run every 50 minutes

Remove duplicate files

Log deleted files in marvellous/marvellous.txt

Send the log file via email

📨 Email Setup
To enable email notifications:

Replace the placeholder in the script:

python
Copy
Edit
msg["From"] = "your_email@example.com"
msg["To"] = "receiver_email@example.com"
s.login("your_email@example.com", "your_app_password")
Make sure:

You use a valid Gmail address.

You enable App Passwords in Gmail (2-Step Verification must be ON).

Use the 16-character app password in the script instead of your actual password.

📄 Log Output Example
pgsql
Copy
Edit
------------------------------------------------------
this is log file of maervellous scripting 
------------------------------------------------------
/full/path/to/duplicate_file1.txt
/full/path/to/duplicate_file2.txt

while scanning now, above files deleted at  Wed Aug 6 19:32:10 2025
⚙️ Dependencies
Install required packages if not already installed:

bash
Copy
Edit
pip install schedule
🧠 How It Works
Checksum: Calculates an MD5 checksum for each file. Files with identical checksums are considered duplicates.

Dictionary Storage: Duplicates are stored in a dictionary with checksums as keys and file paths as values.

Automated Deletion: If multiple files share a checksum, only one is kept; the rest are deleted.

Log & Email: Details of deleted files are logged and emailed to the configured address.

📌 Notes
This script deletes files permanently. Make sure you back up your data before testing.

Supports absolute and relative paths.

Compatible with Python 3.x.








