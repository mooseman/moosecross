

#  Moosecross.py - A simple crosstab app in Python 

#  This code is released to the public domain.  
#  "Share and enjoy....."  :) 

#  Note = as at now (4th June), this code is not working, but 
#  it should be before much longer.  

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
      self.myfile = open('testdata.csv', 'r')  
	  for line in self.myfile.readlines(): 
	      self.datalist.append(list(line.rstrip('\n').split(',') ))  
      self.colslist = zip(*self.datalist) 	   		  
	  self.headingslist = self.colslist[0]  
	  
      
   def crosstab(self, rowvar, colvar, sumvar): 
      ''' Open the file ''' 
	  f = open('testdata.csv', 'r').readlines() 
	  ''' Convert it into lists of lines ''' 
	  for line in f: 
          self.linelist.append(list(line.rstrip('\n').split(',') ))
      ''' Convert it into a list of columns ''' 
	  self.colslist = zip(*self.lineslist) 		  
	  ''' Read it into a dictionary ''' 
	  for x in range(0, len(self.colslist) ):
          self.filedict.update({ self.colslist[x][0]: self.colslist[x][1:]})  
   
   
      if self.filedict.has_key(rowvar) and 	\ 
	     self.filedict.has_key(colvar) and  \  
		 self.filedict.has_key(sumvar): 
		 product = itertool.product(rowvar, colvar) 
		 prodsum = reduce.... ''' to be finished ... ''' 
		     
   def display(self): 
      print self.prodsum  


	  
#  Run the code 
a = crosstab() 

a.init() 

a.read('myfile.csv', sep=",")  

a.crosstab("city", "salesman", "tot_sales") 	  

a.display() 




