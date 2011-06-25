


#  maketables.py 
#  A Python script to create text tables. 
#  License: Public domain 


def print_cell(): 
   print "+" + "------" + "+" 
   print "|" + "      " + "|" 
   print "|" + "      " + "|" 
   print "|" + "      " + "|" 
   print "+" + "------" + "+" + "\n" 


def make_table(rows, cols): 
  for i in range(0, cols + 1):
  	for j in range(0, rows + 1):
  		print_cell()
  		
        
#  Create a table 
make_table(2, 2) 

# make_table(4, 4)


         
