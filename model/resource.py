class Resource:
    source = ""
    identifiant = ""
    organisme = ""
    titre = ""
    description = ""
    liens = []
    public_cible = ""
    thematiques = []
    duree = ""
    rattachement = ""
    adresse = ""
    code_postal = ""
    commune = ""
    geolocalisation = []

    def __int__(self):
        pass

    def __str__(self):
        return f'Source : {self.source}\n' \
               f'ID : {self.identifiant}\n' \
               f'Organisme : {self.organisme}\n' \
               f'Titre : {self.titre}\n' \
               f'Description : {self.description}\n' \
               f'Liens : {self.liens}\n' \
               f'Public cible : {self.public_cible}\n' \
               f'Thématiques : {self.thematiques}\n' \
               f'Durée : {self.duree}\n' \
               f'Rattachement : {self.rattachement}\n' \
               f'Adresse : {self.adresse}, {self.code_postal} {self.commune}\n' \
               f'Géolocalisation : {self.geolocalisation}\n'