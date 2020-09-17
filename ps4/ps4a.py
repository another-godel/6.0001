# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    def str_insert(str, n, ins):
        return str[0:n] + ins + str[n:]
    

    if len(sequence) == 1:
        return [sequence]
    else:
        result = []
        for i in range(len(sequence)):
            for j in get_permutations(sequence.replace(sequence[0],'')):
                result.append(str_insert(j, i, sequence[0]))
        return result
print(get_permutations('abcd'))
if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)
    print('Input:', 'abc')
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations('abc'))
    print()
    print('Input:', 'abcd')
    print('Expected Output:', ['abcd', 'abdc', 'acbd', 'adbc', 'acdb', 'adcb', 'bacd', 'badc', 'cabd', 'dabc', 'cadb', 'dacb', 'bcad', 'bdac', 'cbad', 'dbac', 'cdab', 'dcab', 'bcda', 'bdca', 'cbda', 'dbca', 'cdba', 'dcba'])
    print('Actual Output:', get_permutations('abcd'))
    print()
    print('Input:', 'abcd')
    print('Expected Output:', ['1234', '1243', '1324', '1423', '1342', '1432', '2134', '2143', '3124', '4123', '3142', '4132', '2314', '2413', '3214', '4213', '3412', '4312', '2341', '2431', '3241', '4231', '3421', '4321'])
    print('Actual Output:', get_permutations('1234'))