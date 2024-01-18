import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os

def scrape_and_download_files(roundid):
    # Define the search phrase
    search_phrase = "»Свали"

    # Define the URL of the website
    website_url = f"https://codeit.bg/bul/rounds/standings/{roundid}/"

    # Send a GET request to the website
    response = requests.get(website_url)

    # Parse the HTML content of the website
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all the <a> tags that contain the search phrase
    links = soup.find_all("a", string=search_phrase)

    # Create a folder with the roundid as the folder name
    folder_name = str(roundid)
    os.makedirs(folder_name, exist_ok=True)

    # Iterate over the links
    for link in links:
        # Get the href attribute of the link
        href = link["href"]

        # Append "https://codeit.bg" to the href using urljoin
        download_link = urljoin("https://codeit.bg", href)

        # Find the grandparent <td> tag with class "download"
        grandparent_td = link.find_parent("div").find_parent("td")

        # Check if the grandparent <td> tag contains a non-zero number
        if float(grandparent_td.get_text().strip().split("\n")[0]) != 0:

            # Get the file name from the download link
            file_name = os.path.basename(download_link)

            # Download the file from the download link
            response = requests.get(download_link)

            # Save the downloaded file in the roundid folder
            file_path = os.path.join(folder_name, file_name)
            with open(file_path, "wb") as file:
                file.write(response.content)

            # Print the found hrefs in the console
            print("Found href:", download_link)
