from threading import Thread
from challenge.coinbase import Coinbase

def main():
    thread = Thread(target=Coinbase.Coinbase.websocket_connect)
    keepAlive = Thread(target=Coinbase.coinbase.websocket_keep)
    thread.start()

if __name__ == "__main__":
    main()