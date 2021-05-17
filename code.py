from tkinter import *
import requests
import json

#Create root window/give attributes
root = Tk()
root.geometry('500x400')
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
btcchange2 = api[0]['price_change_24h']
btcrank = api[0]["market_cap_rank"]

#eth
ethname = api[1]['name']
ethsymbol = api[1]['symbol']
ethprice = api[1]['current_price']
eth_msupply = api[1]['max_supply']
ethmcap = api[1]['market_cap']
ethchange1 = api[1]['price_change_percentage_24h']
ethchange2 = api[1]['price_change_24h']

#bnb
bnbname = api[2]['name']
bnbsymbol = api[2]['symbol']
bnbprice = api[2]['current_price']
bnb_msupply = api[2]['max_supply']
bnbmcap = api[2]['market_cap']
bnbchange1 = api[2]['price_change_percentage_24h']
bnbchange2 = api[2]['price_change_24h']

#ada
adaname = api[3]['name']
adasymbol = api[3]['symbol']
adaprice = api[3]['current_price']
ada_msupply = api[3]['max_supply']
adamcap = api[3]['market_cap']
adachange1 = api[3]['price_change_percentage_24h']
adachange2 = api[3]['price_change_24h']

#-----------------------------------------------------------------------------------------------------------------------

#top label
maintitle = Label(root,text="CoinWolf",font=("Helvetica",25),bg="green",fg="white")
maintitle.grid(row=0,column=1,columnspan=7,ipadx=100)

#Marketcap Rating
btcrankLabel = Label(root,text="#" + str(btcrank))

#Marketcap Rating Placement
btcrankLabel.grid(row=1,column=0)

#Coin name labels
btcnameLabel = Label(root,text=btcname)
ethnameLabel = Label(root,text=ethname)
bnbnameLabel = Label(root,text=bnbname)
adanameLabel = Label(root,text=adaname)

#Coin name label placement
btcnameLabel.grid(row=1,column=1)
ethnameLabel.grid(row=2,column=1)
bnbnameLabel.grid(row=3,column=1)
adanameLabel.grid(row=4,column=1)

#Coin Symbol Labels
btcsymbolLabel = Label(root,text=btcsymbol)
ethsymbolLabel = Label(root,text=ethsymbol)
bnbsymbolLabel = Label(root,text=bnbsymbol)
adasymbolLabel = Label(root,text=adasymbol)

#Coin Symbol Label Placement
btcsymbolLabel.grid(row=1,column=2)
ethsymbolLabel.grid(row=2,column=2)
bnbsymbolLabel.grid(row=3,column=2)
adasymbolLabel.grid(row=4,column=2)

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
if btcchange1 < 0:
    btcchange1Label = Label(root, text=str(btcchange1) + "%", fg="red")
else:
    btcchange1Label = Label(root, text=str(btcchange1) + "%", fg="green")

if ethchange1 < 0:
    ethchange1Label = Label(root, text=str(ethchange1) + "%", fg="red")
else:
    ethchange1Label = Label(root, text=str(ethchange1) + "%", fg="green")

if bnbchange1 < 0:
    bnbchange1Label = Label(root, text=str(bnbchange1) + "%", fg="red")
else:
    bnbchange1Label = Label(root, text=str(bnbchange1) + "%", fg="green")

if adachange1 < 0:
    adachange1Label = Label(root, text=str(adachange1) + "%", fg="red")
else:
    adachange1Label = Label(root, text=str(adachange1) + "%", fg="green")


#Coin 24 hour change % Placement
btcchange1Label.grid(row=1,column=4)
ethchange1Label.grid(row=2,column=4)
bnbchange1Label.grid(row=3,column=4)
adachange1Label.grid(row=4,column=4)

#Coin 24 hour change $
if btcchange2 < 0:
    btcchange2Label = Label(root, text="${:,.2f}". format(btcchange2),fg="red")
else:
    btcchange2Label = Label(root, text="${:,.2f}". format(btcchange2),fg="red")

if ethchange2 < 0:
    ethchange2Label = Label(root, text="${:,.2f}". format(ethchange2),fg="red")
else:
    ethchange2Label = Label(root, text="${:,.2f}". format(ethchange2),fg="green")

if bnbchange2 < 0:
    bnbchange2Label = Label(root, text="${:,.2f}". format(bnbchange2),fg="red")
else:
    bnbchange2Label = Label(root, text="${:,.2f}". format(bnbchange2),fg="green")

if adachange1 < 0:
    adachange2Label = Label(root, text="${:,.2f}". format(adachange2),fg="red")
else:
    adachange2Label = Label(root, text="${:,.2f}". format(adachange2),fg="green")

#Coin 24 hour change $ Placement
btcchange2Label.grid(row=1,column=5)
ethchange2Label.grid(row=2,column=5)
bnbchange2Label.grid(row=3,column=5)
adachange2Label.grid(row=4,column=5)

#Coin Market cap Label/format as usd currency
btcmcapLabel = Label(root,text="${:,.2f}". format(btcmcap))
ethmcapLabel = Label(root,text="${:,.2f}". format(ethmcap))
bnbmcapLabel = Label(root,text="${:,.2f}". format(bnbmcap))
adamcapLabel = Label(root,text="${:,.2f}". format(adamcap))

#Coin Market cap Label Placement
btcmcapLabel.grid(row=1,column=6)
ethmcapLabel.grid(row=2,column=6)
bnbmcapLabel.grid(row=3,column=6)
adamcapLabel.grid(row=4,column=6)

#Create Button to open 2nd window to display chart
def open():
    top = Toplevel()
    top.geometry('500x400')
    top.title("Chart")
    label=Label(top,text="Hello World!")
    label.pack()
    btn2= Button(top, text="close window", command=top.destroy)
    btn2.pack()


btcbtn = Button(root,text="view chart",command=open)
btcbtn.grid(row=1,column=7)















root.mainloop()

