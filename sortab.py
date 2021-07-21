"""Given already-sorted lists, `a` and `b`, return sorted list of both.

You may not use sorted() or .sort().

Check edge cases of empty lists:

    >>> sort_ab([], [])
    []

    >>> sort_ab([1, 2,3], [])
    [1, 2, 3]

    >>> sort_ab([], [1, 2, 3])
    [1, 2, 3]

Check:

    >>> sort_ab([1, 3, 5, 7], [2, 6, 8, 10])
    [1, 2, 3, 5, 6, 7, 8, 10]
"""


def sort_ab(a, b):
    """Given already-sorted lists, `a` and `b`, return sorted list of both.

    You may not use sorted() or .sort().
    """

    #Edge cases: if both lists are empty, return an empty list

    #initialize empty results_list
    #index_i for first list = 0
    #index_j for second list = 0

    #while i is less than length of list1 and j is less than length of list 2:
        #num1 = list1[i]
        #num2 = list2[j]
        #num1 >= num2
            #add num 1 to results list
            #increment i
        #otherwise add num2 to results list
            #increment j

    #while i is less than length of list1
        #add list1[i] to results list
        #increment i

    #while j is less than length of list2
        #add list2[j] to results list
        #increment j

    #return results list

    if len(a) == 0 and len(b) == 0:
        return []

    results = []
    i = 0
    j = 0

    while i <= len(a)-1 and j <= len(b)-1:
        num1 = a[i]
        num2 = b[j]
        if num1 <= num2:
            results.append(num1)
            i += 1
        else:
            results.append(num2)
            j +=1

    while i <= len(a)-1:
        results.append(a[i])
        i += 1

    while j <= len(b)-1:
        results.append(b[j])
        j +=1

    return results

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU'RE A MERGE CHAMPION!!\n")
