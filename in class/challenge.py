money = int(input("How much do you need to break? (In cents)"))
dollars = money//100
remainder = money%100
quarters = remainder//25
remainder = remainder - (quarters * 25)
dimes = remainder//10
remainder = remainder - (dimes * 10)
nickles = remainder//5
remainder = remainder - (nickles * 5)
pennies = remainder

print(dollars, "dollars", quarters, "quarters", dimes, "dimes", nickles, "nickles", pennies, "Pennies")