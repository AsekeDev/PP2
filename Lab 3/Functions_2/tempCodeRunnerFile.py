hitman_movie = next((movie for movie in movies if movie["name"] == "Hitman"), None)
if hitman_movie:
    print("Hitman is highly rated:", is_highly_rated(hitman_movie))