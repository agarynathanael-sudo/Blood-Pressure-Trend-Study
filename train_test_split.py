from sklearn.model_selection import train_test_split
y = df['BP_Cat_enc'] # Encoded target variable
X_train, X_test, y_train, y_test = train_test_split(
X_scaled, y, test_size=0.2, random_state=42
)
print(f"Training set : X_train={X_train.shape} y_train={y_train.shape}")
print(f"Testing set : X_test={X_test.shape} y_test={y_test.shape}")
print(f"Train/Test ratio: 80% / 20%")
