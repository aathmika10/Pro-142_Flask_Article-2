import csv



allArticles=[]
with open("articles.csv",encoding='utf-8')as f:
    csvreader=csv.reader(f)
    data=list(csvreader)
    allArticles=data[1:]

likedArticles=[]
notLikedArticles=[]