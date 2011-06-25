


#  maketables.py 
#  A Python script to create text tables. 
#  License: Public domain 


def print_cell(): 
   corner = "+" 
   hline  = "------" 
   vline  = "|" 
   
#  A single-cell table (1 row, 1 col) has - 
#  line = corner + hline + corner 
#  vert_lines = hline * 3 
#  line = corner + hline + corner 
#  So, that is - corner + ( hline + corner )*cols , 
#  corner + ( vline*3 + corner )*rows 
   

#   print "+" + "------" + "+" 
#   print "|" + "      " + "|" 
#   print "|" + "      " + "|" 
#   print "|" + "      " + "|" 
#   print "+" + "------" + "+" + "\n" 


def make_table(rows, cols): 
  for i in range(0, cols + 1):
  	for j in range(0, rows + 1):
  		print_cell()
  		
        
#  Create a table 
make_table(5, 5) 


         
