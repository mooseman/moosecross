

#  Moosecross.py - A simple crosstab app in Python 

#  This code is released to the public domain.  
#  "Share and enjoy....."  :) 

#  Status - as at now (6th June), this code reads a file 
#  into a dictionary.  It shouldn't be long before the actual 
#  crosstab code is added and working.   

#  It is eventually planned to add "traffic-lighting" and 
#  the ability to output the crosstab to HTML and text files. 

import itertools 


class crosstab(): 
   def init(self): 
      self.rowvar = self.colvar = self.sumvar = None 
      self.filedict = {} 
      self.headingslist = []
      self.linelist = [] 
      self.colslist = [] 
	  
	  	  
   def read(self, file, sep=","):       
      ''' Open the file ''' 
      self.file = open(file, 'r').readlines() 
      ''' Convert it into lists of lines ''' 
      for line in self.file:   
          self.linelist.append(list(line.rstrip('\n').split(',') ))
      ''' Convert it into a list of columns ''' 
      self.colslist = zip(*self.linelist) 		  
      ''' Read it into a dictionary ''' 
      for x in range(0, len(self.colslist) ):
          self.filedict.update({ self.colslist[x][0]: self.colslist[x][1:]})  
	  
      
   def crosstab(self, rowvar, colvar, sumvar): 
      ''' 
      if self.filedict.has_key(rowvar) and 	\ 
	     self.filedict.has_key(colvar) and  \  
		 self.filedict.has_key(sumvar): 
		    product = itertool.product(rowvar, colvar) 
		    prodsum = reduce....  to be finished ... '''  
		     						
   def display(self): 
       print self.filedict 

	  
#  Run the code 
a = crosstab() 

a.init() 

a.read('testdata.csv', sep=",")  

#  a.crosstab("city", "salesman", "tot_sales") 	  

a.display() 




