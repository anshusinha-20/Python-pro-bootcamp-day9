# Day 9 Project: The secret auction program

import auction

print(auction.logo)

auctionMembers = {}

def auction():
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: ₹"))
    auctionMembers[name] = bid

auction()

endOfAuction = False

while (endOfAuction == False):
    moreBidders = input("Are there any other bidders? Type 'y' for 'yes' or 'n' for 'no': ").lower()
    if (moreBidders == 'n'):
        endOfAuction = True
    else:
        auction()

winner = ''
winningBid = 0

for member in auctionMembers:
    if auctionMembers[member] > winningBid:
        winningBid = auctionMembers[member]
        winner = member

if (winningBid <= 0):
    print("No one won the bid!")
else:
    print(f"The winner is {winner} with a bid of ₹{winningBid}")

    
