from pprint import pprint
import smtplib, ssl
import sys, re, logging
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



##!<import pandas as pd
##!<import matplotlib.pyplot as plt
##!<from datetime import datetime

# Raw Package
import numpy as np
import pandas as pd
import argparse

#Data Source
import yfinance as yf

#Data viz
import plotly.graph_objs as go
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
t = "    "
ticker_list = ['NNDM' ,'OPTT' ,'CLSK' ,'LTRX' ,'MARA' ,
               'PXLW' ,'VYNT' ,
               'MOSYX' , 'TRT' ,'GMDA' ,'SCYX' ,
               'EKSO','STXS','HUBC','KSCP','VSTM','INGN','AMSC','RMBL', 'ALIM','DTIL',]
               #'RWLK', 'ITI','MRAM','ISDR','EYPT','CASS','BWAY','DAIO','CYBN',
               #'DCTH','RELL','WATT','MCRB','SENS']

def data_dl():
  data = [
          #yf.download(tickers = 'TTOO' ,period='1d', start='2020-05-05'), ## Reverse split on 10-13-22 sell on 8/30/23
          yf.download(tickers = 'NNDM' ,period='1d', start='2020-06-02'),
          #yf.download(tickers = 'RVP' ,period='1d', start='2020-06-02'),sell on 8/28/23
          #yf.download(tickers = 'IPWR' ,period='1d', start='2020-06-10'), sell on 8/29/23
          yf.download(tickers = 'OPTT' ,period='1d', start='2020-06-16'),
          #yf.download(tickers = 'LTBR' ,period='1d', start='2020-06-16'),sell on 8/29/23
          #yf.download(tickers = 'BIOC' ,period='1d', start='2020-06-16'), ## Reverse split 09-08-2020 sell on 8/24/23
          #yf.download(tickers = 'OCX' ,period='1d', start='2020-08-03'), ## reverse split 07/25-2023 sell on 8/28/23
          #yf.download(tickers = 'SMED' ,period='1d', start='2020-08-07'), ACQUISITION!!
         # yf.download(tickers = 'RIBT' ,period='1d', start='2020-08-25'), sell on 8/24/23
          yf.download(tickers = 'CLSK' ,period='1d', start='2020-09-08'),
          yf.download(tickers = 'LTRX' ,period='1d', start='2020-09-23'),
          yf.download(tickers = 'MARA' ,period='1d', start='2020-09-25'),
          #yf.download(tickers = 'SQNS' ,period='1d', start='2020-10-20'), sell on 8/07/23
          #yf.download(tickers = 'ONVO' ,period='1d', start='2020-10-21'), sell on 8/25/23
          yf.download(tickers = 'PXLW' ,period='1d', start='2020-11-06'),
          #yf.download(tickers = 'HYREQ' ,period='1d', start='2020-11-30'), sell on 3/9/23
          #yf.download(tickers = 'WWR' ,period='1d', start='2020-01-20'),  sell on 8/24/23
  
          #yf.download(tickers = 'SLGG' ,period='1d', start='2021-01-12'), sell on 9/08/23
          #yf.download(tickers = 'PRSO' ,period='1d', start='2021-01-12'), sell on 8/25/23
          #yf.download(tickers = 'ICCC' ,period='1d', start='2021-01-29'), sell on 8/28/23
          yf.download(tickers = 'VYNT' ,period='1d', start='2021-02-25'),
          #yf.download(tickers = 'URG' ,period='1d', start='2021-03-15'),  sell on 8/30/23
          #yf.download(tickers = 'IDXG' ,period='1d', start='2021-04-01'), sell on 8/24/23
          #yf.download(tickers = 'BOXL' ,period='1d', start='2021-04-26'), sell on 8/25/23
         # yf.download(tickers = 'WISA' ,period='1d', start='2021-05-12'), sell on 8/25/23
          #yf.download(tickers = 'PLUR' ,period='1d', start='2021-06-04'), sell on 8/28/23
          #yf.download(tickers = 'WATT' ,period='1d', start='2021-07-30'), sell on 9/06/23
          yf.download(tickers = 'MOSYX' ,period='1d', start='2021-08-04'),
          #yf.download(tickers = 'APDN' ,period='1d', start='2021-10-12'), sell on 8/28/23
          #yf.download(tickers = 'CLXT' ,period='1d', start='2021-10-26'), Delisted
          #yf.download(tickers = 'AQMS' ,period='1d', start='2021-12-06'), sell on 8/30/23
          #yf.download(tickers = 'CBUS' ,period='1d', start='2021-12-22'), sell on 8/30/23
          yf.download(tickers = 'TRT' ,period='1d', start='2021-12-22'),
          yf.download(tickers = 'GMDA' ,period='1d', start='2022-03-01'),
          yf.download(tickers = 'SCYX' ,period='1d', start='2022-03-16'),
          yf.download(tickers = 'EKSO' ,period='1d', start='2023-01-10'),
          yf.download(tickers = 'STXS' ,period='1d', start='2023-02-17'),
          yf.download(tickers = 'HUBC' ,period='1d', start='2023-03-20'),
          yf.download(tickers = 'KSCP' ,period='1d', start='2023-05-26'),
          yf.download(tickers = 'VSTM' ,period='1d', start='2023-06-20'),
          yf.download(tickers = 'INGN' ,period='1d', start='2023-06-27'),
          yf.download(tickers = 'AMSC' ,period='1d', start='2023-07-27'),
          yf.download(tickers = 'RMBL' ,period='1d', start='2023-08-01'),
          #yf.download(tickers = 'WRAP' ,period='1d', start='2022-04-18'), sell on 8/29/23
          #yf.download(tickers = 'EOSE' ,period='1d', start='2022-03-17'), sell on 7/28/23
          #yf.download(tickers = 'VGFCQ' ,period='1d', start='2022-06-08'), sell on 3/09/23
          yf.download(tickers = 'ALIM' ,period='1d', start='2023-08-15'),
          yf.download(tickers = 'DTIL' ,period='1d', start='2023-08-18'),
          #yf.download(tickers = 'HGEN' ,period='1d', start='2023-07-10'), sell on 7/25/23
          #yf.download(tickers = 'APRN' ,period='1d', start='2023-02-03'), Sell APRN — 9/29/23
          #yf.download(tickers = 'RWLK' ,period='1d', start='2020-08-25'),
          #yf.download(tickers = 'ITI' ,period='1d', start='2023-08-24'),
          #yf.download(tickers = 'MRAM' ,period='1d', start='2023-08-28'),
          #yf.download(tickers = 'ISDR' ,period='1d', start='2023-08-29'),
          #yf.download(tickers = 'EYPT' ,period='1d', start='2023-08-30'),
          #yf.download(tickers = 'CASS' ,period='1d', start='2023-09-08'),
          #yf.download(tickers = 'BWAY' ,period='1d', start='2023-09-15'),
          #yf.download(tickers = 'DAIO' ,period='1d', start='2022-09-15'),
          #yf.download(tickers = 'CYBN' ,period='1d', start='2023-11-01'),
          #yf.download(tickers = 'DCTH' ,period='1d', start='2023-09-25'),
          #yf.download(tickers = 'RELL' ,period='1d', start='2023-10-04'),
          # yf.download(tickers = 'AFIB' ,period='1d', start='2022-03-09'), sell on 11/09/2023
          # yf.download(tickers = 'CDLX' ,period='1d', start='2023-09-01'), sell on 11/09/2023
          #yf.download(tickers = 'WATT' ,period='1d', start='2023-11-02'),
          #yf.download(tickers = 'MCRB' ,period='1d', start='2023-11-03'),
          #yf.download(tickers = 'SENS' ,period='1d', start='2023-11-14'),
          ]
  return data

