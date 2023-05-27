from scraper.oreilly_scraper import OreillyScraper


if __name__ == "__main__":
    scraper = OreillyScraper()
    scraper.save_book_data()