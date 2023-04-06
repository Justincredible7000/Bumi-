
#Imports the CCXT module
import ccxt

#Creates variables that connect to the different crypto exchanges 
bitfinex=ccxt.bitfinex()
binance=ccxt.binance() 
kraken=ccxt.kraken({
    'apiKey': 's9mXDUbOmTjleTWGY3SBDUvcRLeHUxyAO0fLD3JNGIN6+PWGVvwViZgc',
    'secret': 'DZVRwPEYJtVphOtNBa2RuH+GqRSdMypaEgVZ5X9vnZgWKS962pm/jS6RzSDiF87NrrQaAGXzMVh8DlpkvkRM1Q==',
})
coinbase=ccxt.coinbase({
    'apiKey': 'hNWmGHC9hvfEkijL',
    'secret': 'SUQSYO5d1tTdJUwn7tdVvFGD7GaoWNHw',
    'createMarketBuyOrderRequiresPrice': False
})
gemini=ccxt.gemini()
kucoin=ccxt.kucoin({
    'apiKey': '6423ca1b6a3d73000123d14c',
    'secret': 'c930aec5-56e6-46ae-ab13-c461fe24c296',
    
    }   )
Pairs=['BTC/USD','ETH/USD','BNB/USD','ADA/USD','DOGE/USD','XRP/USD','DOT/USD','UNI/USD','BCH/USD','LTC/USD','LINK/USD','MATIC/USD','THETA/USD','XLM/USD','VET/USD','ATOM/USD','AAVE/USD','FIL/USD','EOS/USD','NEO/USD','KSM/USD','SNX/USD','MKR/USD','ICP/USD','SOL/USD','TRX/USD','XTZ/USD','FTT/USD','BAT/USD','ALGO/USD','HBAR/USD','ZEC/USD','COMP/USD','YFI/USD','GRT/USD','IOST/USD','LUNA/USD','AVAX/USD','ENJ/USD','OMG/USD','MANA/USD','ZIL/USD','WAVES/USD','REN/USD','DGB/USD','CHZ/USD','CVC/USD','ZRX/USD','BTG/USD','LSK/USD']
#Creates list to store all arbitrage oppertunity 
ROIcount=[]
#Variable that keeps the program running 
Process=True
#Function for finding if there is an arbitrage oppertunity on a specific exchange 
def arbitrage(exchange,pair):
    try:
        #Gets bid and ask prices from exchange for a specific pair
        bid=exchange.fetch_ticker(pair)['bid']
        ask=exchange.fetch_ticker(pair)['ask']
        print("Bid: "+str(bid))
        print("Ask: " +str(ask))
        #If Bid is higher than Ask an arbirtrage oppertunity is avalible 
        if bid>ask:
            print(("Sell on "+exchange +" for "+str(bid)))
        #If not oppertunity is avalible print message 
        else:
            print("No arbitrage avalible at this time")
    #Catches errors releated to bad symbol
    except ccxt.BadSymbol:
        print("Pair not avalible")
#Function for finding if there is an arbitrage oppertunity between two exchanges 
def compareprice(exchange1,exchange2,pair):
    try:
        #Prints pair being used in comparision
        print(str(pair))
        #Gets last avalible price from exchanges 
        Ticker1=exchange1.fetch_ticker(pair) 
        Ticker2=exchange2.fetch_ticker(pair) 
        #Prints prices 
        print(str(exchange1)+" "+str(Ticker1['last']))
        print(str(exchange2)+" "+str(Ticker2['last']))
        # If 1st exchange is greater than 2nd exchange 
        if Ticker1['last']<Ticker2['last']:
            #Prints arbitrage oppertunity 
            print("Arbitrage Oppertunity avalible Buy on "+ str(exchange1)+" and sell on "+str(exchange2))
            #Prints ROI of arbitrage 
            ROI=Ticker2['last']-Ticker1['last']
            print(ROI)
            #Adds trade to ROI list 
            ROIcount.append({
                "Buy": (exchange1),
                "Sell": (exchange2),
                "Pair":pair,
                "ROI": ROI})
         # If 2nd exchange is greater than 1st exchange 
        elif Ticker2['last']<Ticker1['last']:
            print("Arbitrage Oppertunity avalible Buy on "+ str(exchange2)+" and sell on "+str(exchange1))
            ROI=Ticker1['last']-Ticker2['last']
            print(ROI)
            ROIcount.append({
                "Buy": (exchange2),
                "Sell": (exchange1),
                "Pair":pair,
                "ROI": ROI})
        # If price is the same print no oppertunity 
        else:
            print("No arbitrage avalible at this time")
    #Catches errors releated to bad symbol
    except ccxt.BadSymbol:
        print("Pair not avalible")  

