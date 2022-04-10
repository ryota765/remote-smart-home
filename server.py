import os
import requests
import json
from dotenv import load_dotenv

from argparse import ArgumentParser
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

import send_signal

load_dotenv()
app = Flask(__name__)

channel_secret = os.getenv("CHANNEL_SECRET")
channel_access_token = os.getenv("CHANNEL_ACCESS_TOKEN")
OPTION_FILE = "options/light_options.json"

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

json_open = open(OPTION_FILE, "r")
options_dict = json.load(json_open)


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = event.message.text

    if message in options_dict:
        send_signal.main(options_dict[message])

        line_bot_api.reply_message(event.reply_token, TextSendMessage("Done!"))

    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(f"Available options are: {list(options_dict.keys())}"),
        )


if __name__ == "__main__":
    arg_parser = ArgumentParser(
        usage="Usage: python " + __file__ + " [--port ] [--help]"
    )
    arg_parser.add_argument("-p", "--port", default=8080, help="port")
    arg_parser.add_argument("-d", "--debug", default=False, help="debug")
    options = arg_parser.parse_args()

    app.run(debug=options.debug, port=options.port)
