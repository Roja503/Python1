import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from lightgbm import LGBMRegressor
from xgboost import XGBRegressor
from catboost import CatBoostRegressor
from sklearn.metrics import mean_squared_error
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.neural_network import MLPRegressor
import matplotlib.pyplot as plt

global filename
global df, X_train, X_test, y_train, y_test

def upload():
    global filename, df
    filename = filedialog.askopenfilename(initialdir="dataset")
    pathlabel.config(text=filename)
    df = pd.read_csv(filename)
    
    # Replace '?' with NaN
    df.replace('0', np.nan, inplace=True)

    # Fill missing values with mode for each column
    df.fillna(df.mode().iloc[0], inplace=True)
    
    text.delete('1.0', tk.END)
    text.insert(tk.END, 'Dataset loaded\n')
    text.insert(tk.END, "Dataset Size: " + str(len(df)) + "\n")

def splitdataset(): 
    global df, X_train, X_test, y_train, y_test

    # Encode string columns to numerical values
    label_encoder = LabelEncoder()
    for column in df.columns:
        if df[column].dtype == 'object':
            df[column] = label_encoder.fit_transform(df[column])

    X = df[['week', 'center_id', 'meal_id', 'checkout_price', 'base_price', 'emailer_for_promotion', 'homepage_featured']]
    y = df['num_orders']
   
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)    
    # Display dataset split information
    text.delete('1.0', tk.END)
    text.insert(tk.END, "Dataset split\n")
    text.insert(tk.END, "Splitted Training Size for Machine Learning : " + str(len(X_train)) + "\n")
    text.insert(tk.END, "Splitted Test Size for Machine Learning    : " + str(len(X_test)) + "\n")
    
    # Display shapes of X_train, X_test, y_train, y_test
    text.insert(tk.END, "\nShape of X_train: " + str(X_train.shape) + "\n")
    text.insert(tk.END, "Shape of X_test: " + str(X_test.shape) + "\n")
    text.insert(tk.END, "Shape of y_train: " + str(y_train.shape) + "\n")
    text.insert(tk.END, "Shape of y_test: " + str(y_test.shape) + "\n\n")



def random_forest():
    text.delete('1.0', tk.END)  # Delete previous text
    global rf_accuracy, rf
    rf = RandomForestRegressor(n_estimators=100, random_state=0)
    rf.fit(X_train, y_train)
    rf_accuracy = rf.score(X_test, y_test)*100
    result_text = f'Accuracy Score for Random Forest is {rf_accuracy}\n'
    text.insert(tk.END, result_text)

def gradient_boosting():
    text.delete('1.0', tk.END)  # Delete previous text
    global gbr_accuracy
    gbr = GradientBoostingRegressor(random_state=0)
    gbr.fit(X_train, y_train)
    gbr_accuracy = gbr.score(X_test, y_test)*100
    result_text = f'Accuracy Score for Gradient Boosting is {gbr_accuracy}\n'
    text.insert(tk.END, result_text)

def lightgbm():
    text.delete('1.0', tk.END)  # Delete previous text
    global lgbm_accuracy,lgbm
    lgbm = LGBMRegressor(random_state=0)
    lgbm.fit(X_train, y_train)
    lgbm_accuracy = lgbm.score(X_test, y_test)*100
    result_text = f'Accuracy Score for LightGBM is {lgbm_accuracy}\n'
    text.insert(tk.END, result_text)

def xgboost():
    text.delete('1.0', tk.END)  # Delete previous text
    global xgb_accuracy
    xgb = XGBRegressor(random_state=0)
    xgb.fit(X_train, y_train)
    xgb_accuracy = xgb.score(X_test, y_test)*100
    result_text = f'Accuracy Score for XGBoost is {xgb_accuracy}\n'
    text.insert(tk.END, result_text)

def catboost():
    text.delete('1.0', tk.END)  # Delete previous text
    global cat_accuracy
    cat = CatBoostRegressor(random_state=0, verbose=False)
    cat.fit(X_train, y_train)
    cat_accuracy = cat.score(X_test, y_test)*100
    result_text = f'Accuracy Score for CatBoost is {cat_accuracy}\n'
    text.insert(tk.END, result_text)

def plot_bar_graph():
    algorithms = ['Random Forest', 'Gradient Boosting', 'LightGBM', 'XGBoost', 'CatBoost']
    accuracies = [rf_accuracy, gbr_accuracy, lgbm_accuracy, xgb_accuracy, cat_accuracy]

    plt.figure(figsize=(10, 6))
    plt.bar(algorithms, accuracies, color='skyblue')
    plt.xlabel('Algorithms')
    plt.ylabel('Accuracy Score')
    plt.title('Accuracy Score by Algorithm')
    plt.xticks(rotation=45)
    plt.ylim(0, 1)  # Set y-axis limit between 0 and 1 for accuracy scores
    plt.show()

