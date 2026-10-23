
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

