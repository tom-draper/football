# Premier-League-Table

### Eductional Project  
I begain this project to find a method to obtain the premier league table data values with real time accuracy. After research, I  then aimed to get a better understanding of web scraping & HTML format, object oriented programming in Python, as well as getting a better grasp at dictionaries. Another main target of this project was to learn about and make use of regular expressions as they would be necessary for how I planned to tackle this project.

Project Aims:
- Extract data from the web
- Research regular expressions.
- Apply regular expressions with the RegEx module.
- Better understand object oriented programming in Python.
- Understand more advanced dictionaries.

What I Learned:
- Basics of regular expressions.
- How to create regular expressions using the re module.
- How to request a website using the requests module.
- Basic HTML structure.
- Creating dictionaries with unique key values in a for loop.

In future, I aim to extend this project to graph the points of each premier league team across the season to become more familiarised with the matplotlib Python module. I could learn how I could use an API to extract the same table data.

-------------------------------------------------------

Running premier_league_table.py will display the current premier league table in the command line. The program requests for the html from the official Premier League tables website (https://www.premierleague.com/tables). Using regular expressions, the first 20 teams mentioned and corresponding table values are searched for and stored in lists which are then used to later instantiate 20 team objects are then built using these values extracted. The Premier League table can then be displayed using the data stored in each team object.

