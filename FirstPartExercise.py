__author__ = 'hamouy'


def match_ends(words):
    compt = 0
    for word in words:
        len_word = len(word)
        if len_word >= 2:
            if  word[0] == word[len_word-1]:
                compt += 1
    return compt


def front_x(words):
    list1 = list(words)
    list2=[]
    for word in words:
        if word[0] == "x":
            list2.append(word)
            list1.remove(word)
            continue
    list1 = sorted(list1)
    list2 = sorted(list2)
    return list2 + list1


def get_last_tupple_element(thetuples):
    return thetuples[len(thetuples)-1]

def sort_last(tuples):
    return sorted(tuples,key = get_last_tupple_element)

def test(got, expected):
    prefix = 'OK' if got == expected else ' X'
    # !r prints a Python representation of the strings (complete with quotes)
    print ' {} got: {!r} expected: {!r}'.format(prefix, got, expected)

def main():
    print 'match_ends'
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    print
    print 'front_x'
    test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
        ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
        ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
        ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

    print
    print 'sort_last'
    test(sort_last([(1, 3), (3, 2), (2, 1)]),
         [(2, 1), (3, 2), (1, 3)])
    test(sort_last([(2, 3), (1, 2), (3, 1)]),
         [(3, 1), (1, 2), (2, 3)])
    test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)])

def remove_adjacent(nums):
    i = 0
    print(nums[0:1])
    while i < len(nums):
        if nums[i] in nums[(i+1):]:
            nums = nums[0:i]+nums[i+1:]
            continue
        i += 1
    return nums

def linear_merge(list1, list2):
    list_len = len(list1+list2)
    i = 0
    j = 0
    merged_list = []
    while (i+j) < list_len:
        if (list1[i] < list2[j]):
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
        if i == len(list1):
            merged_list += list2[j:]
            break;
        elif j == len(list2):
            merged_list += list1[i:]
            break
    return merged_list

def main():
    print 'remove_adjacent'
    test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    test(remove_adjacent([]), [])

    print
    print 'linear_merge'
    test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
        ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
        ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
        ['aa', 'aa', 'aa', 'bb', 'bb'])