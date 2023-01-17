import requests
from typing import List

from model.resource import Resource

url = "https://data.culture.gouv.fr/api/records/1.0/search/"
params = {
    "dataset": "culturecheznous"
    #"rows": 120,
    #"start": 0
}
page_size = 512


def fetch() -> List[Resource]:
    """
    Champs renseignés :
    - organisme
    - titre
    - liens
    - description
    - activite
    - public_cible
    - niveau scolaire enfant
    - types ressource
    - thematiques
    - contenue adapte
    - perenite ressource
    - temps activite
    - rattachement organisme
    - adresse
    - code_postal
    - commune
    - identifiant
    - geolocalisation
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

                # Source
                # -> culturecheznous
                resource.fields["source"] = record["datasetid"]

                # Titre
                if "titre_de_la_ressource" in record["fields"]:
                    resource.fields["titre"] = record["fields"]["titre_de_la_ressource"]
               
                # Description
                if "description_des_contenus_et_de_l_experience_proposes_min_200_max_500_caracteres" in record["fields"]:
                    resource.fields["description"] = record["fields"]["description_des_contenus_et_de_l_experience_proposes_min_200_max_500_caracteres"]

                # Liens
                if "lien_vers_la_ressource" in record["fields"]:
                    # Sur CultureChezNous il n'y a qu'un seul lien.
                    resource.fields["site internet"] = [record["fields"]["lien_vers_la_ressource"]] # Certaines ressources d'autres sources peuvent avoir plusieurs liens

                # Identifiant
                # ID de record
                resource.fields["identifiant"] = record["recordid"]

                # code postal
                if "code_postal" in record["fields"]:
                    resource.fields["code postal"] = record["fields"]["code_postal"]

                # Géolocalisation
                # Certaines resources n'ont pas de géolocalisation
                if "geolocalisation_ban" in record["fields"]:
                    resource.fields["geolocalisation"] = record["fields"]["geolocalisation_ban"]

                # Adresse
                if "adresse_de_l_organisme" in record["fields"]:
                    resource.fields["adresse"] = record["fields"]["adresse_de_l_organisme"]
                
                # commune
                if "commune" in record["fields"]:
                    resource.fields["commune"] = record["fields"]["commune"]

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
                    resource.fields["domaine"] = record["fields"]["thematiques"].split(";")

                # Organisme
                if "nom_de_l_organisme" in record["fields"]:
                    resource.fields["organisme"] = record["fields"]["nom_de_l_organisme"]


                # Public cible
                if "public_cible" in record["fields"]:
                    # {'Parents / Éducateurs', 'Tous publics', 'Enfants'}
                    resource.fields["public_cible"] = record["fields"]["public_cible"]

                # temps activite
                if "temps_d_activite_estime_lecture_ecoute_visionnage_jeu" in record["fields"]:
                    resource.fields["temps activite"] = record["fields"]["temps_d_activite_estime_lecture_ecoute_visionnage_jeu"]

                # Rattachement organisme
                if "rattachement_de_l_organisme" in record["fields"]:
                    resource.fields["rattachement organisme"] = record["fields"]["rattachement_de_l_organisme"]

                # Type ressource
                if "types_de_ressources_proposees" in record["fields"]:
                    resource.fields["types ressource"] = record["fields"]["types_de_ressources_proposees"]

                # niveau scolaire enfant
                if "si_enfants_merci_de_preciser_le_niveau_scolaire" in record["fields"]:
                    resource.fields["niveau scolaire enfant"] = record["fields"]["si_enfants_merci_de_preciser_le_niveau_scolaire"]

                # Activités
                if "activite_proposee_apprendre_se_divertir_s_informer" in record["fields"]:
                    resource.fields["activite"] = record["fields"]["activite_proposee_apprendre_se_divertir_s_informer"]

                # contenue adapte
                if "contenus_adaptes_aux_types_de_handicap" in record["fields"]:
                    resource.fields["contenue adapte"] = record["fields"]["contenus_adaptes_aux_types_de_handicap"]

                # perenite ressource
                if "accessibilite_perennite_de_la_ressource" in record["fields"]:
                    resource.fields["perenite ressource"] = record["fields"]["accessibilite_perennite_de_la_ressource"]

                
                resources.append(resource)

        params["start"] += page_size
        r = requests.get(url=url, params=params)
        response = r.json()

    #for resource in resources:
    #    print(resource)

    return resources
