

# A small Python app to do crosstabs. 

# This code is released to the public domain. 

# Acknowledgements - This code was done with much help from 
# Peter Sutton - http://uompeter.blogspot.com/ 
# Many thanks, Peter!   


import csv, sys 

class crosstab(object):  

   def init(self): 
      self.data = None 

   def summarise(self, csv_path, has_header_row=True):
       with open(csv_path) as csv_file:
           csv_data = list(csv.reader(csv_file))[1 if has_header_row else 0:]
       self.summary = {}
       for region, colour, count in csv_data:
           count = int(count)
           if region in self.summary:
               if colour in self.summary[region]:
                   self.summary[region][colour] += count
               else:
                   self.summary[region][colour] = count
           else:
               self.summary[region] = {colour: count}  
       self.data = self.summary                
       return self.summary


   def display(self):
       for region, colour_count in self.summary.items():
           print(region)
           for colour, count in colour_count.items():
               print("    {0}: {1:d}".format(colour, count))


#  Run the code 
a = crosstab() 
a.init() 
a.summarise("testdata.csv") 
a.display() 

 
 
	
	

