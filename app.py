import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
from tkinter import messagebox
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

# =====================================================================
# BACKGROUND BACKEND: DATA & MODEL TRAINING
# =====================================================================
print("Loading data and training model in background... Please wait...")
df = pd.read_csv('creditcard.csv')

X = df.drop(columns=['Class'])
y = df['Class']

# Scale Time and Amount
scaler = StandardScaler()
X[['Time', 'Amount']] = scaler.fit_transform(X[['Time', 'Amount']])

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Train the best model (Random Forest)
rf_model = RandomForestClassifier(class_weight='balanced', n_estimators=20, random_state=42, n_jobs=-1)
rf_model.fit(X_train, y_train)
print("Model trained successfully! Opening Frontend Window...")

# =====================================================================
# FRONTEND: TKINTER GUI INTERFACE
# =====================================================================
def predict_fraud():
    try:
        # User input se values uthana
        time_val = float(entry_time.get())
        amount_val = float(entry_amount.get())
        
        # Baki V1-V28 features ke liye dummy 0.0 values (kyunki wo anonymized hain)
        dummy_features = [0.0] * 28
        
        # Input data frame banana
        input_data = pd.DataFrame([[time_val] + dummy_features + [amount_val]], columns=X.columns)
        
        # Scale the inputs exactly like training data
        input_data[['Time', 'Amount']] = scaler.transform(input_data[['Time', 'Amount']])
        
        # Prediction karna
        prediction = rf_model.predict(input_data)[0]
        
        # Result show karna popup box mein
        if prediction == 1:
            messagebox.showerror("RESULT", "⚠️ ALERT: This transaction is FRAUDULENT!")
        else:
            messagebox.showinfo("RESULT", "✅ SUCCESS: This transaction is CLEAN / NORMAL.")
            
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter valid numbers for Time and Amount.")

# Main Window Window setup
root = tk.Tk()
root.title("Credit Card Fraud Detection System")
root.geometry("450x350")
root.configure(bg="#f0f2f5")

# Labels & Headings
label_title = tk.Label(root, text="🛡️ Credit Card Fraud Detector", font=("Arial", 16, "bold"), bg="#f0f2f5", fg="#333")
label_title.pack(pady=20)

# Time Input Section
label_time = tk.Label(root, text="Enter Time (in seconds):", font=("Arial", 11), bg="#f0f2f5")
label_time.pack(pady=5)
entry_time = tk.Entry(root, font=("Arial", 11), width=25)
entry_time.insert(0, "400")  # Default example value
entry_time.pack(pady=5)

# Amount Input Section
label_amount = tk.Label(root, text="Enter Amount ($):", font=("Arial", 11), bg="#f0f2f5")
label_amount.pack(pady=5)
entry_amount = tk.Entry(root, font=("Arial", 11), width=25)
entry_amount.insert(0, "99.99")  # Default example value
entry_amount.pack(pady=5)

# Predict Button
btn_predict = tk.Button(root, text="Check Transaction", font=("Arial", 12, "bold"), bg="#007bff", fg="white", width=20, command=predict_fraud)
btn_predict.pack(pady=25)

root.lift()
root.attributes('-topmost', True)
# Run Frontend Loop
root.mainloop()
