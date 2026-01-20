from auction_art import art
import os
def find_highest_bidder(bidding_dictionary):
    winner = max(bidding_dictionary, key=bidding_dictionary.get)
    highest_bid = bidding_dictionary[winner]
    print(f"Winner: {winner}, with a bid of: {highest_bid}")


print(art)

bids = {}
continue_bidding = True

while continue_bidding:

    name = input("What is your name? : \n")
    bid_price = int(input("What is your bid? : "))
    bids[name] = bid_price

    should_continue = input("Are there any other bidders? type 'yes' or 'no' : ").lower()
    if bid_price in bids.values:
        print("This bid already done pleas make another bid")
        continue
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        os.system("clear")
