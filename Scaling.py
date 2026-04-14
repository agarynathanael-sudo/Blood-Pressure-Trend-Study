from sklearn.preprocessing import StandardScaler
features = ['Age','Gender_enc','Smoking_enc','Exercise_enc',
'Pulse_Pressure','Day','Month']
X = df[features]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
import pandas as pd
print(pd.DataFrame(X_scaled[:3], columns=features).round(3))
