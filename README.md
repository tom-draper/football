# Premier-League-Table

A command line tool that can be used to fetch and display the Premier League table at the current time. The program retrieves and displays data from the official Premier League table website (https://www.premierleague.com/tables).

Currently implementation uses web scraping which isn't ideal as the website used could change format. I plan on switching to use of an API in future. 

-------------------------------------------------------

## Getting Started
Run premierLeagueTable.py to display the current premier league table in the command line. 

#### Optional Arguments
- s or small - displays more compact version of the table
The full size table is displayed as default.

### Prerequisites
Required Python modules:
- requests
- beautiful soup (bs4)
