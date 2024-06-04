# About
In this repo I've built an operational database for an ecommerce platform, using popular tech-shop "Komplett.no" as a reference. 
The database contains real product data scraped from komplett, as well as other generated data for table population.
Finally I've built a data warehouse using a star schema approach, used for doing BI analysis.

The project will be updated continously. This is not it's final form.

![Alt Text](https://github.com/mats-bb/Reverse-engineered-Komplett-DB/blob/master/imgs/overview_1.png)


# Table of contents
- [The idea](#the-idea)
- [The process](#the-process)
  - [1. Exploring the website]()
  - 2. Building the ERD
  - 3. Building the operational dabase
  - 4. Scraping the data
  - 5. Generating operations data
  - 6. Transform and load operations data
  - 7. Building the data warehouse
  - 8. Generating dwh data
  - 9. Extract, transform and load dwh data
  - 10. Power Bi
  - 11. Final words
- [Tools](#tools)
- [Future work](#future-work)


# The idea
The idea for this project came to be because I wanted to dig deeper into data modeling. Typically you'd be given a set of instructions on what data processes the system will handle. In order to get some "instructions" for the project, I decided to use a website I know and love for inspiration, popular webshop, Komplett.no.
From there the idea only grew. I wanted to build the actual system itself and populate it with real data, hence the web scraping. Of course, I needed a data warehouse too, on which I would run analysis. I concluded the project would provide a good foundation for future learning, that I could add new functionalities as I learn about new technologies. A good part of the groundwork has been done in this current iteration of the project, and I will detail it all, step by step.

# The process
## 1. Exploring the website
In order to get the required instructions for building the data model, some exploration was needed. I clicked around on the webpage, checking out the different categories and products, different functions like the shoppingcart and wishlist, customer pages and more. After getting a good overview of the core functions I wanted the system to support I could start the actual modeling.

## 2. Building the ERD
At the heart of every webshop is the products they offer. Customers buy the products, and everything gets recorded in an order. I decided to focus on these aspects for the data model as they are the most "important", and most fun to work with, in my opinion. The process itself was pretty straightforward: explore each aspect in depth, break them down into logical pieces, build the tables and relations, and iterate. Some data, of course, is not avaiable by just looking at a webpage, so some actual thinking was involved in designing parts of the schema, like the product inventory table, for example. You can see the current ERD [here](imgs/operations_ERD.drawio.png).

## 3. Building the operational database
There is not very much to say about the actual creation of the database. The ERD is complete, just follow the recipe. The [DDL](sql/operations_DDL.sql) for the operations database. Don't worry about the cascades, I've deliberately kept them as they were a part of the process. Do be careful in a real environment though!

## 4. Scraping the data
The data scraping process was way more involved, using browser dev tools to inspect the HTML of each webpage to get the actual data. Product data was the target here, and I chose to focus on computer parts only. The process simply described, extract the URL for each product and extract the relevant data from these URLs HTML. This was a lengthy process, and a lot of debugging and manual labour had to be done finding the correct HTML elements and writing the actual code for it. Ultimately though, scraping the data would be a one-time operation.

## 5. Generating operations data
Next I needed some data for the customers and their orders. I will not go too much into detail here, but simply put, I used an [API](https://randomuser.me/) to generate the actual customer data, and some basic Python to generate the rest. See the code for more information.

## 6. Transform and load operations data
The data has been retrieved and generated! The next step is to transform the data into the correct format for loading into the operations database. The process involved some error handling, selecting only the necessary data and some small transformations for the products. The user data needed to be combined. Seeing as both products and customers have multiple tables associated with them, stored procedures had to be written for these operations. You can see them [here](sql/operattions_procedures.sql)!

## 7. Building the data warehouse
All the operations data has been loaded and verified to behave the way it's supposed to. Time to construct the data warehouse. I wanted the warehouse to be easy to use and understand, but also be powerful. A star schema was used, and the decided granularity of the data would be individual product sales lines(from an order). The challenge was to come up with good dimensions for the schema, and make sure they and the facts made sense together. Good naming and several attributes went into the dimensions to ensure high usability. Take a look at the ERD [here](imgs/dwh_ERD.drawio.png).

## 8. Generating dwh data
For every business transaction one thing is always present: a date/time element. For deeper analysis, having several attributes for a given date is very helpful. For example, is it a regular weekday or weekend? Holiday? Which day of the week produces most orders? Month? Much insight can be extracted from a simple date. 

## 9. Extract, transform and load dwh data
We're almost there! As with the operations database, we now have all the generated data we need. Next, I had to extract the relevant data from the operations database, do some price transformations for the products, and load everything into the warehouse. 

## 10. Power Bi
The last step, data analysis in Power Bi! All the data is in place, everything works. Finally, I connected Power Bi directly to the data warehouse. "Users" are free to do whatever analysis they want. The warehouse would be available to all departments as a single source of truth. You can see an example dashboard at the beginning of this repo. I will create more reports/dashboards at a later date to demonstrate other usecases for the warehouse.

## 11. Final words


## Ideas
- Build operational database
- Build dimensional data warehouse
- Scrape product data
- Generate dummy data
- Write ETL processes
- Do analysis with Power Bi

## Tools
- Python
- Dbeaver (postgreSQL)
- Power Bi
- Draw.io (ERD design)
- APIs (https://randomuser.me/)

## Future work
- Scrape all product data
- Generate more sales data for deeper analysis
- Implement big data tools (Kafka, Spark)
- Automate with Airflow
- Migrate to Snowflake
- Build a GUI or web solution to interact with DBs
