

# A small Python app to do crosstabs. 

# This code is released to the public domain. 

# Acknowledgements - This code was done with help from 
# Peter Sutton - http://uompeter.blogspot.com/ 
# Many thanks, Peter!   

import itertools, csv, sys, types 
from types import *   
 
# See if we can use zip or iproduct to make the crosstab a bit more 
# elegant.   
 
class crosstab(object):  
   def summarise(self, csv_path, has_header_row=True):
       with open(csv_path) as csv_file:
           csv_data = list(csv.reader(csv_file))[1 if has_header_row else 0:]
       self.summary = {} 
                   
       for region, colour, count in csv_data:    
           # Create a composite key 
           mykey = (region, colour)           
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
a.display() 



 
 
	
	