def plot_graphe():
  fig = go.Figure() 
  data = data_dl()
  for line, ticker in zip(data,ticker_list):
    fig.add_trace(go.Candlestick(x = line.index, open = line['Open'], high=line['High'], low=line['Low'], close=line['Close'], name = ticker ))
  
  
  fig.update_layout(title="Candlestick Chart for Multiple Stocks",
                    xaxis_title="Date",
                    yaxis_title="Stock Price",
                    xaxis_rangeslider_visible=True,
                    width=1500,  
                    height=800   
                    )
  
  fig.show()


def Drop():
    content = ""
    for ticker, value in zip(ticker_list, data_dl()):
        first_opening_price = round(value['Open'][0],2)
        latest_market_price = round(value['Close'][-1],2)

        stop_price = round(first_opening_price * 0.85, 2)
        limit_price = round(first_opening_price * 0.8, 2)

        #(New Price - Old Price)/Old Price and then multiply that number by 100
        roc = round(((latest_market_price - first_opening_price) / first_opening_price) * 100,2);    

        #if latest_market_price < first_opening_price * 0.8:
        if roc < 0:
            price_drop = round(first_opening_price - latest_market_price,2)
            print ( "[Obsolete( "+ color.BOLD + ticker + color.END + ")] price drop: " + str(roc) + "%")
            content += ( "[Obsolete( <b>" + ticker + "</b>)] price drop: " + str(roc) + "%" +
                  "   <br>"+t+t+"   Your first opening price was " + str(first_opening_price) +
                  "   <br>"+t+t+"   Your latest market price is " + str(latest_market_price) +
                  "   <br>"+t+t+"   Your price drop is " + str(price_drop) +
                  "   <br>"+t+t+"   Your sell limit price is " + str(limit_price)+
                  "<br>"
                  )
    return content  

