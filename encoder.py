# Eric Kye
# 919455487
# Section A02


def encoder(message, key):
    
    # YOUR CODE HERE
    x=''
    key_list=[]
  
    for list in key:
        key_list.append(list[0])
        
        
        
 

    for letter in message:
        if letter not in key_list:
                    x=x+"?"
        
        for list in key:
               if letter in list[0]:
                   x=x+list[1]
               
            
              
              
                
               
                
        
            
    

          
                

            
           
        
                
           
           

                

       
    
    
    # Make sure your function returns the encoded text, not prints it, but 
    # you are free to use print() for testing purposes.
    
    return x
# VARIABLES FOR TESTING
code1 = [['a', 'n'],['b', 'o'],['c', 'p'],['d', 'q'],
         ['e', 'r'],['f', 's'],['g', 't'],['h', 'u'],
         ['i', 'v'],['j', 'w'],['k', 'x'],['l', 'y'],
         ['m', 'z'],['n', 'a'],['o', 'b'],['p', 'c'],
         ['q', 'd'],['r', 'e'],['s', 'f'],['t', 'g'],
         ['u', 'h'],['v', 'i'],['w', 'j'],['x', 'k'],
         ['y', 'l'],['z', 'm'],[' ', ' ']]
code2 = [['1','!'], ['2','@'],['3','#'],['4','$'],['5','%'],
         ['6','^'], ['7','&'],['8','*'],['9','('],['0',')']]
test1 = "the quick brown fox jumped over the lazy dog"
test2 = "i do not like green eggs and ham"
test3 = "we can't stop!"
test4 = ""
test5 = "9876543210"





 
 
