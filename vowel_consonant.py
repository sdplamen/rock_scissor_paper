def vowel(vow):
    vowels = 'AaEeIiOoUu'
    if vow in vowels:
        print('It\'s a vowel.')
    else:
        print(vow, 'is a consonant.')
vow = input('Type a vowel or consonant : ')
vowel(vow)
