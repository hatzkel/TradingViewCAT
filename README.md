# TradingviewCAT (CatchAndThrow)

## What is TradingViewCAT?
TradingViewCAT is a flask application designed as a way to take a tradingview alert and using the ccxt library and send an order to an exchange.
Using this application you can create triggers for placing orders, stop loss, scaled orders and use TradingView alert system 
to even create complex strategies.





## What TradingviewCAT does not do?
Now the one thing this will not do is take a TradingView strategy and utilize it as an alert becaues they do not have alerts built in.
If you have access to the underlying strategies script sometimes you can take the signal used such EMA crossovers and set an alertcondition on the crossover but this is beyond the scope of this application.


## Instructions
You will either need to have firewall settings that allow the webhook to be sent the host or use ngrok. If you have a VPS this can also
run on AWS free tier just makesure to have your firewall configured to allow it to receive the TV webhooks. Otherwise please download ngrok.
You can also run this on your PC but again you will have to configure your router/firewall to allow access.
this application.



1. Install pipenv `pip install pipenv`
2. Navigate to the folder where you cloned the repo. You should see Pipfile and Pipfile.lock files.
3. Run command `pipenv install`
4. The dependencies required to get started should now be installed. Check by running command pipenv graph - You should see flask and ccxt.
    If you want to install any other dependencies, or if you get an error that you're missing a depedency, simply use command pipenv install <dependency>
    Starting the virtual environment: pipenv shell
    Starting the flask app: python webhook-bot.py

###
Ngrok Signup: https://dashboard.ngrok.com/signup 
_Ngrok is free and does not require an account to but you will be disconnected every 8 hours so please register._
_You can also spin up Ubuntu VPS on AWS free tier and  run this on that host and send the webhooks there, just make sure the firewall is configured correctly._