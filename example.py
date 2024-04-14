#If you know how to use scratchattach, just look at line 13 - 31
import scratchattach as scratch3
from ScrathonPayments import Scrathon

session = scratch3.login("USERNAME_OF_ANY_ACCOUNT_(ACCOUNT_CAN_BE_NEW_SCRATCHER)", "PASSWORD")

conn = session.connect_cloud("YOUR_PROJECT_ID")

ScrathonPayments = Scrathon("USERNAME_OF_ACCOUNT_TO_RECEIVE_FUNDS")

client = scratch3.CloudRequests(conn)

@client.request
def purchase(username, Price):
    Purchase = ScrathonPayments.purchase(Price, username)

    if Purchase == "You have been banned from selling items in your projects!":
        return "Fail!"
        #In scratch, tell the user the transaction failed
    elif Purchase == "User does not have enough money to buy the item!":
        return "Not enough coins!"
        #In scratch, tell the user they do not have enough coins to make the purchase
    elif Purchase == "Transaction has been added to pending transactions, transaction will go through once the user has confirmed!":
        #In scratch, tell your users to look at the comments of the Scrathon project and find their verification comment in the project's comments, reply to it with 'yes' and the transaction will go through!
        return "Success!"

@client.request
def purchasecheck(username, Price): #Check if the player bought the item so you can give them the promised item (If you don't give the item to the player you will get banned from selling items)
    PurchaseCheck = ScrathonPayments.purchasecheck(Price, username)

    return PurchaseCheck

client.run()
