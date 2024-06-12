class EvenNumbers:
    def __init__(self, start=0, end=1):
        self.start = start
        self.end = end
        self.i = 0

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.start % 2 == 0:
            chet = self.start + self.i
            self.i += 2
        else:
            self.start = self.start + 1
            chet = self.start + self.i
            self.i += 2


        if chet == self.end:
            raise StopIteration()
        return chet

en = EvenNumbers(1, 10)

for i in en:
    print(i)





