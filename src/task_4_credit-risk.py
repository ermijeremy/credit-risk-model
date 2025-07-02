import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def load_data(file_path):
    return pd.read_csv(file_path)

address = "C:/Users/hp/Desktop/Kifya/Week_5/credit-risk-model/data/"
df = load_data(address + "data/raw.csv")

df["TransactionStartTime"] = pd.to_datetime(df["TransactionStartTime"])

# prepare snapshote date for calculating the recency
snapshot_date=df["TransactionStartTime"].max()+pd.Timedelta(days=1)


# calculate the recency
recency_df=df.groupby("CustomerId")["TransactionStartTime"].max().reset_index()
recency_df["recency"]=(snapshot_date-recency_df["TransactionStartTime"]).dt.days

# calculate the frequency
frequency_df=df.groupby("CustomerId")["TransactionId"].nunique().reset_index()
frequency_df.columns=["CustomerId","frequency"]

# calculate the monetary
monetary_df=df.groupby("CustomerId")["Amount"].sum().reset_index()
monetary_df.columns=["CustomerId","monetary"]

# Merge All RFM Metrics
rfm = recency_df.merge(frequency_df, on='CustomerId').merge(monetary_df, on='CustomerId')

scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm[['recency', 'frequency', 'monetary']])


# clustering the data into 3 group based on value rfm
kmeans=KMeans(n_clusters=3,random_state=42)
clusters=kmeans.fit_predict(rfm_scaled)

rfm["clusters"]=clusters
cluster_summary = rfm.groupby('clusters')[['recency', 'frequency', 'monetary']].mean()
high_risk_cluster = cluster_summary['frequency'].idxmin()
rfm['is_high_risk'] = (rfm['clusters'] == high_risk_cluster).astype(int)

# merge the clusters columns with in rfm to the main cleaned data
df["is_high_risk"]=rfm['is_high_risk']
