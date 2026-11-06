# #define list of cart items prices
# prices = [12.5, 4.5, 30.0, 15.5]

# # add up all the prices with loop
# total=0
# for price in prices:
#     total=total+price
# # print("before ",total)

# #decision
# if total >= 50:
#     discount_percent=10
#     total=(1-discount_percent/100)*total
# else:
#     discount_percent=0

# print(f"{len(prices)} items ,total after {discount_percent} discount ={total}")

DISCOUNT_THRESHOLD=50

def apply_discount(total,percent):
    if not 0<=percent<=100:
        raise ValueError("percent most be between 0 and 100")
    return (1-percent/100)*total

def cart_total(prices,percent):
    # # add up all the prices with loop
    total=0
    for price in prices:
        total=total+price

    if total >= DISCOUNT_THRESHOLD:
        total=apply_discount(total,percent)

    
    return total


cart1_prices = [12.5, 4.5, 30.0, 15.5]
try:    
    print("cart1 prices: ",cart_total(cart1_prices,150))
except ValueError as error:
    print(f"Could not apply the discount: {error}")


cart2_prices = [12.5, 14.5, 30.0, 20.5]
try:  
    print("cart2 prices: ",cart_total(cart2_prices,10))
except ValueError as error:
    print(f"Could not apply the discount: {error}")









