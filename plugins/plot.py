import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def run(sql_path):
    '''
    Write a plugin that accepts a path to an sqlite database created by plugin #5 and 
    uses the `matplotplib` Python module to build a plot and save is as a `.png` image.
    '''
    dat = sqlite3.connect(sql_path)
    query = dat.execute("SELECT * From frames")
    cols = [column[0] for column in query.description]
    df = pd.DataFrame.from_records(data = query.fetchall(), columns = cols)
    ax = plt.gca()
    df['coded_picture_number'] = df['coded_picture_number'].astype(float)
    df['pkt_size'] = df['pkt_size'].astype(float)
    df.plot(kind='line',x='coded_picture_number',y='pkt_size',ax=ax)

    plt.savefig('plot.png')
