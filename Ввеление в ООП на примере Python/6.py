class MinMaxWordFinder:
    def __init__(self):
        self.words = []
    
    def add_sentence(self, sentence):
        self.words.extend(sentence.split())
    
    def shortest_words(self):
        if len(self.words) == 0:
            return []
        
        min_length = min(len(w) for w in self.words)
        shortest = [w for w in self.words if len(w) == min_length]
        shortest.sort()
        return shortest
    
    def longest_words(self):
        if len(self.words) == 0:
            return []
        max_length = max(len(w) for w in self.words)
        longest = sorted(set(w for w in self.words if len(w) == max_length))
        return longest


finder = MinMaxWordFinder()
finder.add_sentence('hello abc world')
finder.add_sentence('def asdf qwert')
print(' '.join(finder.shortest_words()))
print(' '.join(finder.longest_words()))
