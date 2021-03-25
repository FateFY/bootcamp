
```
get-hotfix
```

```
winver
```

```
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
```

```
choco install python3 --version=3.8.2
```

```
choco install googlechrome
```

```
choco install jenkins
```

### Schtasks

**A scheduled task runs every 20 mins by using schetasks**
```
schtasks /create /sc minute /mo 20 /tn "NewFRScraper" /tr "C:\python_apps\afr-scraper\afr_new_article_scrape.bat"
```

**A scheduled task runs everyday at 1AM by using schetasks**

```
schtasks /create /sc DAILY /tn "FRDailyTickerScraper" /tr "C:\python_apps\afr-scraper\afr_daily_ticker_search_scrape.bat" /st 01:00
```
