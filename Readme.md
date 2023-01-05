### Sample Web Scraping and Fast api project.

## Table of Contents
- [Tasks](#tasks)
- [How To Run the Project](#how-to-run-the-project)
- [TODO](#todo)
- [Suggestions or Improvments](#suggestion)


## Tasks
- Build the script to scrap static website
- scrape the data from the website and load it into the database (Mongo DB)
- Build the API using fast api to get this data 
- Support query-parameters to the endpoint
- Containerize the whole application with Dockerfiles
- structured codebase by following the separation of concern design principle

## How To Run the Project
 Run the whole application by running below command,  

 `docker-compose up`

 Visit http://localhost:5001/docs for swagger documentation and testing the api.
 Use MongoDB compass to access mongo db or using mongo cli by using below command, 

  `docker exec -it mongodb bash`
  and then loggin in using user and password
  `mongo -u root -p example`


 ## TODO

 - Moving the db operation from `scraper/catalogue_service.py` -> `save_catalgoue` method to sepearte service to remove dependency of database which makes easier to unit test. 
 - Moving out the execute_job logic out of scraper/main file. 
 - Adding unit test around services. 
 - Adding scheduler for scraping
 - Deployment to heroku or AWS or kubernetes 
 
 
 ## Suggestions or Improvments

 # Regarding web scraper job
 - Routes the request with proxy to be protected from getting blocked by target website hitting with same IP
 - Caching to avoid hitting unnecessary requests if its static website and content do not change more often. We can cache the HTTP request and response and write it to file.
 - Scrape data at off-peak hours
