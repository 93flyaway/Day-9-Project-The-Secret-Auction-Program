from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)

#flow: ask name, ask bid, ask if other buyer present.
# if yes, repeat -> while loop
# if no, determine winner, print winner

bids = {}
def add_new_bid(name, amount):
    bids[name] = amount

continue_loop = True

while continue_loop:
    new_bidder = input("What is your name?: ")
    bid_amount = int(input("What's your bid?: $"))
    add_new_bid(new_bidder, bid_amount)
    is_new_bidder = input("Are there any other bidders? Type 'yes' or 'no.:\n").lower()
    if is_new_bidder == "no":
        continue_loop = False
    clear()

highest_bid = 0
winner = ""
for bidder in bids:
    if highest_bid < bids[bidder]:
        highest_bid = bids[bidder]
        winner = bidder
    elif highest_bid == bids[bidder]:
        winner = winner + ", " + bidder

print(f"The winner is {winner} with a bid of ${highest_bid}.")