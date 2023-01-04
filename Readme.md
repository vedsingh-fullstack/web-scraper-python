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

 `docker-compose up`

 ## TODO

 - Adding unit test
 - Adding scheduler for scraping
 - Deployment to heroku or AWS or kubernetes 
 
 
 ## Suggestions or Improvments

 # Regarding web scraper job
 - Routes the request with proxy to be protected from getting blocked by target website hitting with same IP
 - Caching to avoid hitting unnecessary requests if its static website and content do not change more often. We can cache the HTTP request and response and write it to file.
 - Scrape data at off-peak hours
