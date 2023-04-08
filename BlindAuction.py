# Day 9 of 100 for the Udemy Python Bootcamp
# Exercise 9-3: Blind Auction
import os


def cls():
    os.system('cls' if os.name == "nt" else 'clear')


logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

# HINT: You can call clear() to clear the output in the console.
print(logo)
auction = {}
keep_alive = True

def highest_bidder(auction_record):
  highest_bid = 0
  winner_name = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in auction_record:
    bid_amount = auction_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner_name = bidder
  print(f"The winner is {winner_name} with a bid of ${highest_bid}")


while keep_alive:
    user = input("Enter your user name:\n")
    bid = int(input("Enter your bid amount:\n$"))
    auction[user] = bid
    keep_bidding = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    if keep_bidding == 'no':
        keep_alive = False
        highest_bidder(auction)
    elif keep_bidding == 'yes':
        cls()

# Debugging
# print(auction)

