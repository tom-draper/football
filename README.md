# Premier-League-Table

### Eductional Project  
I begain this project to find a method to obtain the premier league table data values with real time accuracy. After reading Automate The Boring Stuff With Python by Al Sweigart, I wanted to create a project that used web scraping. Initially another main target of this project was to learn about and make use of regular expressions when extracting data from the HTML. However, after more research I found the use of the Beautiful Soup module was more reliable and suitable for this purpose and therefore changed my implemenation.

#### Project Aims:
- Extract data from the web
- Research regular expressions.
- Apply regular expressions with the RegEx module.
- Better understand effective object oriented programming in Python.
- Further understand dictionaries.

#### What I Learned:
- Basics of regular expressions.
- How to create regular expressions using the re module.
- How to retrieve a webpage using the requests module.
- Basic HTML structure.
- Creating dictionaries with unique key values in a for loop.
- How to use the BeautifulSoup module to extract specific HTML values.

In future, I could extend this project to graph the points of each premier league team across the season to become more familiarised with the matplotlib Python module. During this project, once I had implemented a working solution using regular expressions, I found that the use of the Beautiful Soup module would be a better alternative. After implementing a solution using Beautiful Soup, I found it to be a much cleaner solution and replaced my regular expressions solution with it.

-------------------------------------------------------

### Hot to use:
Running premier_league_table.py will display the current premier league table in the command line. The full table is displayed as default. Entering argument "small" or "s" will display a small version of the table.  

The program requests for the html from the official Premier League tables website (https://www.premierleague.com/tables). Using regular expressions, the first 20 teams mentioned and corresponding table values are searched for and stored in lists which are then used to later instantiate 20 team objects are then built using these values extracted. The Premier League table can then be displayed using the data stored in each team object.

