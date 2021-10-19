## A small project that I did as part of the recruitment stage.

### This website is simple api designed by me

### Methods:

#### GET /books

This method is showing you all the records that exists in database
You can params like author=value to filter scores showing only authors with names that match the value.
You can also use it like chain ?author=name1&author=name2, and it basically shows records for both values.
Also You can sort by published_date using query param sort=-published_date


#### GET/books/<BookUniqueID>

This method is showing only one record if it matches unique id that exists in database

#### POST db

Use this method to post data to database. You have to give one param at the time which is q=value.
This method is basically scraping data from certain google api that contains information about books.
If records with certain id exists in database, then it is updating it.

### Live site [Link](https://books-api-recruitment.herokuapp.com/books)