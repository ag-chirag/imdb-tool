#!usr/bin/env python3
import os
import re

import imdbsearch
def ret_list(file_name):
   file_name = file_name.lower()
   file_name = re.sub(r'[\._\-]'," ",file_name)
   filelist = file_name.split()
   return filelist

def main(target,filters):
  
  print("fetching filename from " + target)
  stopwords = {"xvid","brrip", "xvid", "dvdrip","bdrip","hdrip","axxo","720p", "1080p", "dvd", "unrated","720","1080"}
  #target = argv[0]
  f = open("files.txt","w")
  for root, dirs, files in os.walk(target):
   for file in files:
     if file.endswith(".avi") or file.endswith(".wmv") or file.endswith(".mkv") or file.endswith(".mp4") or file.endswith(".rmvb") or file.endswith(".divx") or file.endswith(".DAT") or file.endswith(".idx") or file.endswith(".flv"):
       #print(file)
       filelist = ret_list(file)
       length = len(filelist) - 1
       if length == 1: 
          if filelist[0] == "sample":
             continue  
          if re.search(r'^[123]',filelist[0]) is not None and len(filelist[0]) == 1:
              file_name = re.search(target+r'/(.*)',root).group(1)
              filelist = ret_list(file_name)
              length = len(filelist)

       for i in range(0,length):
          word = filelist[i]
          word_l = len(word)
          if word[0] =='[' and word[word_l-1] ==']':
             length = i
          match = re.search(r'(.*)\[(.*)\](.*)',word)
          if match is not None:
              filelist[i] = match.group(1)
              word = filelist[i]
          for stop in stopwords:
              pat = r'(.*)'+ stop + r'(.*)'
              match = re.search(pat,word)
              if stop == word:
                 length = i
              if match is not None:
                 filelist[i] = match.group(1)
                 length = i + 1
          
          if re.search(r'cd(.*)',word) is not None:
              length = i
         
       file = ""
       for i in range(0,length):
          file = file + filelist[i]
          if i != length-1: 
            file = file + " "
       #print(file)      
       f.write(file+"\n")

  f.close()
  #searchgoogle.main()  
  imdbsearch.main(filters)       
