#!usr/bin/env python3
import urllib.request
import urllib.parse
import re
import json as m_json
import scrapper
def main(filters):
  f = open("imdb.txt","w")
  f.truncate()
  f.close()
  minRate = filters['-r']
  minYear = filters['-y']
  minLen = filters['-l']
  reqGen = filters['-g']
  for line in open('files.txt'):
    movie = line.rstrip('\n')
    query = movie 
    print("Fetching " + movie)
    imdb = 'http://www.imdb.com/find?'
    query = urllib.parse.urlencode({'q' : query})
    res = urllib.request.urlopen(imdb + query).read().decode("utf-8")
    base = 'http://www.imdb.com/title/'
    match = re.search(r"/title/([^/]*)",res)
    if match is not None:
       scrapper.main(base + match.group(1) +'/',minLen,minYear,minRate,reqGen)
    else:
       print ("Not Found Link: "+ imdb+query)
       print ("*****************************************************************************************************************\n")
