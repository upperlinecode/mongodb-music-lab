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

4. Update `routes.py` with:
	- the name of the new database,
	- the URI of your MongoDB to connect,
	- a message for the `index()` route.

5. Create a new route for `/add` that uses the `.insert()` method to add the data below to a collection called `songs` in your new database. Then return a message to the user to let them know the song has been added.

```json
{"song":"Row, Row, Row Your Boat"}
```

	> Check that the route adds the data to the correct collection in your database before moving on.

6. Use the `/add` route to add a new song to the collection, but also include the name of the artist along with the song title.

7. Use the `/add` route to add 5 more of your favorite songs to the database.

8. Use the MongoDB dashboard to delete the "Row, Row, Row Your Boat" document from your collection.

9. Create a new route that shows a list of all songs in your collection.

	> Hint: Break down the steps needed to accomplish this:
	> - Find all of the entries in a collection
	> - Pass the result as a variable to an HTML template
	> - Loop over the variable in the template to build the list

10. 


