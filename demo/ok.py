# Letter Frequency Analysis

## Part 1 - Slow

#Our starting test string that will be analyzed.
test_string = "abcdeabcdeabcdeabcdeabcde"




def count_char(text, char):
    """Function uses count to count the number of times a character occurs in a string"""
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count





def letterCounterS(text):
    """This function was constructed using examples from the code learning app Solo Learn. This function uses a nested for loop to see if
    the character (char) is in the supplied string 'text'. Returns a list containing the counts of each letter.'"""
    counts = []
     #convert string 'text' to all lowercase.
    text = text.lower()

    for char in "abcdefghijklmnopqrstuvwxyz":
        counts.append(char + String(count_char(text, char)))
    return counts





#Using our text file in the letterCounterS() function.
print(letterCounterS(test_string))






## Part 2 - Fast

#Our starting test string that will be analyzed.
test_string = "abcdeabcdeabcdeabcdeabcde"




def letterCounter(text):
    """This function takes an input string and counts the occurrences of the letters a-z and A-Z and returns a dictionary with
    key:value pairs representing the key letter and an associated value representing the number of  occurrences.
    Note: This function counts both 'a' and 'A' as an occurrence of 'a'."""
    letters_of_interest=”abcdefghijklmnopqrstuvwxyz”


    #The dictionary object that will contain the frequency (number of occurrences) of each letter in our test-string.
    #Each key:value pair represents the key letter and an associated value representing the number of  occurrences.
    letter_frequency={"a" : 0, "b" : 0, "c" : 0, "d" : 0, "e" : 0, "f" : 0, "g" : 0, "h" : 0, "i" : 0, "j" : 0, "k" : 0,
         "l" : 0, "m" : 0, "n" : 0, "o" : 0, "p" : 0, "q" : 0, "r" : 0, "s" : 0, "t" : 0, "u" : 0, "v" : 0, "w" : 0, "x" : 0, "y" : 0, "z" : 0}

    #convert string 'text' to all lowercase.
    text = text.lower()

    #Checking each character (char) in the string 'text' to see if it is a letter a-z, and counting it if is a letter
    for char in text:
        if char in letters_of_interest:
            letter_frequency[char]=letter_frequency[char]+1

    #return the letter-frequency dictionary
    return letter_frequency





#Using our text file in the letterCounter() function.
print(letterCounter(test_string))





# Part 3 - Slow Read


def count_char(text, char):
    """Function uses count to count the number of times a character occurs in a string"""
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count





def letterCounterS(text):
    """This function was constructed using examples from the code learning app Solo Learn. This function uses a nested for loop to see if
    the character (char) is in the supplied string 'text'. Returns a list containing the counts of each letter.'"""
    counts = []

    for char in "abcdefghijklmnopqrstuvwxyz":
        counts.append(char + String(count_char(text, char)))
    return counts





#Loading the Gettysburg Address as a string of text, and converting it to all lowercase letters.
with open("files/gettysburgaddress.txt") as x:
    test_string = x.read()
    test_string = test_string.lower()
#Printing 'text' to see if loading occured correctly.
print(test_string)





#Using our text file in the letterCounterS() function.
print(letterCounterS(test_string))





# Part 4 - Fast Read

#Loading the Gettysburg Address as a string of text.
with open(files/gettysburgaddress.txt) as x:
    test_string = x.read()





#Print test_string to show file has been properly loaded
print(test_string)





def letterCounter(text):
    """This function takes an input string and counts the occurrences of the letters a-z and A-Z and returns a dictionary with
    key:value pairs representing the key letter and an associated value representing the number of  occurrences.
    Note: This function counts both 'a' and 'A' as an occurrence of 'a'."""
    letters_of_interest=”abcdefghijklmnopqrstuvwxyz”

    #The dictionary object that will contain the frequency (number of occurrences) of each letter in our test-string.
    #Each key:value pair represents the key letter and an associated value representing the number of  occurrences.
    letter_frequency={"a" : 0, "b" : 0, "c" : 0, "d" : 0, "e" : 0, "f" : 0, "g" : 0, "h" : 0, "i" : 0, "j" : 0, "k" : 0,
         "l" : 0, "m" : 0, "n" : 0, "o" : 0, "p" : 0, "q" : 0, "r" : 0, "s" : 0, "t" : 0, "u" : 0, "v" : 0, "w" : 0, "x" : 0, "y" : 0, "z" : 0}

    #convert string 'text' to all lowercase.
    text = text.lower()

    #Checking each character (char) in the string 'text' to see if it is a letter a-z, and counting it if is a letter
    for char in text:
        if char in letters_of_interest:
            letter_frequency[char]=letter_frequency[char]+1

    #return the letter-frequency dictionary
    return letter_frequency

print(letterCounter(test_string))







#Part 5 - DNA Analysis

#Test string of DNA
dna_test = "ATGCTTAGTCAGTCATGCACCCAAGTTTGACCTTTTAAACGGAAC"





def dnaToProtein(sequence):
    """This function takes a string dna sequence and uses a codon table to convert the sequence into a protein sequence and returns it.
    Note: This function does NOT take into account start and stop sequences to get real proteins from real DNA sequences."""

    protein = ""

    """Dictionary object where the keys are codons and the values are amino acid residues: Dictionary provided by pythonforbiologists.com
    Note: this is only an example list"""
    codons = { 'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 'AAC':'N', 'AAT':'N', 'AAA':'K',
    'AAG':'K', 'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R', 'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 'CCA':'P', 'CCC':'P', 'CCG':'P',
    'CCT':'P', 'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 'GTA':'V', 'GTC':'V', 'GTG':'V',
    'GTT':'V', 'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 'GGA':'G', 'GGC':'G', 'GGG':'G',
    'GGT':'G', 'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L', 'TAC':'Y', 'TAT':'Y', 'TAA':'_',
    'TAG':'_', 'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

    for n in range(0, len(sequence), 3):
        if sequence[n:n+3] in codons:
            protein = protein + codons[sequence[n:n+3]]
    return protein






#testing the dnaToProtein function with the test sequence 'dna_test'
print(dnaToProtein(dna_test))
