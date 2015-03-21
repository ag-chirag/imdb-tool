#!usr/bin/env pyhton3

import urllib.request
import re

def printinfo(f,name,length,genre,rating,year,desc):
   f.write("Name : " + name + "\n")
   f.write("Length : " + str(length) +" mins" + "\n")
   for i in range(0,len(genre)): 
     f.write("Genre : " + genre[i] + "\n")
   f.write("Rating : " + str(rating) + "\n")
   f.write("Year : " + str(year) + "\n")
   f.write("Description : " + desc + "\n")
   f.write("***********************************************************************************************************************\n")

def main(link,minLen,minYear,minRate,reqGen):
  #for line in open('links.txt'):
  #  link = line.rstrip('\n')
    res = urllib.request.urlopen(link)
    html = res.read()
    res_string = html.decode("utf-8")
    f = open("imdb.txt","a")  
    match = re.search(r'itemprop="name">(.*)</span>', res_string)
    if match is not None:
      name = match.group(1)
    else:
      name = "Not Found"
    match = re.search(r'>(.*) min</time>', res_string)
    if match is not None:
      length = int(match.group(1))
    else:
      length = 0
    genre = []
    while match is not None:
      match = re.search(r'itemprop="genre">(.*)</span>', res_string)
      if match is not None:
        genre.append(match.group(1))
        res_string = re.sub(r'itemprop="genre">(.*)</span>',"visitedbyme",res_string,1)

    match = re.search(r'class="titlePageSprite star-box-giga-star"> (.*)</div>',res_string)
    if match is not None:
      rating = float(match.group(1))
    else:
      rating = 0.0
    yearlist = [] 
   # match = re.search(r'<span class="nobr">\((.*)\)</span>',res_string)
    match = re.search(r'<a href="/year/(.*)/',res_string)
    if match is not None:
      year = int(match.group(1))
    else:
      year = 0

    match = re.search(r'<p itemprop="description">\n(.*)</p>',res_string)
    if match is not None:
     desc = match.group(1)
    else:
      desc = "Not Found"
    if int(minLen) <= length and float(minRate) <= rating and int(minYear) <= year:
      if reqGen is not None:
         for gen in genre:
            if reqGen == gen:
                printinfo(f,name,length,genre,rating,year,desc) 
      else:
        printinfo(f,name,length,genre,rating,year,desc)
    f.close()
