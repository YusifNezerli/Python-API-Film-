import requests
import json
import sys

if len(sys.argv) > 1:
    filmname = " ".join(sys.argv[1:])
else:
    print("Zəhmət olmasa film adı qeyd et.")
    exit()

url = f"https://www.omdbapi.com/?apikey=a12a5664&1={filmname}"
response = requests.get(url)

if response.status_code != 200:
    print("""
This film is not found.

-----------------------
Request is failed.

    """)
    exit()

film_data = json.loads(response.text)

if film_data["Response"] == "False":
    print("""
------------------
This film is not found.

------------------
Request is successful.

    """)
    exit()

title = film_data["Title"]
year = film_data["Year"]
Released = film_data["Released"]
Genre = film_data["Genre"]
director = film_data["Director"]
actors = film_data["Actors"]
Country = film_data["Country"]
imdbRating = film_data["imdbRating"]

print(f"\n----------------------")
print(f"Title: {title}")
print(f"Year: {year}")
print(f"Released: {Released}")
print(f"Genre: {Genre}")
print(f"Director: {director}")
print(f"Actors: {actors}")
print(f"Country: {Country}")
print(f"IMDB: {imdbRating}")
print("""
----------------------
Request is seccessful.

""")