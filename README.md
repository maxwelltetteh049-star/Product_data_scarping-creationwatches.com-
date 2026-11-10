# Product Data Scraping(creationwatches.com)

A python based web scraper created to automate creationwatches.com website and extract product information using pure selenium.

The scraper visits the bestseller watches page and extacts the product listing detail links of each product being listed. After, then visit each product detail page then extract the target information from each product detail page.

This project was built as a practical web scraping and data extraction project for skill development and portfolio purposes.


## 🚀 Features

- Uses Selenium to establish a browser session
- Scrapes product detail_page urls for each listing product.
- store the extracted detail links.
- Visit each product detail pages.
- Extracts:
  - Product name
  - Marked price
  - Model
  - Movement
  - Water resistance
  - Detail link
- Uses MySQL for data storage and deduplication
- Loads processed data back into Python
- Exports the final dataset to CSV
- Includes error handling
- Includes retry mechanisms for browser and page-loading operations


## 🛠️ Technologies Used

- Python
- Selenium – for browser automation and establishing the browser session
- MySQL – for storing scraped data and handling deduplication
- mysql-connector-python – for connecting Python to MySQL
- CSV – for the final data output

## 🖼️ Screenshots
The interface of the product listing page.

![creationswatches interface](imagesm/listing_page2.png)


The detail page of a product.

![creationswatches interface](imagesm/detail_page2.png)

This is the excel output

![creationswatches interface](imagesm/Excellll.png)





## 🔁 Reliability

The scraper includes error handling and retry mechanisms in important parts of the scraping process.

Retries are implemented in functions responsible for:

- Opening the browser
- Loading the required site/page

This helps the scraper recover from temporary failures instead of immediately terminating the scraping process.

## ⚙️ Installation
1. clone the repository

2. Install the required dependencies:

       - pip install -r requirements.txt

Make sure the required browser and Selenium driver configuration is available before running the scraper.


## ⚠️ Disclaimer

This project is intended for educational and portfolio purposes. When accessing or collecting data from external websites, users should respect the website's terms of use, robots policies where applicable, applicable laws, and reasonable request limits.

## 👤 Author

Maxwell Tetteh

