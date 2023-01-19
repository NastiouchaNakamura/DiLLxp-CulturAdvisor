import requests
from typing import List

from model.resource import Resource

url = "https://data.culture.gouv.fr/api/records/1.0/search/"
params = {
    "dataset": "festivals-global-festivals-_-pl"
    #"rows": 120,
    #"start": 0
}
page_size = 512


def fetch() -> List[Resource]:
    """
    Champs renseignés :
    - nom festival
    - envergure territoriale
    - region principale
    - departement principal
    - commune principale
    - periode principale
    - site internet
    - code postal
    - code insee commune
    - code insee EPCI
    - libelle EPCI
    - numero de voie
    - type de voie
    - nom de voie
    - adresse postale
    - complement adresse
    - adresse mail
    - discipline dominante
    - sous categorie spectacle
    - sous categorie musique
    - sous categorie musique CNM
    - sous categorie cinema
    - sous categorie art visuel
    - sous categorie livre
    - decenie de creation
    - annee de creation
    - identifiant
    - identifiant agence A
    - geocodage
    - identifiant CNM
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
                # -> festivals-global-festivals-_-pl
                resource.fields["source"] = record["datasetid"]

                # Nom du festival
                if "nom_du_festival" in record["fields"]:
                    resource.fields["titre"] = record["fields"]["nom_du_festival"]

                # site internet
                if "site_internet_du_festival" in record["fields"]:
                    resource.fields["site internet"] = record["fields"]["site_internet_du_festival"]

                # identifiant
                if "identifiant" in record["fields"]:
                    resource.fields["identifiant"] = record["fields"]["identifiant"]

                # code postal
                if "code_postal_de_la_commune_principale_de_deroulement" in record["fields"]:
                    resource.fields["code postal"] = record["fields"]["code_postal_de_la_commune_principale_de_deroulement"]

                # geocodage
                if "geocodage_xy" in record["fields"]:
                    resource.fields["geolocalisation"] = record["fields"]["geocodage_xy"]

                # adresse postale
                if "adresse_postale" in record["fields"]:
                    resource.fields["adresse postale"] = record["fields"]["adresse_postale"]

                # commune principale
                if "commune_principale_de_deroulement" in record["fields"]:
                    resource.fields["commune"] = record["fields"]["commune_principale_de_deroulement"]

                # adresse mail
                if "adresse_e_mail" in record["fields"]:
                    resource.fields["adresse mail"] = record["fields"]["adresse_e_mail"]

                # envergure territoriale
                if "envergure_territoriale" in record["fields"]:
                    resource.fields["couverture_geographique"] = record["fields"]["envergure_territoriale"]

                # region principale
                if "region_principale_de_deroulement" in record["fields"]:
                    resource.fields["region"] = record["fields"]["region_principale_de_deroulement"]

                # departement principal
                if "departement_principal_de_deroulement" in record["fields"]:
                    resource.fields["departement"] = record["fields"]["departement_principal_de_deroulement"]

                # code insee commune
                if "code_insee_commune" in record["fields"]:
                    resource.fields["code insee"] = record["fields"]["code_insee_commune"]

                # code insee EPCI
                if "code_insee_epci_collage_en_valeur" in record["fields"]:
                    resource.fields["code insee EPCI"] = record["fields"]["code_insee_epci_collage_en_valeur"]

                # libelle EPCI
                if "libelle_epci_collage_en_valeur" in record["fields"]:
                    resource.fields["libelle EPCI"] = record["fields"]["libelle_epci_collage_en_valeur"]

                # periode principale
                if "periode_principale_de_deroulement_du_festival" in record["fields"]:
                    resource.fields["periode principale"] = record["fields"]["periode_principale_de_deroulement_du_festival"]

                # numero de voie
                if "numero_de_voie" in record["fields"]:
                    resource.fields["numero de voie"] = record["fields"]["numero_de_voie"]

                # type de voie
                if "type_de_voie_rue_avenue_boulevard_etc" in record["fields"]:
                    resource.fields["type de voie"] = record["fields"]["type_de_voie_rue_avenue_boulevard_etc"]

                # nom de voie
                if "nom_de_la_voie" in record["fields"]:
                    resource.fields["nom de voie"] = record["fields"]["nom_de_la_voie"]

                # complement adresse
                if "complement_d_adresse_facultatif" in record["fields"]:
                    resource.fields["complement adresse"] = record["fields"]["complement_d_adresse_facultatif"]

                # discipline dominante
                if "discipline_dominante" in record["fields"]:
                    resource.fields["discipline dominante"] = record["fields"]["discipline_dominante"]

                # sous categorie spectacle
                if "sous_categorie_spectacle_vivant" in record["fields"]:
                    resource.fields["sous categorie spectacle"] = record["fields"]["sous_categorie_spectacle_vivant"]

                # sous categorie musique
                if "sous_categorie_musique" in record["fields"]:
                    resource.fields["sous categorie musique"] = record["fields"]["sous_categorie_musique"]

                # sous categorie musique CNM
                if "sous_categorie_musique_cnm" in record["fields"]:
                    resource.fields["sous categorie musique CNM"] = record["fields"]["sous_categorie_musique_cnm"]

                # sous categorie cinema
                if "sous_categorie_cinema_et_audiovisuel" in record["fields"]:
                    resource.fields["sous categorie cinema"] = record["fields"]["sous_categorie_cinema_et_audiovisuel"]

                # sous categorie art visuel
                if "sous_categorie_arts_visuels_et_arts_numeriques" in record["fields"]:
                    resource.fields["sous categorie art visuel"] = record["fields"]["sous_categorie_arts_visuels_et_arts_numeriques"]

                # sous categorie livre
                if "sous_categorie_livre_et_litterature" in record["fields"]:
                    resource.fields["sous categorie livre"] = record["fields"]["sous_categorie_livre_et_litterature"]

                # decenie de creation
                if "decennie_de_creation_du_festival" in record["fields"]:
                    resource.fields["decenie de creation"] = record["fields"]["decennie_de_creation_du_festival"]

                # annee de creation
                if "annee_de_creation_du_festival" in record["fields"]:
                    resource.fields["annee de creation"] = record["fields"]["annee_de_creation_du_festival"]

                # identifiant agence A
                if "identifiant_agence_a" in record["fields"]:
                    resource.fields["identifiant agence A"] = record["fields"]["identifiant_agence_a"]

                # identifiant CNM
                if "identifiant_cnm" in record["fields"]:
                    resource.fields["identifiant CNM"] = record["fields"]["identifiant_cnm"]
                resources.append(resource)


        params["start"] += page_size
        r = requests.get(url=url, params=params)
        response = r.json()

    return resources