
<<<<<<< HEAD
import pandas as pd

data = {
    "patient_id": [1, 2, 3, 4, 5],
    "age": [24, 35, 42, 29, 51],
    "sex": ["Female", "Male", "Female", "Male", "Female"],
    "tested_positive": [0, 1, 0, 1, 1]
}

df = pd.DataFrame(data)
df.to_csv("sample_data.csv", index=False)

print("Sample data created successfully!")
print(df)

=======
data = {
    "Patient_ID": [1, 2, 3, 4, 5],
    "Age": [25, 34, 45, 29, 52],
    "Sex": ["Female", "Male", "Female", "Male", "Female"],
    "Diagnosis": ["Malaria", "TB", "HIV", "Malaria", "Pneumonia"]
}

df = pd.DataFrame(data)

print(df)

df.to_csv("sample_health_data.csv", index=False)
>>>>>>> 9197f12c8bb9a0a3350c0bf3bb89c7dc4350cd2e
