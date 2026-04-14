import numpy as np
import pandas as pd
np.random.seed(42)
N = 500
# Simulate dataset
df = pd.DataFrame({
'Patient_ID': [f"P{str(i).zfill(4)}" for i in range(1, N+1)],
'Age': np.random.randint(18, 80, N),
'Gender': np.random.choice(['Male','Female'], N),
'Systolic_BP': ..., # age-influenced + noise
'Diastolic_BP': ...,
'Smoking': np.random.choice(['Yes','No'], N, p=[0.3,0.7]),
'Exercise': np.random.choice(['Low','Moderate','High'], N),
'Date': pd.date_range('2022-01-01', periods=N, freq='12h')
})
print(df.head())
print(df.info())
