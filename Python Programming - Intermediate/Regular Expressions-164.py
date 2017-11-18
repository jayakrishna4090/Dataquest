## 1. Introduction ##

strings = ["data science", "big data", "metadata"]
regex = "data"

## 2. Wildcards in Regular Expressions ##

strings = ["bat", "robotics", "megabyte"]
regex = "b.t"

## 3. Searching the Beginnings And Endings Of Strings ##

strings = ["better not put too much", "butter in the", "batter"]
bad_string = "We also wouldn't want it to be bitter"
regex = "^b.tter"

## 5. Reading and Printing the Data Set ##

import csv
posts_with_header=list(csv.reader(open("askreddit_2015.csv",'r')))
posts=posts_with_header[1:]
for each in posts[:10]:
    print(each)
#    each.split(",")
    

## 6. Counting Simple Matches in the Data Set with re() ##

import re

of_reddit_count = 0
for each in posts:
    pat=each[0]
    if re.search("of Reddit",pat) is not None:
        of_reddit_count+=1
   

## 7. Using Square Brackets to Match Multiple Characters ##

import re

of_reddit_count = 0
for each in posts:
    pat=each[0]
    if re.search("of [rR]eddit",pat) is not None:
        of_reddit_count+=1
  

## 8. Escaping Special Characters ##

import re

serious_count = 0
for row in posts:        
    if re.search("\[Serious\]", row[0]) is not None:
        serious_count += 1

## 9. Combining Escaped Characters and Multiple Matches ##

import re

serious_count = 0
for row in posts:
    if re.search("\[[sS]erious\]", row[0]) is not None:
        serious_count += 1

## 10. Adding More Complexity to Your Regular Expression ##

import re

serious_count = 0
for row in posts:
    if re.search("[\[\(][Ss]erious[\]\)]", row[0]) is not None:
        serious_count += 1

## 11. Combining Multiple Regular Expressions ##

import re

serious_start_count = 0
serious_end_count = 0
serious_count_final = 0
for row in posts:
    if re.search("^[\[\(][Ss]erious[\]\)]", row[0]) is not None:
        serious_start_count+=1
for row in posts:        
    if re.search("[\[\(][Ss]erious[\]\)]$", row[0]) is not None:
        serious_end_count+=1
for row in posts:        
    if re.search("^[\[\(][Ss]erious[\]\)]|[\[\(][Ss]erious[\]\)]$", row[0]) is not None:
        serious_count_final+=1        

## 12. Using Regular Expressions to Substitute Strings ##

import re
for row in posts:        
    row[0]=re.sub("[\[\(][Ss]erious[\]\)]","[Serious]", row[0])
    print(row[0])

## 13. Matching Years with Regular Expressions ##

import re

year_strings = []
for row in strings:
    if re.search("[1-2][0-9][0-9][0-9]",row) is not None:
        year_strings.append(row)

## 14. Repeating Characters in Regular Expressions ##

import re

year_strings = []
for row in strings:
    if re.search("[1-2][0-9]{3}",row) is not None:
        year_strings.append(row)

## 15. Challenge: Extracting all Years ##

import re
"""year_strings = []
years=[]
for row in strings:
    if re.search("[1-2][0-9]{3}",row) is not None:
        year_strings.append(row)
        years.append(re.findall("[1-2][0-9]{3}",row))
for year in year_strings:
    a=re.findall("[1-2][0-9]{3}",year)
    years.append(a)
#print(year_strings)
"""
years = re.findall("[1-2][0-9]{3}", years_string)
print(years)