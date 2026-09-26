# On-Time Delivery Rate
df['on_time'] = df['delivery_time_min'] <= df['promised_time_min']
otdr = df['on_time'].mean() * 100
 
# Cost per Delivery
cpd = df['total_cost'].sum() / len(df)
 
print(f"On-Time Delivery Rate: {otdr:.1f}%")
print(f"Cost per Delivery: ${cpd:.2f}")