def Hike():
    content = ""
    for ticker, value in zip(ticker_list, data_dl()):
        first_opening_price = round(value['Open'][0],2)
        latest_market_price = round(value['Close'][-1],2)

        
        limit_price = round(first_opening_price * 1.6, 2)

        #(New Price - Old Price)/Old Price and then multiply that number by 100
        roc = round(((latest_market_price - first_opening_price) / first_opening_price) * 100,2);    

        #if latest_market_price < first_opening_price * 0.8:
        if roc > 0:
            price_hike = round(latest_market_price - first_opening_price,2)
            content += ("[Obsolete( <b>" + ticker + "</b>)] price hike: " + str(roc) + "%" + 
                  "   <br>"+t+t+"  Your first opening price was " + str(first_opening_price) +
                  "   <br>"+t+t+"  Your price hike is " + str(price_hike) +
                  "   <br>"+t+t+" Your sell limit price is " + str(limit_price) +
                  "<br>")
    return content   
    
'''     
def send_email2():
  parser = argparse.ArgumentParser(description='reciever email')


  parser.add_argument('--email', help='email of the user')


  args = parser.parse_args()


  
  port = 465  # For SSL
  smtp_server = "smtp.gmail.com"
  sender_email = "aaleensyed20@gmail.com"  # Enter your address
  receiver_email = "abbmir@gmail.com"  # Enter receiver address
  #password = 'stct gxna upbz hofd'
  password = "txpw qshd uhvk fdgu"
  
  # stop_price = round(first_opening_price * 0.85, 2)
  # limit_price = round(first_opening_price * 0.8, 2)

  msg = EmailMessage()
  # msg.set_content("Hi \n" + "Your first opening price was " + str(first_opening_price) +
                  # "   \n" + "Your latest market price is " + str(latest_market_price) +
                  # "   \n" + "Your price drop is " + str(price_drop) +
                  # "   \n" + "Your stop price is " + str(stop_price) +
                  # "   \n" + "Your limit price is " + str(limit_price))

  # msg['Subject'] = "[Obsolete(" + ticker + ")] price drop: " + str(roc) + "%"
  msg['From'] = sender_email
  msg['To'] = receiver_email
  

  # content = "List of Tickers:\n"
  # content += decrease()
  

  msg.set_content(content)
  
  context = ssl.create_default_context()
  with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
      server.login(sender_email, password)
      server.send_message(msg, from_addr=sender_email, to_addrs=receiver_email)

def send_email3(first_opening_price, latest_market_price, price_hike, roc, ticker):
  port = 465  # For SSL
  smtp_server = "smtp.gmail.com"
  sender_email = "aaleensyed20@gmail.com"  # Enter your address
  receiver_email = "abbmir@gmail.com"  # Enter receiver address
  password = "txpw qshd uhvk fdgu"
  
  limit_price = round(first_opening_price * 1.6, 2)

  msg = EmailMessage()
  msg.set_content("Hi \n" + "Your first opening price was " + str(first_opening_price) +
                  "   \n" + "Your latest market price is " + str(latest_market_price) +
                  "   \n" + "Your price hike is " + str(price_hike) +
                  "   \n" + "Your sell limit price is " + str(limit_price))

  msg['Subject'] = "[Obsolete(" + ticker + ")] price hike: " + str(roc) + "%"
  msg['From'] = sender_email
  msg['To'] = receiver_email
  
  context = ssl.create_default_context()
  with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
      server.login(sender_email, password)
      server.send_message(msg, from_addr=sender_email, to_addrs=receiver_email)

# fig.add_traces(go.Candlestick(x = data[4].index, open = data[4]['Open'], high=data[4]['High'], low=data[4]['Low'], close=data[4]['Close'], name = 'VSTM'))

# fig.show()
'''

