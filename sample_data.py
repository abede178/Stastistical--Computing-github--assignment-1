
data = {
    "Patient_ID": [1, 2, 3, 4, 5],
    "Age": [25, 34, 45, 29, 52],
    "Sex": ["Female", "Male", "Female", "Male", "Female"],
    "Diagnosis": ["Malaria", "TB", "HIV", "Malaria", "Pneumonia"]
}

df = pd.DataFrame(data)

print(df)

df.to_csv("sample_health_data.csv", index=False)
