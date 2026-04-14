print("Missing values BEFORE cleaning:")
print(df.isnull().sum())

df['Systolic_BP'] = df['Systolic_BP'].fillna(df['Systolic_BP'].median())
df['Diastolic_BP'] = df['Diastolic_BP'].fillna(df['Diastolic_BP'].median())
print("\nMissing values AFTER cleaning:")
print(df.isnull().sum())
