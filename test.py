import pandas as pd
import regex as re

#to remove hashtag and @ characters
def preprocessing(tweet):
    tweet = " ".join(re.sub("([^0-9A-Za-z |t])|(\w+:\/\/\S+)","",tweet).split())
    tweet = re.sub(r"\d","",tweet)
    return tweet




#assume the profanity words are stored in a hashset so lookup complexity is O(1)
df = pd.read_csv("train_E6oV3lV.csv")
bad_words= {"****","shit"}
profanity_index = [0]*len(df)
for i in range(len(df)):
    a = (df.loc[i,"tweet"])
    a = preprocessing(a)
    count =0 

    for j in range(len(a)):
        if a[j] in bad_words:
            count+=1
    profanity_index[i] = count







