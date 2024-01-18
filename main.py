# Import the function from the other file
from scraper import scrape_and_download_files

# Call the function with arguments from 100 to 98
if __name__ == "__main__":
    for i in range(97, 95, -1):
        scrape_and_download_files(i)
