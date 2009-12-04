

#  newcross.py 
#  A simple class to read a csv file and do crosstabs. 

import csv, sys, curses.ascii  

class crosstab(object): 
   def init(self): 
      self.data = [] 
      self.mydict = {} 
      
   def head(self, it):       
      return [list[0] for list in it] 
      
   def tail(self, it):       
      return [list[1:] for list in it]     
                  
   # Important note! csv.DictReader is a GENERATOR.       
   # This means that you must iterate over the lines in the file 
   # if you want to read them all.     
   def readfile(self, fname):             
      self.reader = csv.DictReader(open(fname, "r")) 
      for line in self.reader: 
         for k, v in line.items(): 
            if v.isdigit():
               v = int(v) 
               self.mydict.update({k: v})            
            else: 
               self.mydict.update({k: v})            
            line.update({k: v})  
         self.mydict.update({k: v})                  
         print line    
         #self.mydict.update({x[0]: x[1:]})
         #print x[0], x[1:] 
            
                          
      '''for line in self.reader:  
         print line'''  
      '''for k, v in self.head(line), self.tail(line): 
             self.mydict.update({k: v}) '''
                                                                                                  
   def display(self): 
      for k, v in self.mydict.items(): 
         print k, v  
                     
   def test(self): 
      print self.data[0]   
      print self.data[1][0]                       
      print self.data[1][1]
      print self.data[1][2]                                              
                         
                         
#  Run the code 
a = crosstab() 
a.init() 
a.readfile("testdata.csv") 
a.display() 




                         
  


