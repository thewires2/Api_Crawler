# Api Crawler

## 1) Steps to run the code 

1) Download the code as a zip file and extract the folder . Open it with any code editor.

2) Create a virtual enviornment using pipenv or virtualenv and run the command ```$ pip install -r requirements.txt``` in the directory to install all the required dependencies 

3) Use the command ```python manage.py migrate``` to create all the database tables and then ```python manage.py runserver 8080``` to run it on your localhost

4) Goto [http://127.0.0.1:8080/](http://127.0.0.1:8080/) to see the list of categories Api's and [http://127.0.0.1:8080/category](http://127.0.0.1:8080/category) to see all the Api's 
> Since the API is rate limited to 10 requests per user per minute it takes around 10 minutes to populate the entire database the first time you visit the Category section

---

2) Details of all the tables and their schema

There are two tables in this project:

1) Categories

This is a simple table which just one column storing all the 45 categories of different API's 

SCHEMA:

[Schema](https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&title=daa.png#R3ZZdb5swFIZ%2FDZeV%2BMhHdwk07aZpSbVUmnrpgAErxmbGDLJfvwM2H06I1k7NzW4i%2B7E55%2Fg9LyaWF%2BbNk0BF9o3HmFquHTeW92C57tr14LcFJwUWtqtAKkiskDOCPfmNNbQ1rUiMS2Oj5JxKUpgw4ozhSBoMCcFrc1vCqZm1QCm%2BAPsI0Uv6g8QyU%2FR%2BaY%2F8MyZp1md2bL2So36zBmWGYl5PkLexvFBwLtUob0JMW%2B16XdRzj1dWh8IEZvItD7Ddbvv4tUpetzL2Q%2FZyrNf7Ox3lF6KVPrAuVp56BeqMSLwvUNTOa2iy5QWZzCnMHBiislC6J6TBkCrQEbGQuLlaqjMIAMbBPMdSnGCLfsDt5dWmudfTeuyAs9Asm6rfQ6S7ng6hR2FgoLV5h06Lv%2BtECYNRUErBj4NXFqZYBRYECsIC5gcUHQ%2Bc4eeRBQUnTHa1LwNr%2BQCEV7INHA72tm8jseO%2BVeNbSbyakXhFIWtwgEEqu3MrkHA45FT81c%2BK9wt3ZXeJ%2BLABBGnGxT5K6L9snnbfX%2FtoUK0KaCYBPEl81mwQXpqtVX0POeVtcxnvzJAQSs8QoiRlMI2gUV3P2zYSuHB8vZCTOG7TBHMvnuAVi9vX7KN84NmmDz5d2mDOBe6tXLC%2B6oKKnneIknPyz05xVnNO8Z%2B%2FwNoW5fhdXhnYZYEAp%2Bf4X10FtjJvl%2BXM7eJ9jK9gOn5Eu7XJPxFv8wc%3D)


STEPS TO RECREATE THE CATEGORY TABLE:
 
**Since Django autogenerates the migration's for the creation of the tables, there in no explicit creation of the tables.** However if we wanted to create the table manually the sql command is given below

```CREATE TABLE "crawler_category" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL)```

2) Sub-Categories

This is a table which is used for storing the different kind's of API'S with the detail's supplied the API'S call

SCHEMA:

[Schema](https://viewer.diagrams.net/?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Subcategory.png#R7Zhdk5owFIZ%2FDZc7w4dS91LYbe3XdmfcttcRImQMCQ2hYH99DxC%2BdXZ16%2Bp0vHGS94Sc5D0PUaNZbpR%2FECgOv3IfU83U%2FVyz7jTTnNkz%2BCyEbSVMZmYlBIL4lWS0wpL8wUrUlZoSHye9gZJzKkncFz3OGPZkT0NC8Kw%2FbM1pP2uMAjwSlh6iY%2FUn8WWotjXVW32BSRDWmQ1dRSJUD1ZCEiKfZx3JutcsV3Auq1aUu5gW3tW%2BVM%2B93xNtFiYwky95wMx%2FuMln28vi9MHIv%2BWfvpPFjZrlN6Kp2rBarNzWDmQhkXgZI6%2FoZ1BkzXJCGVHoGdBESVz5viY5hlSOmhELifO9SzUaAwAczCMsxRaGqAfM2l4FzUx1s7YCVu1z2HG%2FEZGqetBM3RoDDeXNAT6Zz%2FtECYOWk0jBNw0rk75ZMRYEFoQF9FfI26w4w4%2Bt5sScMFmufepo0ztQeCqLid0Gb%2F00FhvmCz02TmWxtcNim0JWZwWNQJb7roQ1h012zbd%2FpbwO3CTlITKHAWBI3gbrWZZpMSGKCpDZKonLkO4iiQNe7KPKAXuo0vRTg9xZzgABKIfsF7yiweWUFyVnvERkTSgdSIiSgEHXg%2FKVJBTFJXAMzVUgIr5fpHF2vY6Cp8wvXr5%2FRsdtn47bMRzNudaFwzwVHJO9cKR0WCJKhsrRABn2LoDmjx8h9oAifBAsjTZeIIjdffy3WFmDQ2c65sqw3pKr6UVxlYIJV6IOIsoYELXjp8LbEmVfElGLp6fH5RWpw5Ay%2B0g1iJ0NqdmrkEpixI4naASmy0XyDDpVxitR%2Bw4pc3JuouoFXcYp9YWwzfWQeh1S786O1K6rhLMhddS%2FuStWw%2B%2B%2B5gbgBFhBt738KmOdG0Tr%2Fi8%3D)

STEPS TO RECREATE THE SUB-CATEGORY TABLE:

**Since Django autogenerates the migration's for the creation of the tables, there in no explicit creation of the tables.** However if we wanted to create the table manually the sql command is given below

```CREATE TABLE "crawler_subcategory" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "Api" varchar(500) NOT NULL, "Description" varchar(500) NOT NULL, "Auth" varchar(500) NOT NULL, "Link" varchar(100) NOT NULL, "Category" varchar(100) NOT NULL, "Cors" varchar(100) NOT NULL, "HTTPS" varchar(500) NOT NULL)```


---

3)Points to achieve

1. OOPS

The project follows the core- concepts of OOP's like encapsulation and data abstraction

2. Support for handling authentication requirements & token expiration of server

This is done by regenerating the bearer token after every 5 minutes until all the data is generated.

3. Support for pagination to get all data

Pagination is fully supported for both the API's lists and Categories

4. Develop work around for rate limited server

The workaround for the rate limited server is filled by using time delay's

5. Crawled all API entries for all categories and stored it in a database

This was also successfully implemented


---

What is not done from “Points to achieve”.

Done all the tasks in Points to Achieve


---

What would you improve if given more days

Given more time i would have done the following tasks

1) Create a more interactive UI for the project

2) More robust error handling and following best practices for code

3) Containerize the application with Docker


