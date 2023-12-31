import csv
import pandas as pd

with open('movies.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]
    headers = data[0]

headers.append("poster_link")

with open(final_links.csv) as f:
    csvwritter = csv.writter(f)
    csvwritter.writerow(headers)


with open("movie_lins.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movie_links = data[1:]

for movie_item in all_movies:
    poster_found = any(movie_item[8] in movie_link_items for movie_link_items in all_movie_links)
    if poster_found:
        for movie_link_item in all_movie_links:
            if movie_item[8] == all_movie_links:
                movie_item.append(movie_link_item[0])
                if len(movie_item) == 28:
                    with open("final.csv", "a+") as f:
                        csvwritter = csv.writter(f)
                        csvwritter.writerow(movie_item)

df = pd.read_csv('final.csv')
df = df[df['soup'].notna()]