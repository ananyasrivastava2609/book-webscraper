import requests
from bs4 import BeautifulSoup
import csv
import json


def scrape_books():

    url = "https://books.toscrape.com/"

    # Send request to website
    response = requests.get(url)

    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all book containers
    books = soup.find_all("article", class_="product_pod")

    # Store extracted data
    extracted_data = []

    # Loop through each book
    for book in books:

        # Extract title
        title = book.h3.a["title"]

        # Extract price
        price = book.find("p", class_="price_color").text

        # Extract availability
        availability = book.find("p", class_="instock availability").text.strip()

        # Create dictionary
        book_data = {
            "title": title,
            "price": price,
            "availability": availability
        }

        extracted_data.append(book_data)

        # Print data in terminal
        print(f"{title} | {price} | {availability}")

    # Save CSV
    with open("data/books.csv", "w", newline="", encoding="utf-8") as csv_file:

        fieldnames = ["title", "price", "availability"]

        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()

        writer.writerows(extracted_data)

    # Save JSON
    with open("data/books.json", "w", encoding="utf-8") as json_file:

        json.dump(extracted_data, json_file, indent=4)

    print("\nData saved successfully!")