from flask import Flask
from fetcher import culturecheznous, cataloguedonneesministereCulture, listefestivalfrance, basilic, eurelien
import pandas as pd
import numpy as np
import sqlite3
import csv
import mysql.connector
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    resources1 = culturecheznous.fetch()
    resources2 = cataloguedonneesministereCulture.fetch()
    resources3 = listefestivalfrance.fetch()
    resources4 = basilic.fetch()
    resources5 = eurelien.fetch()

    #for resource in resources5:
    #    print(resource.fields)

    res1 = []
    for resource1 in resources1:
        if resource1.fields not in res1: # supprimer les doublons
            res1.append(resource1.fields)
    res2 = []    
    for resource2 in resources2:
        if resource2.fields not in res2:
            res2.append(resource2.fields)
    res3 = []
    for resource3 in resources3:
        if resource3.fields not in res3: # supprimer les doublons
            res3.append(resource3.fields)
    res4 = []
    for resource4 in resources4:
        if resource4.fields not in res4: # supprimer les doublons
            res4.append(resource4.fields)
    res5 = []
    for resource5 in resources5:
        if resource5.fields not in res5: # supprimer les doublons
            res5.append(resource5.fields)

    # convertir en dataframe
    df1 = pd.DataFrame(res1) 
    df2 = pd.DataFrame(res2)
    df3 = pd.DataFrame(res3)
    df4 = pd.DataFrame(res4)
    df5 = pd.DataFrame(res5)
    # afficher les dataframes
    #print(df1) 
    #print(df2) 
    #print(df3) 
    #print(df4) 
    #print(df5) 


    # concatener les BDD et afficher le dataframe final
    frames = [df1, df2, df3,df5,df4]
    result = pd.concat(frames)
    print(result)

    #print(result['titre'])
    # afficher toute les colonnes du dataframe
    #print(result.columns)

    # afficher toute les valeurs d'une colonne
    #resultat = result.statut_ouverture.value_counts()
    #print(resultat)

    # créer un fichier csv des données
    result.to_csv('culture.csv', sep ='π')

    # rempli une base de données SQL à partir du csv
    #csv_to_db()
    
    return 'Hello World!'


def csv_to_db():
    sql_connection = mysql.connector.Connect(
        host="localhost",
        user="culturAdvisor",
        password="culturAdvisor",
        port="3306"
    )
    with open('culture.csv', 'r') as file:
        rows = csv.reader(file, delimiter='π')
        insert_req = "INSERT INTO culture_elements VALUES (%, %, %);"
        for row in rows:
            replace_list = []
            for value in row:
                if value == "":
                    replace_list.append(None)
                else:
                    replace_list.append(value)
            values = tuple(replace_list)
            sql_connection.execute(insert_req, values)
    return sql_connection


if __name__ == '__main__':
    app.run()



    """ nom des colonnes :
    ['origine', 'titre', 'description', 'site_internet', 'identifiant', 'code_postal', 'geolocalisation', 'adresse', 'commune', 'domaine',
       'organisme', 'public_cible', 'temps_activite', 'rattachement_organisme', 'types_ressource', 'activite', 'perenite_ressource',
       'niveau_scolaire_enfant', 'contenue_adapte', 'adresse_mail', 'couverture_geographique', 'type_de_producteur', 'direction',
       'mots_cles', 'formats', 'frequence_de_mise_a_jour', 'volumetrie', 'statut_ouverture', 'date_de_mise_a_jour', 'actif_inactif',
       'sous_domaine', 'service', 'sous_direction_departement', 'precision_domaine', 'donnees_geolocalise', 'adresse_postale', 'region',
       'departement', 'code_insee', 'code_insee_EPCI', 'libelle_EPCI', 'periode_principale', 'numero_de_voie', 'type_de_voie', 'nom_de_voie',
       'complement_adresse', 'discipline_dominante', 'sous_categorie_cinema', 'decenie_de_creation', 'annee_de_creation', 'sous_categorie_musique',
       'sous_categorie_musique_CNM', 'sous_categorie_livre', 'sous_categorie_spectacle', 'identifiant_CNM', 'identifiant_agence_A',
       'sous_categorie_art_visuel', 'type_equipement_lieux', 'label', 'adresse_postal', 'sources', 'identifiant_origine', 'num_departement',
       'num_region', 'fonctions', 'rang', 'identifiant_deps', 'precision_equipement', 'nb_salles_theatre', 'jauge_theatre',
       'surface_bibliotheque', 'multiplexe', 'type_cinema', 'nb_fauteils_cinema', 'nb_ecrans', 'keyword', 'license', 'license_url',
       'langage', 'modifie', 'publie', 'records_count', 'attributions', 'domain', 'staged', 'visibility', 'references']


    requete a faire :
       requete par code postal : de la forme 45100, 75000 ...
       requete par geolocalisation : de la forme [48.88785, 2.347225], ...
       requete par commune : paris, orleans, ...
       requete par public cible : tous public, enfant, parents/educateurs
       requete par status ouverture : non ouvert, ouvert
       requete par regions :
       reuete par departement :
       requete par numero departement : 70,11,25,...
       requete par numero region : 45,12,7,...


       """