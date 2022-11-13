# Python...here we come!

![1_9Yl5cX0C2p1rLZzdq-bwaQ](https://user-images.githubusercontent.com/115101031/201499189-e2a30f97-a10f-4d77-9d1d-b20df82cdf92.png)
####source: https://medium.com/codex/how-to-improve-your-coding-style-and-documentation-with-python-programming-language-d2bb0ad0fedb 

## Why Python?

Python is among the most popular programming languages in the world. As a general purpose language, Python is ideally designed and has applications across a wide range of applications, including data science, software and web development, automation, and generally getting stuff done.

As a tool for complex data analytics, Python can be used to solve a range of problems across many fields, from finance to scientific research. Python allows data analysts to use the language to conduct complex statistical calculations, create data visualizations, build machine learning algorithms, manipulate and analyze data, and complete other data-related tasks.

At its core, Python is often referred to as the glue that holds the data pipeline together. Python can pull data from one place and save it in another, as well as automate a range of tasks.

Fun fact: Did you know? The name Python comes from Monty Python. When Guido van Rossum was creating Python, he was also reading the scripts from BBC’s Monty Python’s Flying Circus. He thought the name Python was appropriately short and slightly mysterious.

SOURCES: 
https://www.coursera.org/articles/what-is-python-used-for-a-beginners-guide-to-using-python
https://www.python.org/doc/essays/omg-darpa-mcc-position/

## Scope of Project

Python is an ideal programming language for the financial industry. Widespread across the investment banking and hedge fund industries, banks are using Python to solve quantitative problems for pricing, trade management, and risk management platforms. Python also seems to have answers to most challenges raised by the financial industry when looking at analytics, regulation, compliance, and data, which are made easy by the abundance of supporting libraries. 

Python is an equally powerful analytical tool, allowing political analysts to sift through a range of different data to analyze and compare electoral results.

In this project, the analysis was two-pronged:
1) Creating a Python script to analyze the financial records of the RubberHose Company. Using a financial dataset outlining profits and loses over a period of months and years, I have created a Python script that analyzes the records to calculate each of the following values:
    * The total number of months included in the dataset
    * The net total amount of "Profit/Losses" over the entire period
    * The changes in "Profit/Losses" over the entire period, and then the average of those changes
    * The greatest increase in profits (date and amount) over the entire period
    * The greatest decrease in profits (date and amount) over the entire period
    
2) In the second prong, I have been tasked with helping a small, rural town modernize its vote-counting process.  Having been provided with a set of poll data, composed of voters (by Voter ID), County, and Candidate. I developed a Python script that analyzes the votes and calculates each of the following values:
    * The total number of votes cast
    * A complete list of candidates who received votes
    * The percentage of votes each candidate won
    * The total number of votes each candidate won
    * The winner of the election based on popular vote

## At first glance

I found Python a much more interactive and user-friendly tool than VBA.  It was easy to access libraries and detailed information on the different functions and modules.  I particularly enjoyed to write and preview the code piece by piece in real time.  This allowed me to resolve errors far more easily as I progressed, and build the logic for the project in a more strategic way than VBA, even though there are some fundamental similarities between them.

The functionality of Python (through VS Code interface and Git) allows for learning in real time, including:
* Navigating to folders on your computer using the command line.
* Reading and extracting data from CSV files (including building pathways to access files).
* Determining the difference between Python data types and performing different actions on them.
* Learning to create data structures using indexed lists, and learning to understand when a list might be a better choice for storing information than a dictionary or a tuple.  
* Creating and using For loops and conditional statements (If, Elseif).
* Writing data to an output file and print the file.
* Overcoming challenges and difficulties encountered, and researching best practices by accessing a huge community online.  This was particularly key when addressing errors in my code.
* Learning Python, reviewing the code, building an error-free, readable, reusable, and efficient script for analysis, while maintaining an open and creative approach to reviewing data.  I continue to push myself to write code always looking for the loophole (ie. lloking for the ways my coding might fail).

![78cbfc3917d9bf65e65d46f84128a2e1](https://user-images.githubusercontent.com/115101031/201499198-a127d470-53ee-45f1-9305-b4f8c2e96cfe.jpeg)

## Observations during coding

Both projects were very different, but each started with similar questions
* Examine the data: how is it organized, what is its nature (string, integer), how does it need to be reorganized
* Decide what data needed to be collected
* Make coding decisions: 
    * Indexing was essential, therefore using lists (instead of dictionaries) to collect data for the purposes of the project (there is a crucial difference between List and Dictionary in Python.)
            ![Difference BTWN Lists   Dictionaries](https://user-images.githubusercontent.com/115101031/201499210-d1a398e0-76ba-458b-bf36-57633b4a3cfa.jpg)
            
    * Make it readable: ensure that when sharing the code, others could understand it
    * Make it reusable: while designed with this data set in mind, it can be used with any size of data set, and in additional contexts.  For example, looking at sales projections by month to determine prime profit period; while the election date was limited to county elections, it can be used for larger elections (ie. provincial).  With minimal effort the code could be easily expanded to include more depth in the data collected.
    * Ensure the run-time is efficient: by controlling the stored variables, the drain on storage and run-time will be minimal.

## Next Steps

I would like to return to this project (and the script) to further explore more ways that it can be enhanced:
* Election Analysis: it might be interesting to expand the code to include county data.  Or, looking for a broader data source, I could analyse demographic data, including how the votes for each candidate skew along political lines (liberal, conservative, labour) or demographic data (such as race, sex, or age), you could easily add these as new columns to the dataset and apply the same decisison and repitition statements that were used for counting and assigning the total winning votes per candidate. I believe the code could even expand to create a map of the source (county) where the votes originated, with census data mapped over.
* Financial Analysis: The code allows for expansion of the analysis.  For example, comparing change over time to understand the business’s most profitable seasons and growth trends. Comparing industry benchmarks and competitors to see if there is potential for you to generate more income. Analyzing areas for more efficiency in your business. Or, looking at rates of return to understand what is generating the most income, or uncovering areas for improvement.
