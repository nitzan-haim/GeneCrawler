from known_gene_ace2_scraper import *


class MouseScraper(KnownGeneScraper):
    """
    class for scraping information about the ace2 gene in mice.
    """

    def json_to_urls(self, urls_json):
        return [urls_json["known genes"]["mouse"]]