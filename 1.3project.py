def add_tip(total, tip_percent):
    ''' Return the total amount including tip'''
    tip = tip_percent*total
    return total + tip

def pythag(a, b):
    c_squared = (a * a) + (b * b)
    c = c_squared ** (0.5)
    return c
    
def in_square(x,y):
    if (x > 40 and 130 > x and y >= 100 and y <= 120):
        print "true"
    else:
        print "false"
    
def really(d , e):
    f=(d+e)/(3)
    return f
    

def age_limit_output(age):
    '''Step 6a if-else example'''
    AGE_LIMIT = 13    # convention: use CAPS for constants
    if age < AGE_LIMIT:
      print (age, 'is below the age limit.')
    else:
      print(age, 'is old enough.')
    print(' Minimum age is ', AGE_LIMIT)
    
def truletter(letter):
    word = 'no'
    if letter in word:
        return True
    else:
        return False
        