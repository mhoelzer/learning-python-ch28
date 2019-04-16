class Person:
    def __init__(self, name, job=None, pay=0):  # constructor takes 3 args
        self.name = name  # fill out fields when made; self is new instance obj
        self.job = job
        self.pay = pay


if __name__ == "__main__":  # run tests at bottom only when file is run
    bob = Person("Bob Smith")  # gets the defaults
    sue = Person("Sue Jones", job="dev", pay=100000)
    print(bob.name, bob.pay)  # to get rid of the extra () --> format/fstring
    print(sue.name, sue.pay)
    print(bob.name.split()[-1])  # last name
    sue.pay *= 1.10  # inreases pay
    print("%.2f" % sue.pay)
    # print("{}".format(sue.pay))
