class Anagram():
    def __init__(self, word):
        self.word = word

    def match(self, list):
        anagrams = []
        for new_word in list:
            if sorted([letter for letter in new_word]) == sorted([letter for letter in self.word]):
                anagrams.append(new_word)
        return anagrams

listen = Anagram('listen')

print(listen.match(["listen", "silent", "hippopotamus"]))