#While user hasn't stopped arbitrage program 
while Process==True:
    #Prompts user to enter exchanges to test 
    E1=input("What exchange would like to test(Kraken,Binance,Coinbase,Bitfinex,Gemini,Kucoin) ")
    E2=input("What other exchange would like to test(Kraken,Binance,Coinbase,Bitfinex,Gemini,Kucoin) ")
    #Prompts user to enter pair to use
    P=input("What Pair would you like to use ")
    #Matches exchange string to exchange variable 
    if E1=="Kraken":
        E1=kraken
    if E1=="Coinbase":
        E1=coinbase
    if E1=="Gemini":
        E1=gemini
    if E1=="Binance":
        E1=binance
    if E1=="Bitfinex":
        E1=bitfinex
    if E1=="Kucoin":
        E1=kucoin
    if E2=="Kraken":
        E2=kraken
    if E2=="Coinbase":
        E2=coinbase
    if E2=="Gemini":
        E2=gemini
    if E2=="Binance":
        E2=binance
    if E2=="Bitfinex":
        E2=bitfinex
    if E2=="Kucoin":
        E2=kucoin
    #Puts in user exchanges and pair into compare price function
    compareprice(E1, E2, P)
    #Sets Highest ROI to first value in list
    HighestROI=ROIcount[0]
    #Goes through all Trade values and finds highest value
    for x in ROIcount:
        if x ["ROI"]>HighestROI["ROI"]:
            HighestROI=x
    print("Best ROI: " +"Buy on "+str(HighestROI["Buy"])+" Sell on "+str(HighestROI["Sell"])+" Currency "+str(HighestROI["Pair"])+" ROI "+str(HighestROI["ROI"]))
    #Prompts user if they want to implement trade 
    Choice=input("Do you want to test another pair Y/N? ")
    if Choice=="N":
        Process=False
print("Best ROI: " +"Buy on "+str(HighestROI["Buy"])+" Sell on "+str(HighestROI["Sell"])+" Currency "+str(HighestROI["Pair"])+" ROI "+str(HighestROI["ROI"]))
Trade=input("Would you like to make this Trade Y/N? ")

if Trade=="Y":
    #Prompts user to choose how much to buy
    BAmount=input("How much would you like to buy ")
    SAmount=input("How much would you like to sell ")
    
    Type=input("limit or market trade? ")
    if Type=="Market":
        Type="market"
    if Type=="Limit":
        Type="limit"   
    #Gets prices for buying and selling
    Bprice = (HighestROI["Buy"].fetch_ticker(HighestROI["Pair"])['last'])
    
    Sprice = (HighestROI["Sell"].fetch_ticker(HighestROI["Pair"])['last'])
    try:
        #creates buy order 
       BOrder=HighestROI["Buy"].create_order(HighestROI["Pair"], Type, "buy", BAmount,Bprice)
       
       print("Order successfully placed!")
      #Catches insuffencient funds error 
    except ccxt.InsufficientFunds as e:
         print("Insufficient funds to place order.")
    #Catches other errors
    except Exception as e:
            print(f"Error placing order: {e}")
    try:
       #creates sell order
       BOrder=HighestROI["Sell"].create_order(HighestROI["Pair"], Type, "sell", SAmount, Sprice)
       
       print("Order successfully placed!")
    except ccxt.InsufficientFunds as e:
         print("Insufficient funds to place order.")
    except Exception as e:
            print(f"Error placing order: {e}")
#If the user doesn't want to trade end program
if Trade=="N":
    print("Program finished")

