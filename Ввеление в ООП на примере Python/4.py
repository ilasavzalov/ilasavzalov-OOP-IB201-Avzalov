class OddEvenSeparator:
    def __init__(self):
        self.e_ns = []
        self.o_ns = []
    
    def add_number(self, number):
        if number % 2 == 0:
            self.e_ns.append(number)
        else:
            self.o_ns.append(number)
    
    def even(self):
        return self.e_ns
    
    def odd(self):
        return self.o_ns



separator = OddEvenSeparator()
separator.add_number(1)
separator.add_number(5)
separator.add_number(6)
separator.add_number(8)
separator.add_number(3)
print(' '.join(map(str, separator.even())))
print(' '.join(map(str, separator.odd())))
