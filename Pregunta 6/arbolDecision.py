import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import matplotlib.pyplot as plt

# Cargar el dataset
data = pd.read_csv("data.csv", encoding="latin1")

# Seleccionar características y objetivo
features = data.drop("booking_complete", axis=1)
target = data["booking_complete"]

# Preprocesamiento de datos
numeric_features = ["num_passengers", "purchase_lead", "length_of_stay", "flight_hour", "flight_duration"]
categorical_features = ["sales_channel", "trip_type", "flight_day", "route", "booking_origin", 
                        "wants_extra_baggage", "wants_preferred_seat", "wants_in_flight_meals"]

# Preprocesamiento para características numéricas y categóricas
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(), categorical_features)
    ])

# Crear un pipeline
clf = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', DecisionTreeClassifier(max_depth=3, random_state=42))
])

# Entrenar el modelo
clf.fit(features, target)

# Visualizar el árbol de decisión
plt.figure(figsize=(20, 10))
plot_tree(clf.named_steps['classifier'], 
          feature_names=clf.named_steps['preprocessor'].get_feature_names_out(), 
          class_names=["Not Completed", "Completed"], 
          filled=True)
plt.show()