def plot_week_vs_num_orders():
    plt.figure(figsize=(10, 6))
    plt.plot(df['week'], df['num_orders'], marker='o', linestyle='-')
    plt.xlabel('Week')
    plt.ylabel('Number of Orders')
    plt.title('Week vs Number of Orders')
    plt.grid(True)
    plt.show()
def predict():
    global rf
    file_path = filedialog.askopenfilename(initialdir=".", title="Select CSV file", filetypes=(("CSV files", "*.csv"), ("All files", "*.*")))
    if file_path:
        test_data = pd.read_csv(file_path)
        test_data.replace('0', np.nan, inplace=True)
        test_data.fillna(test_data.mode().iloc[0], inplace=True)
        X_pred = test_data[['week', 'center_id', 'meal_id', 'checkout_price', 'base_price', 'emailer_for_promotion', 'homepage_featured']]
        y_pred = lgbm.predict(X_pred)
        text.delete('1.0', tk.END)
        text.insert(tk.END, f'Predicted results:\n{y_pred}\n')

def plot_custom_graph():
    plt.figure(figsize=(10, 6))
    plt.scatter(df['meal_id'], df['base_price'], c=df['num_orders'], cmap='viridis')
    plt.colorbar(label='Number of Orders')
    plt.xlabel('Meal ID')
    plt.ylabel('Base Price')
    plt.title('Scatter Plot: Meal ID vs Base Price colored by Number of Orders')
    plt.grid(True)
    plt.show()


    

main = tk.Tk()
main.title("Time Series Forecasting and Modeling of Food Demand Supply Chain Based on Regressors Analysis") 
main.geometry("1500x900")

font = ('times', 16, 'bold')
title = tk.Label(main, text='Time Series Forecasting and Modeling of Food Demand Supply Chain Based on Regressors Analysis',font=("times"))
title.config(bg='Dark Blue', fg='white')
title.config(font=font)           
title.config(height=3, width=145)
title.place(x=0, y=5)

font1 = ('times', 12, 'bold')
text = tk.Text(main, height=20, width=150)
scroll = tk.Scrollbar(text)
text.configure(yscrollcommand=scroll.set)
text.place(x=50, y=120)
text.config(font=font1)

uploadButton = tk.Button(main, text="Upload Dataset", command=upload, bg="sky blue", width=15)
uploadButton.place(x=50, y=600)
uploadButton.config(font=font1)

pathlabel = tk.Label(main)
pathlabel.config(bg='Dark blue', fg='white')  
pathlabel.config(font=font1)           
pathlabel.place(x=250, y=600)

splitButton = tk.Button(main, text="Split Dataset", command=splitdataset, bg="light green", width=15)
splitButton.place(x=450, y=600)
splitButton.config(font=font1)

#rfButton = tk.Button(main, text="Random Forest", command=random_forest, bg="lightblue", width=15)
#rfButton.place(x=50, y=650)
#rfButton.config(font=font1)

#gbrButton = tk.Button(main, text="Gradient Boosting", command=gradient_boosting, bg="lightcoral", width=15)
#gbrButton.place(x=250, y=650)
#gbrButton.config(font=font1)

lgbmButton = tk.Button(main, text="LightGBM", command=lightgbm, bg="lightyellow", width=15)
lgbmButton.place(x=50, y=650)
lgbmButton.config(font=font1)

#xgbButton = tk.Button(main, text="XGBoost", command=xgboost, bg="lightgreen", width=15)
#xgbButton.place(x=650, y=650)
#xgbButton.config(font=font1)

#catButton = tk.Button(main, text="CatBoost", command=catboost, bg="lightpink", width=15)
#catButton.place(x=850, y=650)
#catButton.config(font=font1)

plotButton = tk.Button(main, text="Plot Results", command=plot_bar_graph, bg="white", width=15)
plotButton.place(x=250, y=700)
plotButton.config(font=font1)

plotWeekButton = tk.Button(main, text="Plot Week vs Num Orders", command=plot_week_vs_num_orders, bg="yellow", width=20)
plotWeekButton.place(x=250, y=700)
plotWeekButton.config(font=font1)

predictButton = tk.Button(main, text="Predict", command=predict, bg="yellow", width=15)
predictButton.place(x=850, y=700)
predictButton.config(font=font1)

# Create a button for plotting the custom graph
customPlotButton = tk.Button(main, text="Plot Custom Graph", command=plot_custom_graph, bg="lightyellow", width=20)
customPlotButton.place(x=450, y=700)
customPlotButton.config(font=font1)

main.config(bg='#3498db')
main.mainloop()
