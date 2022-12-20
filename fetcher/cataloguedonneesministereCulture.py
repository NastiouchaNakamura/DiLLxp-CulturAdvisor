import requests
from typing import List

from model.resource import Resource

url = "https://data.culture.gouv.fr/api/records/1.0/search/"
params = {
    "dataset": "catalogue-des-donnees-du-ministere-de-la-culture"
    #"rows": 120,
    #"start": 0
}
page_size = 512


def fetch() -> List[Resource]:
    """
    Champs renseignés :
    - identifiant
    - titre
    - description
    - domaine
    - sous_domaine
    - type_de_producteur
    - direction
    - service
    - sous_direction_departement
    - boite_fonctionnelle
    - precision_domaine
    - mots_cles
    - donnees_geolocalisees
    - lien1
    - lien2
    - couverture_geographique
    - type_de_format
    - autres_formats
    - frequence_de_mise_a_jour
    - volumetrie
    - statut_ouverture
    - date_de_mise_a_jour
    - actif_inactif
    """
    resources = []

    params["rows"] = page_size
    params["start"] = 0
    r = requests.get(url = url, params = params)
    response = r.json()
    while len(response["records"]) > 0:
        for record in response["records"]:
                # Création de l'objet Resource
                resource = Resource()

                """# Source
                # -> catalogue-des-donnees-du-ministere-de-la-culture
                resource.fields["source"] = record["datasetid"]"""

                
                # Titre
                if "titre" in record["fields"]:
                    resource.fields["titre"] = record["fields"]["titre"]
                resources.append(resource)

                # Description
                if "description" in record["fields"]:
                    resource.fields["description"] = record["fields"]["description"]
                resources.append(resource)

                # Lien1
                if "lien1" in record["fields"]:
                    resource.fields["liens"] = record["fields"]["lien1"]
                resources.append(resource)

                # Lien2
                if "lien2" in record["fields"]:
                    resource.fields["liens"] = record["fields"]["lien2"]
                resources.append(resource)

                # Domaine
                if "domaine" in record["fields"]:
                    resource.fields["domaine"] = record["fields"]["domaine"]
                resources.append(resource)
            
                # Sous-domaine
                if "sous_domaine" in record["fields"]:
                    resource.fields["sous_domaine"] = record["fields"]["sous_domaine"]
                resources.append(resource) 

                # Producteur
                if "type_de_producteur" in record["fields"]:
                    resource.fields["type_de_producteur"] = record["fields"]["type_de_producteur"]
                resources.append(resource)

                # Direction
                if "direction" in record["fields"]:
                    resource.fields["direction"] = record["fields"]["direction"]
                resources.append(resource)

                # Service
                if "service" in record["fields"]:
                    resource.fields["service"] = record["fields"]["service"]
                resources.append(resource)

                # Sous_direction_departement
                if "sous_direction_departement" in record["fields"]:
                    resource.fields["sous_direction_departement"] = record["fields"]["sous_direction_departement"]
                resources.append(resource)

                # Boite_fonctionnelle
                if "boite_fonctionnelle" in record["fields"]:
                    resource.fields["boite_fonctionnelle"] = record["fields"]["boite_fonctionnelle"]
                resources.append(resource)

                # Precision_domaine
                if "precision_domaine" in record["fields"]:
                    resource.fields["precision_domaine"] = record["fields"]["precision_domaine"]
                resources.append(resource)

                # Mots_cles
                if "mots_cles" in record["fields"]:
                    resource.fields["mots_cles"] = record["fields"]["mots_cles"]
                resources.append(resource)

                # Donnees_geolocalisees
                if "donnees_geolocalisees" in record["fields"]:
                    resource.fields["donnees_geolocalisees"] = record["fields"]["donnees_geolocalisees"]
                resources.append(resource)

                # Couverture_geographique
                if "couverture_geographique" in record["fields"]:
                    resource.fields["couverture_geographique"] = record["fields"]["couverture_geographique"]
                resources.append(resource)

                # Types
                if "type_de_format" in record["fields"]:
                    resource.fields["type_de_format"] = record["fields"]["type_de_format"]
                resources.append(resource)

                # Autre_format
                if "autres_formats" in record["fields"]:
                    resource.fields["autres_formats"] = record["fields"]["autres_formats"]
                resources.append(resource)

                # Frequence_de_mise_a_jour
                if "frequence_de_mise_a_jour" in record["fields"]:
                    resource.fields["frequence_de_mise_a_jour"] = record["fields"]["frequence_de_mise_a_jour"]
                resources.append(resource)

                # Volumetrie
                if "volumetrie" in record["fields"]:
                    resource.fields["volumetrie"] = record["fields"]["volumetrie"]
                resources.append(resource)

                # Statut_ouverture
                if "statut_ouverture" in record["fields"]:
                    resource.fields["statut_ouverture"] = record["fields"]["statut_ouverture"]
                resources.append(resource)

                # Date_de_mise_a_jour
                if "date_de_mise_a_jour" in record["fields"]:
                    resource.fields["date_de_mise_a_jour"] = record["fields"]["date_de_mise_a_jour"]
                resources.append(resource)

                # Actif_inactif
                if "actif_inactif" in record["fields"]:
                    resource.fields["actif_inactif"] = record["fields"]["actif_inactif"]
                resources.append(resource)


        params["start"] += page_size
        r = requests.get(url=url, params=params)
        response = r.json()

    return resources