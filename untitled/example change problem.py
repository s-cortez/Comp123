from collections import OrderedDict


def makechange(money):
    print("Making change for " + str(money) + " cents!")

    # Define change by amount of cents and name
    moneytypes = OrderedDict([
        (100, "Dollars"),
        (25, "Quarters"),
        (10, "Dimes"),
        (5, "Nickles"),
        (1, "Pennies")
    ])

    # Get list of amount of change by type
    amounts = makechangehelper(money, moneytypes.keys())

    # Print results
    for (amount, moneytype) in zip(amounts, moneytypes.values()):
        print(moneytype + ": " + str(amount))
    print("")


def makechangehelper(money, changelist):
    amounts = []

    # Get amount of change for each type
    for divisor in changelist:
        amount = money // divisor  # Amount of change type
        amounts.append(amount)

        money = money % divisor  # Money remaining after change is removed
    return amounts


makechange(732)
makechange(343)
makechange(101)
makechange(100)
