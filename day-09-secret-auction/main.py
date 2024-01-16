import art
import os

bids = []
clear = lambda: os.system('cls')

def add_bidder():
    name = input("what is your name?: ")
    bid = input("What is your bid?: ")
    if bid.isnumeric():
        bidder = {
            "name": name,
            "bid": float(bid)
        }
        other = input("Are there any other bidder? Type 'yes' or 'no': ").lower()
        bids.append(bidder)
        return True if other == "yes" else False
    else:
        print("Invalid input. Please try again")
        return add_bidder()

def check(bids):
    max = {"name":str(), "bid":float()}
    for bidder in bids:
        print(max)
        if bidder["bid"] > max["bid"]:
            max = bidder
    return max

def auction():
    print(art.logo)
    print("Welcome to the secret auction program.")

    more_bidder = True 
    while more_bidder:
        more_bidder = add_bidder()
        clear()

    highest = check(bids)

    print(f"Highest bidder is {highest['name']} with ${highest['bid']}")

    toContinue = input("\nDo you want to start a new auction? Type 'yes' or 'no': ")
    if toContinue == "yes":
        clear()
        auction()

auction()