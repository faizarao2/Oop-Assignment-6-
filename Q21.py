# 21. Make a Custom Class Iterable
# Assignment:
# Create a class Countdown that takes a start number. Implement __iter__() and __next__() 
# to make the object iterable in a for-loop, counting down to 0.

class CountDown:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        self.current = self.start
        return self    
    
    def __next__(self):
        if self.current < self.stop:  # Stop iteration when current reaches stop
            raise StopIteration
        current_value = self.current
        self.current -= 1  # Decrement current value for countdown
        return current_value


# Countdown object
countdown = CountDown(5, 0)

print("Lets count......")
# Loop through the countdown object
for number in countdown:
    print(number)