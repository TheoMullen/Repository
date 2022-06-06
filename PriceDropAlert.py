import requests
from bs4 import BeautifulSoup
from smtplib import SMTP

link = "https://www.amazon.com/Bose-SoundLink-Bluetooth-Portable-Waterproof/dp/B099TJGJ91/ref=sr_1_3?crid=3L3SOOEEY2474&keywords=bose%2Bspeaker%2Bflex&qid=1654521258&sprefix=bose%2Bspeaker%2Bfle%2Caps%2C219&sr=8-3&th=1"
header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15",
            "Accept_Language": "en-us"}

response = requests.get(link, headers=header)
print(response)
data = response.text
soup = BeautifulSoup(data, "html.parser")
section = soup.select(".a-offscreen")
price_str = section[0].text
price = float(price_str[1:])



if price <= 100:

    my_email = "tjmtestemail@gmail.com"
    password = PASSWORD
    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="theo.mullen2012@gmail.com",
                            msg=f"Subject:Price Drop\n\nThe price is now ${price}.\n{link}")
