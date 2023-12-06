from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np

df2=pd.read_csv("articles.csv")
df2=df2[df2["title"].notna()]

count=CountVectorizer(stop_words="english")
countMatrix=count.fit_transform(df2["title"])

cosineSim=cosine_similarity(countMatrix,countMatrix)

df2=df2.reset_index()
indices=pd.Series(df2.index,index=df2["contentId"])


def get_recommendations(contentId):
    idx=indices[int(contentId)]
    sim_scores=list(enumerate(cosineSim[idx]))
    sim_scores=sorted(sim_scores,key=lambda x: x[1],reverse=True)
    sim_scores=sim_scores[1:11]
    articleIndices=[i[0] for i in sim_scores]
    return df2[["url","title","text","lang","total_events"]].iloc[articleIndices].values.tolist()