def send_email(email):  
  port = 465  # For SSL
  smtp_server = "smtp.gmail.com"
  sender_email = "aaleensyed20@gmail.com"  # Enter your address
  receiver_email = email  # Enter receiver address
  password = "omaq zcyi swbg nwhd"
  
  msg = MIMEMultipart()
  msg['Subject'] = "[Obsolete(tickers)]"
  msg['From'] = sender_email
  msg['To'] = receiver_email

  content = ""
  content += Hike() + "<br>"
  
  content += Drop()
  

   
  msg.attach(MIMEText(content, 'html'))
  context = ssl.create_default_context()

  with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
      server.login(sender_email, password)
      server.send_message(msg, from_addr=sender_email, to_addrs=receiver_email)


def main():
  parser = argparse.ArgumentParser(epilog="additional position arguments:\n  Specify variable overrides using <NAME>:<VALUE> syntax on command line.",description="Email or Plot Stock hike and drop",formatter_class=argparse.RawDescriptionHelpFormatter)
  #parser.add_argument("flow",metavar="FLOW",help="Required. Specify desired flow. Use --list_flows to see available flows",default="UNSPECIFIED",nargs="?")
  parser.add_argument("--email","-e",help="Specify your e-mail address", default=None)
  parser.add_argument("--plot","-p",help="Plot tickers on browser",action='store_true',default=False)
  args,option_overrides = parser.parse_known_args()
  logger = logging.getLogger("logger")
  # Check the option overrides array for any unknown arguments. Anything starting with a dash (-) is an unknown switch, not 
  # an override
  for o in option_overrides:
    if re.match(r'^-',o):
      logger.error("Unknown command line argument \"{}\"".format(o))
      parser.print_help()
      sys.exit(1)
  if args.plot:
     plot_graphe()
  elif args.email:
     send_email(args.email)
     

  
  #!<for line, ticker in zip(data,ticker_list):
  #!<     # starting_price = line['Close'][0]  
  #!<      #ending_price = line['Close'][-1]   
#!<
  #!<      #for o in line['Open']:
  #!<      #   print (str(o) + " for " + ticker)
#!<
  #!<      #if ending_price < starting_price:
  #!<      first_opening_price = line['Open'][0]
  #!<      latest_market_price = line['Close'][-1]
  #!<      
  #!<      #(New Price - Old Price)/Old Price and then multiply that number by 100
  #!<      roc = ((latest_market_price - first_opening_price) / first_opening_price) * 100;    
#!<
  #!<      #if(latest_market_price < first_opening_price*0.8):
  #!<      if roc < 0:
  #!<         print("Opening price drop found on ticker ", ticker)
  #!<         price_drop = first_opening_price - latest_market_price
  #!<         send_email2( round(first_opening_price,3),round(latest_market_price,3),round(price_drop,3), round(roc,3), ticker)
  #!<      #if(latest_market_price * 0.90 > first_opening_price):
  #!<      if roc >= 0:
  #!<         print("Opening price hike found on ticker ", ticker)
  #!<         price_hike = latest_market_price - first_opening_price
  #!<         send_email3( round(first_opening_price,3),round(latest_market_price,3),round(price_hike,3), round(roc,3), ticker)
  #!<      
  #!<      #fig.add_trace(go.Candlestick(x = line.index, open = line['Open'], high=line['High'], low=line['Low'], close=line['Open'], name = ticker ))
#!<
  #!<    # fig.add_trace(go.Candlestick(
  #!<    #     x=list.index[n:],  
  #!<    #     open=list['Open'], 
  #!<    #     high=list['High'], 
  #!<    #     low=list['Low'], 
  #!<    #     close=list['Close'], 
  #!<    #     name=ticker
  #!<    
  #!<    # ))
  #!<    
  #!<
  #!<
  #!<
# #!<  fig.update_traces(selector=dict(name = 'APRN'),  increasing_line=dict(color='indigo'),   increasing_fillcolor = 'indigo',    decreasing_line=dict(color='firebrick'),  decreasing_fillcolor = 'firebrick')
  #!<                  
  #!<
  #!<
  #!<
  #!<#fig.update_layout(title="Candlestick Chart for Multiple Stocks",
  #!<#                  xaxis_title="Date",
  #!<#                  yaxis_title="Stock Price",
  #!<#                  xaxis_rangeslider_visible=True)
  #!<
  #!<
  #!<#fig.show()

if __name__ == "__main__":
     main()
     #send_email()
     #send_email2()


