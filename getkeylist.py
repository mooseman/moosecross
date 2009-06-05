


d = {("foo", "bar"): 123 }

d.update({ ("foo", "baz"): 234 }) 

d.update({ ("foo", "hi there"): 845 })

d.update({ ("bar", "test"): 5376 })

  

#  This assumes that keys are in a tuple 
def getkeylist(dictname):
   for key in dictname.keys(): 
       print list(key) 
   a = list(d.keys()) 
   print a[0], a[1], a[2], a[3]  
   ''' Print the column keys ''' 
   
      
#  Run the code 
test = getkeylist(d) 

print d 


   
   
   
   
