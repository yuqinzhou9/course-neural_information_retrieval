
import json
import pandas as pd


# convert dataset from json to dataframe
def get_dataframe(path):
    with open (path) as corpus_json:
        corpus = [json.loads(line) for line in corpus_json]
    
    _rows = []
    for i in corpus:
        _rows.append([i['_id'], i['title'], i['text']])

    corpus_df = pd.DataFrame(_rows, columns=['_id', 'title', 'text'])
    corpus_df.rename(columns = {'_id' : 'docno'}, inplace = True)
    return corpus_df
    
# import query and qrel files
def get_query(path):
    query = pd.read_csv(path, dtype=str)
    return query

def get_qrel(path):
    qrel = pd.read_csv(path, dtype=str)
    qrel = qrel.loc[:, ["qid", "docno","label"]]
    qrel = qrel.astype({"label": int}) 
    return qrel