import tkinter as tk
from tkinter import messagebox
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error

class hotel_analitic(object):
    def __init__(self, data):
        self.data = data
    
    def mashin_learning(self, new_price, new_customer_rating):
        X = [];
        y = [];
        for line in self.data.lines:
            words = line.split()
            X += [[int(words[1]), float(words[4])]]
            y += [float(words[5])]
                  
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        model = MLPRegressor(hidden_layer_sizes=(100, 50), max_iter=500, random_state=42)
        model.fit(X_train_scaled, y_train)

        y_pred = model.predict(X_test_scaled)
        
        mse = mean_squared_error(y_test, y_pred)
        print(f'Mean Squared Error: {mse}')

        new_data = np.array([[new_price, new_customer_rating]])
        new_data_scaled = scaler.transform(new_data)
        predicted_personal_rating = model.predict(new_data_scaled)
        return predicted_personal_rating[0];
        
    def analitic_hotel_form(self):
        def check_hotel(new_price, new_customer_rating):
            predict_mark = self.mashin_learning(new_price, new_customer_rating)
            label = tk.Label(root, text=f"May be your mark is {predict_mark:.1f}")
            label.grid(row = 5, columnspan=3, pady=5)
            

        root = tk.Toplevel()
        
        width = 300
        height = 200
        root.geometry(f"{width}x{height}")
        
        label = tk.Label(root, text="Name: ")
        label.grid(row = 0, columnspan=1, pady=5)
        label = tk.Label(root, text="Price: ")
        label.grid(row = 1, columnspan=1, pady=5)
        label = tk.Label(root, text="Region: ")
        label.grid(row = 2, columnspan=1, pady=5)
        label = tk.Label(root, text="Mark: ")
        label.grid(row = 3, columnspan=1, pady=5)
        
        
        entry_name = tk.Entry(root, width=30)
        entry_price = tk.Entry(root, width=30)
        entry_country = tk.Entry(root, width=30)
        entry_region = tk.Entry(root, width=30)
        entry_mark = tk.Entry(root, width=30)

        entry_name.grid(row=0, column=2, padx=10, pady=5)
        entry_price.grid(row=1, column=2, padx=10, pady=5)
        entry_region.grid(row=2, column=2, padx=10, pady=5)
        entry_mark.grid(row=3, column=2, padx=10, pady=5)
        
        add_button = tk.Button(root, text="Check hotel",  command=lambda: check_hotel(entry_price.get(), entry_mark.get()))
        add_button.grid(row = 30, columnspan=3, pady=10)

        root.mainloop()

    pass




