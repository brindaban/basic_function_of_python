def congrats_with_full_name(first_name,second_name):
    return "You are wellcome " + first_name + " " + second_name

print congrats_with_full_name("Suman","Das")


class calculation:
    def add_two(self):
        print "addition of 2 and 1 is "+str(2 + 1)
    def multiplication(self):
        print "multiplication of 3 and 4 is "+str(3*4)
myObject = calculation();
myObject.add_two();
myObject.multiplication();
