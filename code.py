from tkinter import *
import requests
import json

#Create root window/give attributes
root = Tk()
root.geometry('600x600')
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
ethrank = api[1]['market_cap_rank']

#bnb
bnbname = api[2]['name']
bnbsymbol = api[2]['symbol']
bnbprice = api[2]['current_price']
bnb_msupply = api[2]['max_supply']
bnbmcap = api[2]['market_cap']
bnbchange1 = api[2]['price_change_percentage_24h']
bnbchange2 = api[2]['price_change_24h']
bnbrank = api[2]['market_cap_rank']

#ada
adaname = api[3]['name']
adasymbol = api[3]['symbol']
adaprice = api[3]['current_price']
ada_msupply = api[3]['max_supply']
adamcap = api[3]['market_cap']
adachange1 = api[3]['price_change_percentage_24h']
adachange2 = api[3]['price_change_24h']
adarank = api[3]['market_cap_rank']

#c5
c5name = api[4]['name']
c5symbol = api[4]['symbol']
c5price = api[4]['current_price']
c5_msupply = api[4]['max_supply']
c5mcap = api[4]['market_cap']
c5change1 = api[4]['price_change_percentage_24h']
c5change2 = api[4]['price_change_24h']
c5rank = api[4]['market_cap_rank']

#c6
c6name = api[5]['name']
c6symbol = api[5]['symbol']
c6price = api[5]['current_price']
c6_msupply = api[5]['max_supply']
c6mcap = api[5]['market_cap']
c6change1 = api[5]['price_change_percentage_24h']
c6change2 = api[5]['price_change_24h']
c6rank = api[5]['market_cap_rank']

#c7
c7name = api[6]['name']
c7symbol = api[6]['symbol']
c7price = api[6]['current_price']
c7_msupply = api[6]['max_supply']
c7mcap = api[6]['market_cap']
c7change1 = api[6]['price_change_percentage_24h']
c7change2 = api[6]['price_change_24h']
c7rank = api[6]['market_cap_rank']

#c8
c8name = api[7]['name']
c8symbol = api[7]['symbol']
c8price = api[7]['current_price']
c8_msupply = api[7]['max_supply']
c8mcap = api[7]['market_cap']
c8change1 = api[7]['price_change_percentage_24h']
c8change2 = api[7]['price_change_24h']
c8rank = api[7]['market_cap_rank']

#c9
c9name = api[8]['name']
c9symbol = api[8]['symbol']
c9price = api[8]['current_price']
c9_msupply = api[8]['max_supply']
c9mcap = api[8]['market_cap']
c9change1 = api[8]['price_change_percentage_24h']
c9change2 = api[8]['price_change_24h']
c9rank = api[8]['market_cap_rank']

#c10
c10name = api[9]['name']
c10symbol = api[9]['symbol']
c10price = api[9]['current_price']
c10_msupply = api[9]['max_supply']
c10mcap = api[9]['market_cap']
c10change1 = api[9]['price_change_percentage_24h']
c10change2 = api[9]['price_change_24h']
c10rank = api[9]['market_cap_rank']

#-----------------------------------------------------------------------------------------------------------------------

#top label
maintitle = Label(root,text="CoinWolf",font=("Helvetica",25),bg="green",fg="white")
maintitle.grid(row=0,column=1,columnspan=7,ipadx=100)

#indication top levels
rank = Label(root,text="Rank")
name = Label(root,text="Name")
symbol = Label(root,text="Symbol")
price = Label(root,text="Current Price")
change1 = Label(root,text="24h change %")
change2 = Label(root,text="24h change $")
marketcap = Label(root,text="Market Cap")

#indication top levels placement
rank.grid(row=1,column=0)
name.grid(row=1,column=1)
symbol.grid(row=1,column=2)
price.grid(row=1,column=3)
change1.grid(row=1,column=4)
change2.grid(row=1,column=5)
marketcap.grid(row=1,column=6)

#Marketcap Rating
btcrankLabel = Label(root,text="#" + str(btcrank))
ethrankLabel = Label(root,text="#" + str(ethrank))
bnbrankLabel = Label(root,text="#" + str(bnbrank))
adarankLabel = Label(root,text="#" + str(adarank))
c5rankLabel = Label(root,text="#" + str(c5rank))
c6rankLabel = Label(root,text="#" + str(c6rank))
c7rankLabel = Label(root,text="#" + str(c7rank))
c8rankLabel = Label(root,text="#" + str(c8rank))
c9rankLabel = Label(root,text="#" + str(c9rank))
c10rankLabel = Label(root,text="#" + str(c10rank))


#Marketcap Rating Placement
btcrankLabel.grid(row=2,column=0)
ethrankLabel.grid(row=3,column=0)
bnbrankLabel.grid(row=4,column=0)
adarankLabel.grid(row=5,column=0)
c5rankLabel.grid(row=6,column=0)
c6rankLabel.grid(row=7,column=0)
c7rankLabel.grid(row=8,column=0)
c8rankLabel.grid(row=9,column=0)
c9rankLabel.grid(row=10,column=0)
c10rankLabel.grid(row=11,column=0)

