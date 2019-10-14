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
Something I found during this project is that the Requests module doesn't always return the HTML in the same format as my browser did. After research I found this to be because the Requests module returns the HTML before the Javascript has run. It appears the Premier League website includes a lot of Javascript. This meant that during the extracting of table values I had to use less eloquent solutions. For example, the \<table> html tag appeard to contain the full Premier League table in my browser, but found to only contain the first row of the table when returned from requests.get. This forced me to use the table row <tr> tag to access all of the table row values. As there were also Premier League tables from previous seasons on this webpage, my list of table rows contains more than just this Premier League season, and I had to slice this list and to get only the first 20 rows found on the page. To avoid this in future I could use the Selenium browser automation module instead as it can load the page and evaluate any Javascript before retrieving the content.

-------------------------------------------------------

### How to use:
Running premier_league_table.py will display the current premier league table in the command line. The full table is displayed as default. Entering argument "small" or "s" will display a small version of the table.  
The program requests and displays data from the official Premier League table website (https://www.premierleague.com/tables).

