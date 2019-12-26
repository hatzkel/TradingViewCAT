# TradingviewCAT (CatchAndThrow)

## What is TradingViewCAT?
TradingViewCAT is a way to take a tradingview alert and using the ccxt library it will send an order to  an exchange.
Using this application you can create triggers for placing orders, stop loss, scaled orders and use TradingView alert system 
to even create complex strategies.





## What TradingviewCAT does not do?
Now the one thing this will not do is take a TradingView strategy and utilize it as an alert becaues they do not have alerts built in.
If you have access to the underlying strategies script sometimes you can take the signal used such EMA crossovers and set an alertcondition on the crossover but this is beyond the scope of this application.


## Instructions
You will either need to have firewall settings that allow the webhook to be sent the host or use ngrok.
Please download ngrok. Otherwise you will have to configure your firewall to allow the webhooks to be received by the host running
this application.


1. ./.env/Scripts/activate to activate the virtual env with the required packages to run this application.
2. Run alert.py to generate the message to be pasted into TradingView when the alert is triggered.
4. Copy and paste the message into the message field of the alert you wish to use in TradingView.
5. Run webhook.py 
6. Profit
7. ???

