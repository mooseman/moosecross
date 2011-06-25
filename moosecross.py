

# A small Python app to do crosstabs. 

# This code is released to the public domain. 
# "Share and enjoy..."  :)    

# Acknowledgements - The crosstab class was done with help from 
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

# Expand this to print col headings, row headings and 
# data separately (using position lists for each). 
def puttable(y, x, table):    
   # Col headings 
   stdscr.move(1, 15) 
   (y, x) = stdscr.getyx()                          
   stdscr.addstr(y, x, "Moosecross - Type Ctrl-G to quit...", curses.A_NORMAL )     
   stdscr.move(3, 15) 
   (y, x) = stdscr.getyx()                          
   for key in table.summary.keys():     
      stdscr.addstr(y, x, str(key[1]), curses.A_NORMAL )     
      x += 5                     
      stdscr.refresh() 
   
   # Row headings 
   stdscr.move(5, 3) 
   (y, x) = stdscr.getyx()                          
   for key in table.summary.keys():     
      stdscr.addstr(y, x, str(key[0]), curses.A_NORMAL )     
      y += 1                     
      stdscr.refresh() 
   
   # Data 
   stdscr.move(5, 15) 
   (y, x) = stdscr.getyx()                          
   for val in table.summary.values():     
      stdscr.addstr(y, x, str(val), curses.A_NORMAL )     
      x += 5                     
      stdscr.refresh() 


try:

    # Print data 
    stdscr.move(3, 5) 
    (y, x) = stdscr.getyx()                      
    puttable(y, x, a)  
    
    
    #  We do keyhandling here.   
    while (1): 
       c=stdscr.getch()	
       if c==curses.KEY_F2:  
          stdscr.move(10, 20)
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


