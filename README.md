# Premier-League-Table

A command line tool that can be used to fetch and display the Premier League table at the current time. The program retrieves and displays data from the official Premier League table website (https://www.premierleague.com/tables).

Currently, this implementation only uses web scraping which isn't ideal as the website used could change format. In future, I plan on creating an alternative method of data collection using a football API.

#### Project Aims:
- Create a useful tool to quickly display the real-time Premier League table on the command line.
- Expand Python web scraping ability
- Understand and use of APIs for data collection

#### What I Learned:
- How to work with the requests and beautiful soup modules to perform web scraping
- Initially began learning regular expressions with the regex module, before simplifying my implementation with bs4 instead

-------------------------------------------------------

## Getting Started
Run premierLeagueTable.py to display the current premier league table in the command line. 

#### Optional Arguments
- s or small - displays more compact version of the table
The full size table is displayed as default.

### Prerequisites
Required Python modules:
- requests (re)
- beautiful soup (bs4)
