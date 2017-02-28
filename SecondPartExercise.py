__author__ = 'hamouy'

def donuts(count):
    if count < 10:
        output= 'Number of donuts: %d' % count
    else:
        output= 'Number of donuts: many'
    return output

donuts(9)
#donuts(11)


# In[97]:

def both_ends(s):
    len_s = len(s)
    if len_s < 2:
        s = ""
    else:
        s=s[0:2]+s[len_s-2:len_s]
    return s


# In[98]:

both_ends('spring')


# In[82]:

def fix_start(s):
    first_char = s[0]
    len_s = len(s)
    i = 1
    while i < len_s:
        if s[i]== first_char:
            s= s[0:i]+ "*"+s[i+1:]
        i+=1
    return s


# In[81]:

fix_start('bubble')


# In[83]:

def mix_up(a, b):
    temp = a
    a = b[0:2]+a[2:]
    b = temp[0:2]+b[2:]
    temp = a + " " + b
    return temp


# In[84]:

mix_up("mix","pod")


# In[99]:

def main():
    print 'donuts'
    # Each line calls donuts, compares its result to the expected for that call.
    test(donuts(4), 'Number of donuts: 4')
    test(donuts(9), 'Number of donuts: 9')
    test(donuts(10), 'Number of donuts: many')
    test(donuts(99), 'Number of donuts: many')

    print
    print 'both_ends'
    test(both_ends('spring'), 'spng')
    test(both_ends('Hello'), 'Helo')
    test(both_ends('a'), '')
    test(both_ends('xyz'), 'xyyz')


    print
    print 'fix_start'
    test(fix_start('babble'), 'ba**le')
    test(fix_start('aardvark'), 'a*rdv*rk')
    test(fix_start('google'), 'goo*le')
    test(fix_start('donut'), 'donut')

    print
    print 'mix_up'
    test(mix_up('mix', 'pod'), 'pox mid')
    test(mix_up('dog', 'dinner'), 'dig donner')
    test(mix_up('gnash', 'sport'), 'spash gnort')
    test(mix_up('pezzy', 'firm'), 'fizzy perm')



def verbing(s):
    len_s = len(s)
    if len_s > 2:
        if s[len_s-3:] == "ing":
            s = s+"ly"
        else:
            s = s+"ing"
    return s

def not_bad(s):
    myString = s.split(" ")
    activate_remove = False
    i = 0
    index_not = 0
    index_bad = 0
    while i < len(myString):
        if myString[i] == "not":
            index_not = i
            activate_remove = True
        elif myString[i][0:3] == "bad" and activate_remove == True:
            index_bad = i
            myString[i]="good"+ myString[i][3:]
            myString = myString[0:index_not] + myString[index_bad:]
            break
        i+=1
    myString = ' '.join(str(e) for e in myString)
    return myString


def front_back(a, b):
    half_a = len(a)/2+1 if len(a) % 2 == 1 else len(a)/2
    half_b = len(b)/2+1 if len(b) % 2 == 1 else len(b)/2
    return a[0:half_a] + b[0:half_b] + a[half_a:] + b[half_b:]

def main():
    print 'verbing'
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')

    print
    print 'not_bad'
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print
    print 'front_back'
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')