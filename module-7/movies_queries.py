import mysql.connector

db = mysql.connector.connect(
    host = "127.0.0.1",
    user = "movies_user",
    password = "popcorn",
    database = "movies"
)

cursor = db.cursor()
#First query Studio
cursor.execute("SELECT studio_id, studio_name FROM studio")
print("--Studio Table:--")
print("Studio_id | Studio_name")
studio = cursor.fetchall()

for s in studio:
    print(s)
#Second query Genre
cursor.execute("SELECT genre_id, genre_name FROM genre")
print("\n--Genre Table:--")
print("Genre_id | Genre_name")
genre = cursor.fetchall()

for g in genre:
    print(g)

#Third query
cursor.execute("SELECT film_name FROM film WHERE film_runtime <120")
print("\n--Short Films:--")
for row in cursor.fetchall():
    print("Movie: ", row[0])

#Fourth query
cursor.execute("SELECT film_director, GROUP_CONCAT(film_name) FROM film GROUP BY film_director")
print("\n--Movies Grouped by Director:--")
for row in cursor.fetchall():
    print("Director: ", row[0])
    print("Movies ", row[1])

def show_films(cursor, title):
    # Define the SQL query to select film information with joins
    cursor.execute("SELECT film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' from film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id")

    # Fetch all films from the executed query
    films = cursor.fetchall()

    # Print the title
    print("\n -- {} --".format(title))

    # Iterate over the fetched films and print each film's information
    for film in films:
        print("Film Name: {}, Director: {}, Genre: {}, Studio: {}".format(film[0], film[1], film[2], film[3]))

# Call the show_films function
show_films(cursor, "DISPLAYING FILMS")

cursor.close()
