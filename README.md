# Credit Card Fraud Detection (Mid-Hackathon Project)

This project implements a Machine Learning solution to detect fraudulent credit card transactions using highly imbalanced data.

## 📊 Dataset Overview
- **Total Transactions:** ~284,807
- **Fraud Cases:** ~492 (Only ~0.17% of the dataset)

## 🛠️ Tech Stack & Techniques
- **Language:** Python
- **Libraries:** Pandas, Seaborn, Matplotlib, Scikit-Learn
- **Imbalance Handling:** Class Weights (`class_weight='balanced'`)
- **Scaling:** StandardScaler applied to 'Time' and 'Amount' columns.

## 📈 Model Performance & Results

### 1. Logistic Regression
- **Recall:** 0.92 (Caught 90 out of 98 fraud cases)
- **Precision:** 0.06 (High False Positives: 1,389 normal transactions flagged as fraud)

### 2. Random Forest (Best Performer)
- **Precision:** 0.94 (Only 5 False Positives!)
- **Recall:** 0.79 (Caught 77 out of 98 fraud cases)
- **F1-Score:** 0.86

## 🎯 Conclusion
The **Random Forest Classifier** performed best overall. For a bank, managing False Positives is critical because locking genuine customers out of their accounts creates massive operational issues. Random Forest successfully achieved a high **F1-Score of 0.86**, making it the most practical model for real-world deployment.