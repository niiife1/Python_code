import webbrowser as wb

def web_automation():
    chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
    URLS = ('Gsmarena.com' , 'youtube.com' , 'softuni.bg' , 'emag.bg')
    for url in URLS:
        print('Opening' + url)
        wb.get(chrome_path).open(url)
web_automation()
