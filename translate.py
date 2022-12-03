def translate(json):
    status = json["status"]
    publication_status = json["publication-status"]
    if status == "AVAILABLE":
        json["status"] = "Disponivel"
    elif status == "REGISTERED":
        json["status"] = "Registrado"

    if publication_status == "published":
        json["publication-status"] = "Publicado"

    return json