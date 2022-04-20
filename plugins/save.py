import json
import pandas as pd
import sqlite3 as sq

def main(path):
    '''
    Write a plugin that accepts a path 
    to a json file created by plugin #4 
    and saves per-frame information into an sqlite database.
    '''
    with open(path) as j:
        data = json.load(j)

    df = pd.DataFrame(data.get('frames'))
    table_name = "frames" 

    conn = sq.connect(f'{table_name}.sqlite')
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()