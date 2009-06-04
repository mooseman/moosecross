

#  Moosecross.py - A simple crosstab app in Python 

#  This code is released to the public domain.  
#  "Share and enjoy....."  :) 

#  Note = as at now (4th June), this code is not working, but 
#  it should be before much longer.  

#  It is eventually planned to add "traffic-lighting" and 
#  the ability to output the crosstab to HTML and text files. 


class crosstab(): 
   def init(self): 
      self.rowvar = self.colvar = self.sumvar = None 
	  self.filedict = {} 
	  self.keylist = []
	  self.keys = dict(self.keylist)  
	  	  
   def read(self, file, sep=","): 
      myfile = open(file, 'r')
	  self.keylist.append(myfile.readline()
      
   def crosstab(self, rowvar, colvar, sumvar): 
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




