import requests
from typing import List

from model.resource import Resource

url = "https://data.culture.gouv.fr/api/records/1.0/search/"
params = {
    "dataset": "base-des-lieux-et-des-equipements-culturels"
    #"rows": 120,
    #"start": 0
}
page_size = 10000

def fetch() -> List[Resource]:
    """
    Champs renseignés :
    - type equipement lieu
    - precision equipement
    - nom
    - label
    - domaine
    - sous domaine
    - adresse
    - complement adresse    xxxxxxx
    - libele geographique
    - code postal
    - adresse postal
    - code insee
    - code insee Arrondt
    - region
    - departement
    - annee label           xxxxxxx
    - source
    - identifiant origine
    - num departement
    - num region
    - fonction 1
    - fonction 2
    - fonction 3
    - fonction 4
    - multiplexe
    - type cinema
    - nb fauteils cinema
    - nb ecrans
    - nb salles theatre
    - organisme siege theatre       xxxxxxx
    - jauge theatre
    - code reseau bibliotheque
    - nom reseau bibliotheque
    - archeologie detail
    - nom de l'illustre             xxxxxx
    - surface bibliotheque
    - coordonnees GPS
    - rang
    - ident
    - identifiant deps
    - libelle EPCI
    - code insee EPCI
    - demographie entree        xxxxxxx
    - demographie sortie        xxxxxxx
    - demographie detail        xxxxxxx
    """
    resources = []

    params["rows"] = page_size
    params["start"] = 0
    r = requests.get(url = url, params = params)
    response = r.json()
    #while len(response["records"]) > 0:
    for record in response["records"]:
            # Création de l'objet Resource
            resource = Resource()

            # Source
            # -> base-des-lieux-et-des-equipements-culturels
            resource.fields["source"] = record["datasetid"]

             
            # ident
            if "ident" in record["fields"]:
                resource.fields["identifiant"] = record["fields"]["ident"]
             
            # code postal
            if "code_postal" in record["fields"]:
                resource.fields["code postal"] = record["fields"]["code_postal"]
              
            # nom
            if "nom" in record["fields"]:
                resource.fields["titre"] = record["fields"]["nom"]
             
            # coordonnees GPS
            if "coordonnees_gps_lat_lon" in record["fields"]:
                resource.fields["geolocalisation"] = record["fields"]["coordonnees_gps_lat_lon"]
                        
            # adresse
            if "adresse" in record["fields"]:
                resource.fields["adresse"] = record["fields"]["adresse"]
             
            # libele geographique
            if "libelle_geographique" in record["fields"]:
                resource.fields["commune"] = record["fields"]["libelle_geographique"]
               
            # domaine
            if "domaine" in record["fields"]:
                resource.fields["domaine"] = record["fields"]["domaine"]

            # sous domaine
            if "sous_domaines" in record["fields"]:
                resource.fields["sous domaine"] = record["fields"]["sous_domaines"]
  
            # region
            if "region" in record["fields"]:
                resource.fields["region"] = record["fields"]["region"]
             
            # departement
            if "departement" in record["fields"]:
                resource.fields["departement"] = record["fields"]["departement"]
             
            # code insee Arrondt
            if "code_insee_arrondt" in record["fields"]:
                resource.fields["code insee"] = record["fields"]["code_insee_arrondt"]
            
            # code insee
            if "code_insee" in record["fields"]:
                resource.fields["code insee"] = record["fields"]["code_insee"]
             
            # code insee EPCI
            if "code_insee_epci" in record["fields"]:
                resource.fields["code insee EPCI"] = record["fields"]["code_insee_epci"] 
            
            # type equipement lieux
            if "type_equipement_ou_lieu" in record["fields"]:
                resource.fields["type equipement lieux"] = record["fields"]["type_equipement_ou_lieu"]
             
            # precision equipement
            if "precision_equipement" in record["fields"]:
                resource.fields["precision equipement"] = record["fields"]["precision_equipement"]
            
            # label
            if "label_et_appellation" in record["fields"]:
                resource.fields["label"] = record["fields"]["label_et_appellation"]
           
            # adresse postal
            if "adresse_postale" in record["fields"]:
                resource.fields["adresse postal"] = record["fields"]["adresse_postale"]
         
            # source
            if "source" in record["fields"]:
                resource.fields["sources"] = record["fields"]["source"]
             
            # identifiant origine
            if "identifiant_origine" in record["fields"]:
                resource.fields["identifiant origine"] = record["fields"]["identifiant_origine"]
             
            # num departement
            if "n_departement" in record["fields"]:
                resource.fields["num departement"] = record["fields"]["n_departement"]
             
            # num region
            if "n_region" in record["fields"]:
                resource.fields["num region"] = record["fields"]["n_region"]
                 
            # fonction 1
            if "fonction_1" in record["fields"]:
                resource.fields["fonctions"] = record["fields"]["fonction_1"]
              
            # fonction 2
            if "fonction_2" in record["fields"]:
                resource.fields["fonctions"] = record["fields"]["fonction_2"]
              
            # fonction 3
            if "fonction_3" in record["fields"]:
                resource.fields["fonctions"] = record["fields"]["fonction_3"]
              
            # fonction 4
            if "fonction_4" in record["fields"]:
                resource.fields["fonctions"] = record["fields"]["fonction_4"]
              
            # multiplexe
            if "multiplexe" in record["fields"]:
                resource.fields["multiplexe"] = record["fields"]["multiplexe"]
              
            # type cinema
            if "type_de_cinema" in record["fields"]:
                resource.fields["type cinema"] = record["fields"]["type_de_cinema"]
              
            # nb fauteils cinema
            if "nombre_fauteuils_de_cinema" in record["fields"]:
                resource.fields["nb fauteils cinema"] = record["fields"]["nombre_fauteuils_de_cinema"]
              
            # nb ecrans
            if "nombre_ecrans" in record["fields"]:
                resource.fields["nb ecrans"] = record["fields"]["nombre_ecrans"]
              
            # nb salles theatre
            if "nombre_de_salles_de_theatre" in record["fields"]:
                resource.fields["nb salles theatre"] = record["fields"]["nombre_de_salles_de_theatre"]
            
            # jauge theatre
            if "jauge_du_theatre" in record["fields"]:
                resource.fields["jauge theatre"] = record["fields"]["jauge_du_theatre"]

            # code reseau bibliotheque
            if "code_du_reseau_de_bibliotheques" in record["fields"]:
                resource.fields["code reseau bibliotheque"] = record["fields"]["code_du_reseau_de_bibliotheques"]

            # nom reseau bibliotheque
            if "nom_du_reseau_de_bibliotheques" in record["fields"]:
                resource.fields["nom reseau bibliotheque"] = record["fields"]["nom_du_reseau_de_bibliotheques"]

            # archeologie detail
            if "archeologie_detail" in record["fields"]:
                resource.fields["archeologie detail"] = record["fields"]["archeologie_detail"]
             
            # surface bibliotheque
            if "surface_bibliotheque" in record["fields"]:
                resource.fields["surface bibliotheque"] = record["fields"]["surface_bibliotheque"]
             
            # rang
            if "rang" in record["fields"]:
                resource.fields["rang"] = record["fields"]["rang"]

            # identifiant deps
            if "identifiant_deps_a_partir_de_2022" in record["fields"]:
                resource.fields["identifiant deps"] = record["fields"]["identifiant_deps_a_partir_de_2022"]
             
            # libelle EPCI
            if "libelle_epci" in record["fields"]:
                resource.fields["libelle EPCI"] = record["fields"]["libelle_epci"]
             

            resources.append(resource)


    #params["start"] += page_size
    r = requests.get(url=url, params=params)
    response = r.json()

    return resources