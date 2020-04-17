import scrapy
import re
import abc


class Ace2Spider(scrapy.Spider, abc.ABC):
    """
    abstract class for scraping information about the ace2 gene from genome browser (UCSC).
    """

    # class variables

    # Spider settings
    name = "ace2_scraper"
    custom_settings = {
        'FEED_FORMAT': 'jsonlines',
        'FEED_URI': 'ace2_comparison.jsonl'
    }

    # other variables
    """
    path to a file that contains urls for scraping
    """
    URLS_PATH = "ace2_genome_browser_urls"

    """
    list to store this spider's urls
    """
    urls = []

    # selectors:

    # css selectors:
    """
    selector for the base pairs number that this gene contains (=length of the gene)"""
    BP_SELECTOR = '#size ::text'

    """
    selector for the chromosome information of this gene (num and location)
    """
    CHROMOSOME_SELECTOR = '.positionDisplay ::text'

    # xpath selectors:
    """
    selector for the title of the page, containing the species name.
    """
    SPECIES_SELECTOR = './/form[@id="TrackHeaderForm"]/center//span/b/text()'

    """
    selectors for the exon and intron number of this gene. both unique to the sub-class.
    """
    EXON_SELECTOR = ''
    INTRON_SELECTOR = ''

    # regular expressions for formatting scraped data:
    """
    get the exon or intron number, for example "Exon (4/18)" > 18
    """
    EXON_INTRON_REGEX = '[/](\d+)'

    """
    match the first part of the title, including species name
    """
    NAME_REGEX = "UCSC Genome Browser on ([a-zA-Z]+) "

    # abstract methods:

    @abc.abstractmethod
    def set_urls(self):
        """
        set the urls_d of this spider.
        """
        return

    # Spider overridden methods:

    def start_requests(self):
        self.set_urls()
        for url in self.urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # get the chromosome information
        chromosome_info = response.css(self.CHROMOSOME_SELECTOR).get().split(":")
        chromosome_num = chromosome_info[0][3:]
        [chromosome_start_loc, chromosome_end_loc] = chromosome_info[1].split("-")

        yield {
            'species': re.search(self.NAME_REGEX,
                                 response.xpath(self.SPECIES_SELECTOR).get()).group()[23:-1],

            'size': response.css(self.BP_SELECTOR).get(),
            'chromosome': chromosome_num,
            'chromosome start location': chromosome_start_loc,
            'chromosome end location': chromosome_end_loc,
            'exons num': re.search(self.EXON_INTRON_REGEX, response.xpath(self.EXON_SELECTOR).get()).group()[1:],
            'introns num': re.search(self.EXON_INTRON_REGEX, response.xpath(self.INTRON_SELECTOR).get()).group()[1:],

        }
