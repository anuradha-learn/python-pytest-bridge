DISCOUNT_THRESHOLD=50

def apply_discount(total,percent):
    if not 0<=percent<=100:
        raise ValueError("percent most be between 0 and 100")
    return (1-percent/100)*total

def cart_total(items,percent):
    # # add up all the prices with loop
    total=0
    for item in items:
        total=total+item['price']*item['quantity']

    if total >= DISCOUNT_THRESHOLD:
        total=apply_discount(total,percent)

    
    return total



# items=[{"name":"Notebook","price":12.5,"quantity":3},{"name":"pen","price":2.5,"quantity":100}]

# print(cart_total(items,10))