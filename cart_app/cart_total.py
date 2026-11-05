#define list of cart items prices
prices = [12.5, 4.5, 30.0, 15.5]

# add up all the prices with loop
total=0
for price in prices:
    total=total+price
# print("before ",total)

#decision
if total >= 50:
    discount_percent=10
    total=(1-discount_percent/100)*total
else:
    discount_percent=0

print(f"{len(prices)} items ,total after {discount_percent} discount ={total}")



