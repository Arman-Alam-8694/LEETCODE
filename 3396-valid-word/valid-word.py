class Solution:
    def isValid(self, word: str) -> bool:
        if len(word)<3:
            return False
        else:
            conso,vowel,uppercase,lowercase,digit=False,False,False,False,False
            for i in word:
                if i.isdigit():
                    digit=True
                elif i.isalpha():
                    if i.isupper():
                        uppercase=True
                    else:
                        lowercase=True
                    if i in "aeiou" or i in "AIEOU":
                        vowel=True
                    else:
                        conso=True
                else:
                  
                    return False
            return vowel and conso 





        