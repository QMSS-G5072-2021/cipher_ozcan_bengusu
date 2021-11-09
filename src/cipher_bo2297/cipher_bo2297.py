```
def cipher(text, shift, encrypt=True):

 """Shift each letter in a text on the alphabet by an indicated index
    Parameters
    ----------
    text: str
    shift: int
    encrypt: True by default 

    Returns: ciphered string
    -------
    Examples: 
    >>> cipher(bob, 1, True)
    cpc
    --------
    >>> count_words("text.txt")
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text
```