from tkinter import *
import requests
import json

#Create root window/give attributes
root = Tk()
root.geometry('500x500')
root.config(bg="")
root.title('CoinWolf')

#API INFO
api_requests = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false')
api = json.loads(api_requests.content)

#coin info

#btc
btcname = api[0]['name']
btcsymbol = api[0]['symbol']
btcprice = api[0]['current_price']
btc_msupply = api[0]['max_supply']
btcmcap = api[0]['market_cap']
btcchange1 = api[0]['price_change_percentage_24h']

#eth
ethname = api[1]['name']
ethsymbol = api[1]['symbol']
ethprice = api[1]['current_price']
eth_msupply = api[1]['max_supply']
ethmcap = api[1]['market_cap']
ethchange1 = api[1]['price_change_percentage_24h']

#bnb
bnbname = api[2]['name']
bnbsymbol = api[2]['symbol']
bnbprice = api[2]['current_price']
bnb_msupply = api[2]['max_supply']
bnbmcap = api[2]['market_cap']
bnbchange1 = api[2]['price_change_percentage_24h']

#ada
adaname = api[3]['name']
adasymbol = api[3]['symbol']
adaprice = api[3]['current_price']
ada_msupply = api[3]['max_supply']
adamcap = api[3]['market_cap']
adachange1 = api[3]['price_change_percentage_24h']

#-----------------------------------------------------------------------------------------------------------------------

#top label
maintitle = Label(root,text="CoinWolf",font=("Helvetica",25),bg="green",fg="white")
maintitle.grid(row=0,column=3,columnspan=5,ipadx=50)

#Coin name labels
btcnameLabel = Label(root,text=btcname)
ethnameLabel = Label(root,text=ethname)
bnbnameLabel = Label(root,text=bnbname)
adanameLabel = Label(root,text=adaname)

#Coin name label placement
btcnameLabel.grid(row=1,column=0)
ethnameLabel.grid(row=2,column=0)
bnbnameLabel.grid(row=3,column=0)
adanameLabel.grid(row=4,column=0)

#Coin Symbol Labels
btcsymbolLabel = Label(root,text=btcsymbol)
ethsymbolLabel = Label(root,text=ethsymbol)
bnbsymbolLabel = Label(root,text=bnbsymbol)
adasymbolLabel = Label(root,text=adasymbol)

#Coin Symbol Label Placement
btcsymbolLabel.grid(row=1,column=1)
ethsymbolLabel.grid(row=2,column=1)
bnbsymbolLabel.grid(row=3,column=1)
adasymbolLabel.grid(row=4,column=1)

#Coin Current Price Label/format as usd currency
btcpriceLabel = Label(root,text="${:,.2f}". format(btcprice))
ethpriceLabel = Label(root,text="${:,.2f}". format(ethprice))
bnbpriceLabel = Label(root,text="${:,.2f}". format(bnbprice))
adapriceLabel = Label(root,text="${:,.2f}". format(adaprice))

#Coin Current Price Label Placement
btcpriceLabel.grid(row=1,column=3)
ethpriceLabel.grid(row=2,column=3)
bnbpriceLabel.grid(row=3,column=3)
adapriceLabel.grid(row=4,column=3)

#Coin 24 hour change %
btcchange1Label = Label(root,text=str(btcchange1) + "%")
ethchange1Label = Label(root,text=str(ethchange1) + "%")
bnbchange1Label = Label(root,text=str(bnbchange1) + "%")
adachange1Label = Label(root,text=str(adachange1) + "%")

#Coin 24 hour change %
btcchange1Label.grid(row=1,column=4)
ethchange1Label.grid(row=2,column=4)
bnbchange1Label.grid(row=3,column=4)
adachange1Label.grid(row=4,column=4)

#Coin Market cap Label/format as usd currency
btcmcapLabel = Label(root,text="${:,.2f}". format(btcmcap))
ethmcapLabel = Label(root,text="${:,.2f}". format(ethmcap))
bnbmcapLabel = Label(root,text="${:,.2f}". format(bnbmcap))
adamcapLabel = Label(root,text="${:,.2f}". format(adamcap))

#Coin Market cap Label Placement
btcmcapLabel.grid(row=1,column=5)
ethmcapLabel.grid(row=2,column=5)
bnbmcapLabel.grid(row=3,column=5)
adamcapLabel.grid(row=4,column=5)








root.mainloop()
