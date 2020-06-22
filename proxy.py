import subprocess, sys, os, urllib.request, requests, datetime, random, time
from pathlib import Path

proxyport = 14808

messages = ["revox knew how to speak estonian back in the day",
  "Bilaboz has some nice girls in the area",
  "Tech1k probably has a nuclear plant in his backyard",
  "Melons. ~Punixz",
  "Science isn't about why. It is about why not!",
  "coca cola oh no",
  "revox can terrorize men and women equally",
  "there are rumours Jacob sits with popcorn and watches DUCO community write in broken english",
  "hypogre still thinks revox syphoons his DUCO",
  "phantom32: suck my balls [while being bubble tea]",
  "fix the code? Na, thanks, I'll just blame how bad python is",
  "pro tip: don't buy AK-47 in the second round",
  "who would win? a complex program or one winky boi;;;;",
  "revox likes (E) - Ekwador Manieczki club",
  "idk what else can I write here"]

while True:
  now = datetime.datetime.now()
  print("\n" + now.strftime("%Y/%m/%d %H:%M:%S")+ " [INFO] Duino-Coin WebSockets Proxy by revox 2020; main GO code by zquestz")
  now = datetime.datetime.now()
  print(now.strftime("%Y/%m/%d %H:%M:%S")+ " [INFO] Random fact: " + random.choice(messages))

  if not Path("ws-tcp-proxy").is_file(): # Check if ws-tcp-proxy is downloaded
    now = datetime.datetime.now()
    print(now.strftime("%Y/%m/%d %H:%M:%S")+ " [INFO] Downloading ws-tcp-proxy")

    url = "https://github.com/revoxhere/duino-coin-websocket-proxy/blob/master/ws-tcp-proxy?raw=true"	
    r = requests.get(url)
    with open("ws-tcp-proxy", "wb") as f:
      f.write(r.content)

    now = datetime.datetime.now()
    print(now.strftime("%Y/%m/%d %H:%M:%S")+ " [INFO] Done")

  now = datetime.datetime.now()
  print(now.strftime("%Y/%m/%d %H:%M:%S")+ " [INFO] Retrieving main server data")

  serverip = "https://raw.githubusercontent.com/revoxhere/duino-coin/gh-pages/serverip.txt" # Well known code to get server IP
  with urllib.request.urlopen(serverip) as content:
    content = content.read().decode().splitlines()
  pool_address = content[0]
  pool_port = content[1]

  now = datetime.datetime.now()
  print(now.strftime("%Y/%m/%d %H:%M:%S")+ " [INFO] Official server is on " + str(pool_address) + ":" + str(pool_port))

  try:
    now = datetime.datetime.now()
    print(now.strftime("%Y/%m/%d %H:%M:%S")+ " [INFO] Binding proxy to port :"+str(proxyport))
    command = "./ws-tcp-proxy "+str(pool_address)+":"+str(pool_port)+" -t -p "+str(proxyport)
    subprocess.call(command, shell=True)
  except:
    now = datetime.datetime.now()
    print(now.strftime("%Y/%m/%d %H:%M:%S")+ " [ERROR] Error in ws-tcp-proxy:", sys.exc_info()[0], sys.exc_info()[1])
