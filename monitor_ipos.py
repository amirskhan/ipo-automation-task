import os
import requests
from datetime import datetime
import smtplib
from email.message import EmailMessage

# 1. Setup Configuration
FINNHUB_API_KEY = os.environ.get('FINNHUB_API_KEY')
EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS') 
RECEIVER_EMAIL = os.environ.get('EMAIL_USER') 

def get_ipo_data():
    today = datetime.now().strftime('%Y-%m-%d')
    # Finnhub IPO calendar endpoint
    url = f"https://finnhub.io/api/v1/calendar/ipo?from={today}&to={today}&token={FINNHUB_API_KEY}"
    response = requests.get(url)
    return response.json().get('ipoCalendar', [])

def filter_ipos(ipo_list):
    selected_tickers = []
    for ipo in ipo_list:
        # Offer Amount = (Number of Shares) * (Offer Price)
        # Some APIs provide 'numberOfShares' and 'price'
        shares = ipo.get('numberOfShares', 0)
        price = ipo.get('price', 0)
        
        # Ensure values are not None/Zero before calculating
        if shares and price:
            offer_amount = float(shares) * float(price)
            if offer_amount > 200000000:
                selected_tickers.append(f"{ipo['symbol']} (Value: ${offer_amount:,.2f})")
    return selected_tickers

def send_email(tickers):
    msg = EmailMessage()
    msg['Subject'] = f"IPO Alert: High-Value Tickers for {datetime.now().strftime('%Y-%m-%d')}"
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = RECEIVER_EMAIL
    
    body = "The following IPOs today have an offer amount > $200M:\n\n"
    body += "\n".join(tickers) if tickers else "No IPOs met the criteria today."
    msg.set_content(body)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

if __name__ == "__main__":
    ipos = get_ipo_data()
    matches = filter_ipos(ipos)
    send_email(matches)
