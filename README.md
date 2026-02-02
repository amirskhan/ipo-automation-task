# Daily IPO Monitor Automation

This repository contains an automated workflow designed to monitor the U.S. stock market for high-value IPOs. The system identifies upcoming IPOs scheduled for the current day with an offer amount exceeding **USD 200 Million** and sends an automated email notification.

## Features

* **Real-time Monitoring:** Fetches daily IPO data via the Finnhub API.
* **Threshold Filtering:** Automatically calculates the offer amount () and filters for tickers above $200M.
* **Scheduled Execution:** Runs daily at **9:00 AM Dubai Time (GST)** using GitHub Actions.
* **Secure Credential Management:** Utilizes GitHub Secrets for API keys and SMTP credentials.

## Technical Stack

**Language:** Python 3.9 

**Automation:** GitHub Actions (Cron) 

**Communication:** SMTP via `smtplib`

**Data Source:** Finnhub IPO Calendar API

## Setup & Installation

1. **Clone the repository:**
```bash
git clone https://github.com/amirskhan/ipo-automation-task.git

```


2. **Install Dependencies:**
```bash
pip install requests

```


3. **Configure Environment Variables:**
The script requires the following secrets to be configured in GitHub Actions:
* `FINNHUB_API_KEY`: API access token.
* `EMAIL_USER`: Sender email address.
* `EMAIL_PASS`: App-specific password for the email provider.



## Automation Schedule

The workflow is triggered via a cron schedule:

* **Schedule:** `0 5 * * *` (5:00 AM UTC / 9:00 AM GST)