#Coin name labels
btcnameLabel = Label(root,text=btcname)
ethnameLabel = Label(root,text=ethname)
bnbnameLabel = Label(root,text=bnbname)
adanameLabel = Label(root,text=adaname)
c5nameLabel = Label(root,text=c5name)
c6nameLabel = Label(root,text=c6name)
c7nameLabel = Label(root,text=c7name)
c8nameLabel = Label(root,text=c8name)
c9nameLabel = Label(root,text=c9name)
c10nameLabel = Label(root,text=c10name)

#Coin name label placement
btcnameLabel.grid(row=2,column=1)
ethnameLabel.grid(row=3,column=1)
bnbnameLabel.grid(row=4,column=1)
adanameLabel.grid(row=5,column=1)
c5nameLabel.grid(row=6,column=1)
c6nameLabel.grid(row=7,column=1)
c7nameLabel.grid(row=8,column=1)
c8nameLabel.grid(row=9,column=1)
c9nameLabel.grid(row=10,column=1)
c10nameLabel.grid(row=11,column=1)

#Coin Symbol Labels
btcsymbolLabel = Label(root,text=btcsymbol)
ethsymbolLabel = Label(root,text=ethsymbol)
bnbsymbolLabel = Label(root,text=bnbsymbol)
adasymbolLabel = Label(root,text=adasymbol)
c5symbolLabel = Label(root,text=c5symbol)
c6symbolLabel = Label(root,text=c6symbol)
c7symbolLabel = Label(root,text=c7symbol)
c8symbolLabel = Label(root,text=c8symbol)
c9symbolLabel = Label(root,text=c9symbol)
c10symbolLabel = Label(root,text=c10symbol)

#Coin Symbol Label Placement
btcsymbolLabel.grid(row=2,column=2)
ethsymbolLabel.grid(row=3,column=2)
bnbsymbolLabel.grid(row=4,column=2)
adasymbolLabel.grid(row=5,column=2)
c5symbolLabel.grid(row=6,column=2)
c6symbolLabel.grid(row=7,column=2)
c7symbolLabel.grid(row=8,column=2)
c8symbolLabel.grid(row=9,column=2)
c9symbolLabel.grid(row=10,column=2)
c10symbolLabel.grid(row=11,column=2)


#Coin Current Price Label/format as usd currency
btcpriceLabel = Label(root,text="${:,.2f}". format(btcprice))
ethpriceLabel = Label(root,text="${:,.2f}". format(ethprice))
bnbpriceLabel = Label(root,text="${:,.2f}". format(bnbprice))
adapriceLabel = Label(root,text="${:,.2f}". format(adaprice))
c5priceLabel = Label(root,text="${:,.2f}". format(c5price))
c6priceLabel = Label(root,text="${:,.2f}". format(c6price))
c7priceLabel = Label(root,text="${:,.2f}". format(c7price))
c8priceLabel = Label(root,text="${:,.2f}". format(c8price))
c9priceLabel = Label(root,text="${:,.2f}". format(c9price))
c10priceLabel = Label(root,text="${:,.2f}". format(c10price))

#Coin Current Price Label Placement
btcpriceLabel.grid(row=2,column=3)
ethpriceLabel.grid(row=3,column=3)
bnbpriceLabel.grid(row=4,column=3)
adapriceLabel.grid(row=5,column=3)
c5priceLabel.grid(row=6,column=3)
c6priceLabel.grid(row=7,column=3)
c7priceLabel.grid(row=8,column=3)
c8priceLabel.grid(row=9,column=3)
c9priceLabel.grid(row=10,column=3)
c10priceLabel.grid(row=11,column=3)


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
btcchange1Label.grid(row=2,column=4)
ethchange1Label.grid(row=3,column=4)
bnbchange1Label.grid(row=4,column=4)
adachange1Label.grid(row=5,column=4)

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
btcchange2Label.grid(row=2,column=5)
ethchange2Label.grid(row=3,column=5)
bnbchange2Label.grid(row=4,column=5)
adachange2Label.grid(row=5,column=5)

#Coin Market cap Label/format as usd currency
btcmcapLabel = Label(root,text="${:,.2f}". format(btcmcap))
ethmcapLabel = Label(root,text="${:,.2f}". format(ethmcap))
bnbmcapLabel = Label(root,text="${:,.2f}". format(bnbmcap))
adamcapLabel = Label(root,text="${:,.2f}". format(adamcap))

#Coin Market cap Label Placement
btcmcapLabel.grid(row=2,column=6)
ethmcapLabel.grid(row=3,column=6)
bnbmcapLabel.grid(row=4,column=6)
adamcapLabel.grid(row=5,column=6)

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

