def vowelOrConsonant(x):
    if (x == 'a' or x == 'e' or x == 'i' or
        x == 'o' or x == 'u' or x == 'A' or
        x == 'E' or x == 'I' or x == 'O' or
        x == 'U'):
        print("Vowel")
    else:
        print("Consonant")
 
# Driver code
if __name__ == '__main__':
    vowelOrConsonant(str(input("Enter the vowel or consonent :")))

    