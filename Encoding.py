from sklearn.preprocessing import LabelEncoder
le_gender = LabelEncoder()
le_smoke = LabelEncoder()
le_ex = LabelEncoder()
df['Gender_enc'] = le_gender.fit_transform(df['Gender']) # Male=1, Female=0
df['Smoking_enc'] = le_smoke.fit_transform(df['Smoking']) # Yes=1, No=0
df['Exercise_enc'] = le_ex.fit_transform(df['Exercise']) # High=0, Low=1, Moderate=2
print(df[['Gender','Gender_enc','Smoking','Smoking_enc','Exercise','Exercise_enc']].head
(3))
