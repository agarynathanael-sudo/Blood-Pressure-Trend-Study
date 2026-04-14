y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)
# Sample predictions vs actual
sample_df = pd.DataFrame({
'Actual' : le_cat.inverse_transform(y_test[:8]),
'Predicted': le_cat.inverse_transform(y_pred[:8]),
'P(Elevated)': y_prob[:8,0].round(3),
'P(High)' : y_prob[:8,1].round(3),
'P(Normal)' : y_prob[:8,2].round(3),
})
print(sample_df.to_string(index=False))
