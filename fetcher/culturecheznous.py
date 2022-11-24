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
    #"rows": 120,
    #"start": 0
}
page_size = 512

def fetch() -> List[Resource]:
    resources = []

    publics = set()
    thematiques = set()

    params["rows"] = page_size
    params["start"] = 0
    r = requests.get(url = url, params = params)
    response = r.json()
    while len(response["records"]) > 0:
        for record in response["records"]:
                # Création de l'objet Resource
                resource = Resource()

                # Source
                # -> culturecheznous
                resource.source = record["datasetid"]

                # Identifiant
                # ID de record
                resource.identifiant = record["recordid"]

                # Organisme
                if "nom_de_l_organisme" in record["fields"]:
                    resource.organisme = record["fields"]["nom_de_l_organisme"]

                # Titre
                if "titre_de_la_ressource" in record["fields"]:
                    resource.titre = record["fields"]["titre_de_la_ressource"]

                # Description
                if "description_des_contenus_et_de_l_experience_proposes_min_200_max_500_caracteres" in record["fields"]:
                    resource.description = record["fields"]["description_des_contenus_et_de_l_experience_proposes_min_200_max_500_caracteres"]

                # Liens
                if "lien_vers_la_ressource" in record["fields"]:
                    # Sur CultureChezNous il n'y a qu'un seul lien.
                    resource.liens = [record["fields"]["lien_vers_la_ressource"]] # Certaines ressources d'autres sources peuvent avoir plusieurs liens

                # Public cible
                if "public_cible" in record["fields"]:
                    # {'Parents / Éducateurs', 'Tous publics', 'Enfants'}
                    publics.add(record["fields"]["public_cible"])
                    resource.public_cible = record["fields"]["public_cible"]

                # Thématiques
                if "thematiques" in record["fields"]:
                    # ['Architecture et patrimoine', 'Archives', 'Archéologie',
                    # 'Art urbain (graph, hip hop, street art…)', 'Arts du cirque, arts de la rue',
                    # 'Arts décoratifs, design, métiers d’art', 'Arts numériques', 'Arts visuels', 'Audiovisuel',
                    # 'Bande dessinée', 'Cinéma', 'Danse', 'Histoire', 'Humour et performances',
                    # 'Littérature, sciences humaines, langues', 'Mode', 'Monuments historiques',
                    # 'Musique, concerts et opéras', 'Musées', 'Parcs et jardins', 'Peinture', 'Photographie',
                    # 'Sciences', 'Sculpture', 'Théâtre, Spectacles', 'Éducation artistique et culturelle',
                    # 'Éducation aux médias']
                    # /!\ Thématique "Vidéo, flux en direct, programmes en différé;;;;;;;;" par exemple
                    for thematique in record["fields"]["thematiques"].split(";"):
                        if (thematique) != "":
                            thematiques.add(thematique)
                    resource.thematiques = record["fields"]["thematiques"].split(";")

                # Durée
                if "temps_d_activite_estime_lecture_ecoute_visionnage_jeu" in record["fields"]:
                    resource.duree = record["fields"]["temps_d_activite_estime_lecture_ecoute_visionnage_jeu"]

                # Rattachement
                if "rattachement_de_l_organisme" in record["fields"]:
                    resource.rattachement = record["fields"]["rattachement_de_l_organisme"]

                # Adresse
                if "adresse_de_l_organisme" in record["fields"]:
                    resource.adresse = record["fields"]["adresse_de_l_organisme"]
                if "code_postal" in record["fields"]:
                    resource.code_postal = record["fields"]["code_postal"]
                if "commune" in record["fields"]:
                    resource.commune = record["fields"]["commune"]

                # Géolocalisation
                # Certaines resources n'ont pas de géolocalisation
                if "geolocalisation_ban" in record["fields"]:
                    resource.geolocalisation = record["fields"]["geolocalisation_ban"]

                resources.append(resource)

        params["start"] += page_size
        r = requests.get(url=url, params=params)
        response = r.json()

    #for resource in resources:
    #    print(resource)

    print(len(publics))
    print(publics)
    print(len(thematiques))
    print(sorted(list(thematiques)))
    print(len(resources))

    return resources
