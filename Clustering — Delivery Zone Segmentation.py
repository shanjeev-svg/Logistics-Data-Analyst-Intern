from sklearn.cluster 
import KMeans
 
coords = df[['drop_lat', 'drop_lon']]
kmeans = KMeans(n_clusters=5, random_state=42, n_init='auto')
df['zone'] = kmeans.fit_predict(coords)
 
# Each 'zone' can now be assigned to a dedicated vehicle/route
zone_summary = df.groupby('zone').agg(orders=('order_id', 'count'))
