import mysql.connector

db = mysql.connector.connect(
    host = "127.0.0.1",
    user = "movies_user",
    password = "popcorn",
    database = "movies"
)

cursor = db.cursor()


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

# Define the film details
film_name = "Iron Man"
film_releaseDate = "2008"
film_runtime = 126
film_director = "Jon Favreau"
studio_id = 1  
genre_id = 2   

# Execute the SQL INSERT statement
cursor.execute("INSERT INTO film (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) VALUES (%s, %s, %s, %s, %s, %s)", (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id))

# Commit the transaction
db.commit()

# Call the show_films function to display the inserted film
show_films(cursor, "DISPLAYING FILMS AFTER INSERTING 'Iron Man'")

# Execute the SQL UPDATE statement to classify "Alien" as a Horror film
cursor.execute("UPDATE film SET genre_id = (SELECT genre_id FROM genre WHERE genre_name = 'Horror') WHERE film_name = 'Alien'")

# Commit the transaction
db.commit()

# Call the show_films function to display the updated film
show_films(cursor, "DISPLAYING FILMS AFTER UPDATING 'Alien'")

# Execute the SQL DELETE statement to remove the movie "Gladiator"
cursor.execute("DELETE FROM film WHERE film_name = 'Gladiator'")

# Commit the transaction
db.commit()

# Call the show_films function to display the films after deletion
show_films(cursor, "DISPLAYING FILMS AFTER DELETING 'Gladiator'")

cursor.execute("DELETE FROM film WHERE film_name = 'Inception'")

db.commit()

show_films(cursor, "DISPLAYING FILMS AFTER DELETING 'Gladiator'")
cursor.close()