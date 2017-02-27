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
