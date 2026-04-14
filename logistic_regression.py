from sklearn.linear_model import LogisticRegression
model = LogisticRegression(max_iter=1000, random_state=42, C=1.0)
model.fit(X_train, y_train)
print("Model Training Complete!")
print(f"Model Type : {type(model).__name__}")
print(f"Classes : {model.classes_} => {le_cat.classes_}")
print(f"No. Iterations : {model.n_iter_[0]}")
print(f"Training Accuracy: {accuracy_score(y_train, model.predict(X_train))*100:.2f}%")
