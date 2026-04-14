df['Pulse_Pressure'] = df['Systolic_BP'] - df['Diastolic_BP']
# BP Category based on AHA guidelines
def bp_category(row):
s, d = row['Systolic_BP'], row['Diastolic_BP']
if s < 120 and d < 80: return 'Normal'
elif s < 130 and d < 80: return 'Elevated'
else: return 'High'
df['BP_Category'] = df.apply(bp_category, axis=1)
# Time-based features
df['Day'] = df['Date'].dt.day
df['Month'] = df['Date'].dt.month
print(df[['Systolic_BP','Diastolic_BP','Pulse_Pressure','BP_Category','Day','Month']].he
ad(5))
print("\nBP Category Distribution:")
print(df['BP_Category'].value_counts())
