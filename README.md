# duino-coin-websocket-proxy
Duino-Coin Websocket Proxy Server

# Installation
```bash
sudo apt install git python3
git clone https://github.com/revoxhere/duino-coin-websocket-proxy
cd duino-coin-websocket-proxy
sudo chmod 777 *
python3 proxy.py
```
After successfull install and launch go to your router settings and you'll need to forward duco proxy port (default is **14808**) - make sure you have firewall and ddos protection enabled in your router (but it should be enabled by default) to prevent any potential spammers.

# Credits
zquestz's GO proxy code: https://github.com/zquestz/ws-tcp-proxy
