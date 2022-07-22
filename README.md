# Webex-Bot-with-Websockets
Basic example of a Webex bot that uses Websockets to communicate with the cloud. Great for testing and 'behind the firewall' deployments.

<img src="https://github.com/DJF3/My-Image-Repo/blob/main/webex-python-bot-ws.jpg?raw=true" width="650px" style="padding-left:50px;"/>

**Time to setup**: if you have setup a bot and have Python installed you can get this to work in 5-10 minutes.

**A Prepare**
- Create a bot (on [developer.webex.com](https://developer.webex.com))
- Download the code (above)
- Check if you have python: ```python -V```    The version should be 3.9 or higher
- Check if you have pip: ```python -m pip -V```    'pip' is used to install Python libraries

**B Create a folder**** for the bot and copy the bot files to this folder
- ```mkdir webex-bot-ws```
- ```cd webex-bot-ws```
- copy bot files to this folder (webexwebsocket.py, webex-bot-ws.py) (When using Pipenv, also copy "Pipfile")


______________ *BELOW: C/D/E/F only if you use Pipenv* ______________

**C Install "Pipenv"** (if not installed)
- Check if you have pipenv: ```pipenv -V```
- If not, install it: ```python -m pip install pipenv```


**D Create Pipfile** (***or use the provided Pipfile***)
- (Mac) ```touch Pipfile``` (or create a file called "Pipfile")
- Edit ```Pipfile```
- Paste content below in the Pipfile and save it. The folder now contains 1 file: "Pipfile" and Pipenv is ready to do its job.

```source
url = "https://pypi.python.org/simple"
verify_ssl = true
name = "webex-bot-using-websocket"
[dev-packages]
[packages]
uuid = "*"
webexteamssdk = "*"
websockets = "*"
[requires]
python_version = "3.9"
```

**E Setup virtual environment**
- ```Pipenv install```
- Based on the Pipfile, this creates a local environment with the required packages.

**F Activate the created virtual environment**
- ```Pipenv shell```
- Your prompt changes to indicate you are in the "isolated" setup.

NOTE: When you start the bot, you need to be in the Pipenv shell. Otherwise, it will not have the right libraries available.
alternatively: type ```pipenv run python webex-bot-ws.py```
This directly runs the python code inside the pipenv environment. 

______________ *ABOVE: C/D/E/F only if you use Pipenv* ______________

**G Set bot token environment variable**
- (MacOS): ```export MY_BOT_TOKEN='YOUR_TOKEN_HERE'```
- (Windows): ```set MY_BOT_TOKEN=YOUR_TOKEN_HERE```


**H Run the Bot** (Python code)
- ```python webex-bot-ws.py```
- When the ```___Bot_started_____``` message appears, test the bot!


**I Test the bot**
- Send ```test``` to the bot.
- It should repeat your message.
- Send ```hello``` to the bot. The not should respond differently.

# FAQ

- **Does this work inside the corporate firewall?** Yes, it most likely will!

- **I don't want to/can use Websockets** check out my alternative solution: [Webex Bot using Ngrok](https://github.com/DJF3/Webex-Bot-with-Ngrok)


# More Webex Development resources?

Article: "[Using Websockets with the Webex JavaScript SDK](https://developer.webex.com/blog/using-websockets-with-the-webex-javascript-sdk)"

Go to [cs.co/webexdevinfo](http://cs.co/webexdevinfo)
