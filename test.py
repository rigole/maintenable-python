def protect_animals(animals, sanctuary="little farm", max_places=4):
    """Place les animaux données."""
    is_little = "little" in sanctuary

    if max_places < 5 or is_little:
        print("C'est petit, mais c'est mieux que rien")

    protected = animals[:max_places]
    print(f"Nous avons protégés ces animaux M :{protected}")


animals = ["cochon", "poule", "cerf", "lapin", "chien"]
protect_animals(animals)
