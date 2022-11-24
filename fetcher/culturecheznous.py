import requests
from typing import List

from model.resource import Resource

url = "https://data.culture.gouv.fr/api/records/1.0/search/"
params = {
    "dataset": "culturecheznous",
    "facet": [
        "activite_proposee_apprendre_se_divertir_s_informer",
        "public_cible",
        "types_de_ressources_proposees",
        "thematiques",
        "contenus_adaptes_aux_types_de_handicap",
        "accessibilite_perennite_de_la_ressource",
        "rattachement_de_l_organisme"
    ],
    "rows": 40,
    "start": 0
}

def fetch() -> List[Resource]:
    r = requests.get(url = url, params = params)
    response = r.json()

    resources = []

    for record in response["records"]:
        resource = Resource()
        resource.source = record["datasetid"]
        resource.identifiant = record["recordid"]
        resource.organisme = record["fields"]["nom_de_l_organisme"]
        resource.titre = record["fields"]["titre_de_la_ressource"]
        resource.description = record["fields"]["description_des_contenus_et_de_l_experience_proposes_min_200_max_500_caracteres"]
        resource.liens = [record["fields"]["lien_vers_la_ressource"]] # Certaines ressources d'autres sources peuvent avoir plusieurs liens
        resource.public_cible = record["fields"]["public_cible"]
        resource.thematiques = record["fields"]["thematiques"].split(";")
        resource.duree = record["fields"]["temps_d_activite_estime_lecture_ecoute_visionnage_jeu"]
        resource.rattachement = record["fields"]["rattachement_de_l_organisme"]
        resource.adresse = record["fields"]["adresse_de_l_organisme"]
        resource.code_postal = record["fields"]["code_postal"]
        resource.commune = record["fields"]["commune"]
        if "geolocalisation_ban" in record["fields"]:
            resource.geolocalisation = record["fields"]["geolocalisation_ban"]

        resources.append(resource)

    for resource in resources:
        print(resource)

    return resources
