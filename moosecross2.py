

# A small Python app to do crosstabs. 

# This code is released to the public domain. 
# "Share and enjoy..."  :)    

# Acknowledgements - The crosstab code was done with help from 
# Peter Sutton - http://uompeter.blogspot.com/ 
# Many thanks, Peter!   

import itertools, csv, sys, types 
from types import *   
import curses, curses.ascii 
import time


class crosstab(object):  
   def summarise(self, csv_path, has_header_row=True):
       with open(csv_path) as csv_file:
           csv_data = list(csv.reader(csv_file))[1 if has_header_row else 0:]
       self.summary = {} 
                   
       for region, colour, count in csv_data:    
           # Create keys - one for rows, the other for columns. 
           rowkey = region 
           colkey = colour 
           # Combine the keys to summarise the data
           mykey = (rowkey, colkey)            
           if self.summary.has_key(mykey):  
              self.summary[mykey] += int(count)                    
           else:
              self.summary.update({(mykey): int(count)} )        
       return self.summary

   def display(self):
       for item in self.summary.items():
           print item 

#  Run the code 
a = crosstab() 
a.summarise("testdata.csv") 
#a.display() 


#  Setup the curses window  
stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

try:

    # Column headings 
    colheads = list(chr(x) for x in range(65,70))     
    poslist = list( (y,x) for y in range(2, 3) for 
           x in range(7, 50, 7) )    
    for x,y in zip(colheads, poslist): 
        stdscr.addstr(y[0], y[1], str(x), curses.A_STANDOUT )                    
        stdscr.refresh() 	
       
    # Row headings     
    rowheads = list(range(1,11))      
    poslist = list( (y,x) for y in range(3, 15) for 
           x in range(0, 1) )  
    for x,y in zip(rowheads, poslist): 
        stdscr.addstr(y[0], y[1], str(x), curses.A_STANDOUT )                          
        stdscr.refresh()   
    
    
    #  We do keyhandling here.   
    while (1): 
       c=stdscr.getch()	
       if c==curses.KEY_F2:  
          stdscr.move(7, 20)
          (y, x) = stdscr.getyx()                      
          stdscr.addstr(y, x, "Hi there!" )                          
          stdscr.refresh() 
       # Ctrl-G quits the app                  
       elif c==curses.ascii.BEL: 
          break      
       
       
finally:
    curses.nocbreak()
    stdscr.keypad(0)
    curses.echo()
    curses.endwin()


