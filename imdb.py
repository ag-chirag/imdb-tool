#!usr/bin/env python3
import getfiles
import sys
if __name__ == "__main__":
   filters = dict()   
   if len(sys.argv) > 2:
     i = iter(sys.argv[2:])
     filters = dict(zip(i, i))
   if '-r' not in filters:
     filters['-r'] = 0.0
   if '-g' not in filters:
     filters['-g'] = None
   if '-y' not in filters:
     filters['-y'] = 0
   if '-l' not in filters:
     filters['-l'] = 0

   getfiles.main(sys.argv[1],filters)
