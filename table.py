

#  table.py 
#  Draw a table for use in crosstabs.  
# This code is released to the public domain. 
# "Share and enjoy..."  :)    


class table(object):  
   def __init__(self, name, rows, cols, width, height): 
      self.name = name 
      self.rows = rows 
      self.cols = cols 
      self.width = width 
      self.height = height
            
   def cell(self, crow, ccol, cdata=None): 
      self.crow = crow 
      self.ccol = ccol   
      self.cdata = cdata 
      
   def rowline(self): 
      self.rowline = "+" + ("-" * self.width) + "+"   
      
   def colline(self): 
      self.colline = "|" + " " + self.cdata + 
         (self.width-len(self.cdata)) + " " + "|"       
      
   def draw(self):  
      #  To be completed 
      
      
      
      
      
      
      
      
        



