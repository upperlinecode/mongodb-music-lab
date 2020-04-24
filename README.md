# MongoDB Music Lab

> Estimated time: 2-3h

In this lab, students will practice working with their MongoDB by creating a new database to collect their favorite music. They will then interact with the database by creating several new Flask routes and any associated HTML templates necessary for displaying data from the database. Some starter code is provided to help with the initial setup and configuration.

## Getting Started

This lab assumes that students:

- Are comfortable using Flask, writing Flask routes, and building HTML templates.
- Have already set up a free Atlas account on MongoDB and are familiar with the MongoDB dashboard.

## Instructions

1. In the MongoDB dashboard, create a new user that can read and write to any database.

	> Make a note of the username and password for this account.

2. In the MongoDB dashboard, create another new user that can only read any database.

3. In the MongoDB dashboard, create a new database that will store data about your musical preferences.

4. Update `app.py` with:
	- the name of the new database,
	- the URI of your MongoDB to connect,
	- a message for the `index()` route.

5. Create a new route for `/add` that uses the `.insert()` method to add the data below to a collection called `songs` in your new database. Then return a message to the user to let them know the song has been added.

	`{"song":"Uptown Funk"}`

	> Use the MongoDB dashboard to check that the route adds the data to the correct collection in your database before moving on.

6. Use the `/add` route to add a new song to the collection, but also include:
	- the `song` title
	- the name of the `artist`
	- a `description` of why you like the song.

7. Use the `/add` route to add 5 more of your favorite songs to the database.

8. Use the MongoDB dashboard to delete the "Row, Row, Row Your Boat" document from your collection.

9. Create a new route that shows a list of all of the song titles in your collection.

	> Hint: Break down the steps needed to accomplish this:
	> 1. Find all of the entries in a collection
	> 2. Pass the result as a variable to an HTML template
	> 3. Loop over the variable in the template to build the list

10. Update your HTML template to include the name of the artist for each song, too.

11. Update the route method to show the songs in alphabetical order by the name of the song.

12. Update the route method to show the songs in alphabetical order by the name of the artist.

13. Update the route method to show just the first three songs when ordered alphabetically by artist.

## Stretch

14. Create a new HTML template that is a form for a user to submit their favorite songs to the list. Make sure there is a way for the user to include the song title, artist, and a description of why they like that song.

15. Create a new route that has two parts:
	- a `GET` request that renders the template you made above.
	- a `POST` request that gets the data from the form, adds it to the database, and then lets the user know the data was properly submitted.

There are several ways to do this so there's no one right answer.

## Double Stretch

16. Create a new HTML template and route that will show all songs matching an artist's name: e.g. `/artist/<name>`.

17. Update the HTML template showing all songs to make each artist's name a hyperlink which shows all songs by that artist.

## Triple Stretch

18. Create a new HTML template and route that will show a song based on the unique identifier, `_id`, that is assigned by MongoDB: e.g. `/song/<_id>`. Each song-specific page should also show the user-submitted description of the song.

	> You may have to search for PyMongo methods to work with the `_id` in MongoDB; it is a new data type called an `ObjectId`.

19. Update the HTML template showing all songs to make each song a hyperlink that shows the song-specific page.
