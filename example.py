#If you know how to use scratchattach, just look at line 13 - 42

import requests
import scratchattach as scratch3

session = scratch3.login("USERNAME_OF_ANY_ACCOUNT_(ACCOUNT_CAN_BE_NEW_SCRATCHER)", "PASSWORD")


conn = session.connect_cloud("YOUR_PROJECT_ID")

client = scratch3.CloudRequests(conn)

@client.request
def purchase(username, SellerName, Price):
    request = requests.post("https://scrathon.justablock.online/transaction", json={
    "price": Price,
    "buyer": username,
	"seller": SellerName
    })

    if request.content == "You have been banned from selling items in your projects!":
        return "Fail!"
        #In scratch, tell the user the transaction failed
    elif request.content == "User does not have enough money to buy the item!":
        return "Not enough coins!"
            #In scratch, tell the user they do not have enough coins to make the purchase

    elif request.content == "Transaction has been added to pending transactions, transaction will go through once the user has confirmed!":
        #In scratch, tell your users to look at the comments of the Scrathon project and find their verification comment in the project's comments, reply to it with 'yes' and the transaction will go through!
        #if the user

        return "Success!"

@client.request
def purchasecheck(username, SellerName, Price): #Check if the player bought the item so you can give them the promised item (If you don't give the item to the player you will get banned from selling items)
    request = requests.post("https://scrathon.justablock.online/checkpurchase", json={
    "price": Price,
    "buyer": username,
	"seller": SellerName
    })

    return request.content

client.run()