class Bus:
    def __init__(self, numSeatsTotal, numSeatsFilled, depart, arrive):
        self.numSeatsTotal = numSeatsTotal
        self.numseatsFilled = numSeatsFilled
        self.depart = depart
        self.arrive = arrive

    def isFilled(self):
        return self.numseatsFilled == self.numSeatsTotal

