class Person:
    def __init__(self, name, job=None, pay=0):  # constructor takes 3 args
        self.name = name  # fill out fields when made; self is new instance obj
        self.job = job
        self.pay = pay

    def last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __repr__(self):
        return "[Person: {}, ${}]".format(self.name, self.pay)


if __name__ == "__main__":  # run tests at bottom only when file is run
    bob = Person("Bob Smith")  # gets the defaults
    sue = Person("Sue Jones", job="dev", pay=100000)
    # print(bob.name, bob.pay)  # to get rid of the extra () --> format/fstring
    # print(sue.name, sue.pay)
    print(bob)
    print(sue)
    print(bob.last_name(), sue.last_name())
    sue.give_raise(.10)
    print(sue)