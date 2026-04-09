weeklySales= []
for i in range(7):
    daysale  = int(input(f"Day {i+1} sales :"))
    weeklySales.append(daysale)
totalsale = sum(weeklySales)
print("Total weekly sales is ",totalsale)    