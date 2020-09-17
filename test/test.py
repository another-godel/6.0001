import string
VOWELS_LOWER = 'aeiou'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
def build_transpose_dict(vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        transpose_dict = {}
        for char in VOWELS_LOWER:
            transpose_dict[char] = vowels_permutation[VOWELS_LOWER.index(char)]
            transpose_dict[char.upper()] = transpose_dict[char].upper()
        for char in CONSONANTS_LOWER:
            transpose_dict[char] = char
            transpose_dict[char.upper()] = char.upper()
        return transpose_dict

#print(build_transpose_dict("eaiuo"))

def apply_transpose(text, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        transposed = ''
        for char in text:
            if char in ' .,!':
                transposed += char
            elif (char in string.ascii_lowercase) or (char in string.ascii_uppercase):
                transposed += transpose_dict[char] 
            else: 
                raise ValueError('Not a valid string')
        return transposed
    
print(apply_transpose('con cho nay', build_transpose_dict("eaiuo")))