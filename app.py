from flask import Flask
from fetcher import culturecheznous, cataloguedonneesministereCulture
import pandas as pd
import numpy as np
import sqlite3
import csv
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    resources1 = culturecheznous.fetch()
    resources2 = cataloguedonneesministereCulture.fetch()

    res1 = []
    for resource1 in resources1:
        #print(resource1.fields)
        if resource1.fields not in res1: # supprimer les doublons
            res1.append(resource1.fields)
        
    res2 = []    
    for resource2 in resources2:
        #print(resource2.fields)
        if resource2.fields not in res2:
            res2.append(resource2.fields)

    # convertir en dataframe
    df1 = pd.DataFrame(res1) 
    print(df1)  
    df2 = pd.DataFrame(res2)
    print(df2)  

    # concatener les 2 BDD
    frames = [df1, df2]
    result = pd.concat(frames)
    print(result)

    # créer un fichier csv des données
    result.to_csv('culture.csv', sep ='\t') 

    return 'Hello World!'


if __name__ == '__main__':
    app.run()