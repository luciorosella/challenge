import json, time, os
from threading import Thread
from websocket import create_connection, WebSocketConnectionClosedException
from dotenv import load_dotenv
from challenge.messages import Messages

load_dotenv()

class Coinbase:
    def __init__(self):
        self.thread = None
        self.keepAlive = None

    def websocket_connect():
        global webSocket

        webSocket = create_connection(os.getenv('UrlCoinbase'))
        webSocket.send(json.dumps({
                "type": os.getenv('Type'),
                "product_ids": json.loads(os.getenv('Pairs')),
                "channels": json.loads(os.getenv('Channel')),
            })
        )

        return webSocket

    def processWebSocket(webSocket):
        while True:
            try:
                data = webSocket.recv()
                if data != "":
                    msg = Messages(json.loads(data))
                else:
                    msg = {}
            except ValueError as e:
                print(e)
            except Exception as e:
                print(e)
            else:
                if "Result" not in msg:
                    print(msg)

        try:
            if webSocket:
                webSocket.close()
        except WebSocketConnectionClosedException:
            pass
        finally:
            keepAlive.join()

    def websocket_keep(interval=30):
        global webSocket
        while webSocket.connected:
            webSocket.ping("keepAlive")
            time.sleep(interval)
