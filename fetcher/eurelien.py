import requests
from typing import List

from model.resource import Resource

url = "https://data.eurelien.fr/api/datasets/1.0/search/"
params = {
    "dataset": ""
    #"rows": 120,
    #"start": 0
}
page_size = 58

def fetch() -> List[Resource]:
    """
    Champs renseignés :
    - description
    """
    resources = []

    params["rows"] = page_size
    params["start"] = 0
    r = requests.get(url = url, params = params)
    response = r.json()
    #while len(response["records"]) > 0:
    for record in response["datasets"]:
            # Création de l'objet Resource
            resource = Resource()

            # Source
            # -> base-des-lieux-et-des-equipements-culturels
            resource.fields["source"] = record["datasetid"]

            # titre
            if "title" in record["metas"]:
                resource.fields["titre"] = record["metas"]["title"]
             
            # description
            if "description" in record["metas"]:
                resource.fields["description"] = record["metas"]["description"]
            
            # domaine
            if "theme" in record["metas"]:
                resource.fields["domaine"] = record["metas"]["theme"]
             
            # keyword
            if "keyword" in record["metas"]:
                resource.fields["keyword"] = record["metas"]["keyword"]
             
            # license
            if "license" in record["metas"]:
                resource.fields["license"] = record["metas"]["license"]
             
            # license_url
            if "license_url" in record["metas"]:
                resource.fields["license_url"] = record["metas"]["license_url"]
            
            # langage
            if "language" in record["metas"]:
                resource.fields["langage"] = record["metas"]["language"]
            
            # modifie
            if "modified" in record["metas"]:
                resource.fields["modifie"] = record["metas"]["modified"]
            
            # couverture_geographique
            if "territory" in record["metas"]:
                resource.fields["couverture_geographique"] = record["metas"]["territory"]

            # publie
            if "publisher" in record["metas"]:
                resource.fields["publie"] = record["metas"]["publisher"]
             
            # references
            if "references" in record["metas"]:
                resource.fields["references"] = record["metas"]["references"]
             
            # records_count
            if "records_count" in record["metas"]:
                resource.fields["records_count"] = record["metas"]["records_count"]
            
            # attributions
            if "attributions" in record["metas"]:
                resource.fields["attributions"] = record["metas"]["attributions"]
            
            # domain
            if "domain" in record["metas"]:
                resource.fields["domain"] = record["metas"]["domain"]
            
            # staged
            if "staged" in record["metas"]:
                resource.fields["staged"] = record["metas"]["staged"]
             
            # visibility
            if "visibility" in record["metas"]:
                resource.fields["visibility"] = record["metas"]["visibility"]
             
            
            
            

            resources.append(resource)


    #params["start"] += page_size
    r = requests.get(url=url, params=params)
    response = r.json()

    return resources