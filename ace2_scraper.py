import scrapy
import re
import abc
import json


class Ace2Spider(scrapy.Spider, abc.ABC):
    """
    abstract class for scraping information about the ace2 gene from genome browser (UCSC).
    """

    # class variables

    # Spider properties
    name = "ace2_scraper"
    custom_settings = {
        'FEED_FORMAT': 'jsonlines',
        'FEED_URI': 'ace2_comparison.jsonl'
    }
    start_urls = []

    # other variables
    """
    path to a file that contains urls for scraping
    """
    URLS_PATH = "ace2_genome_browser_urls"


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

    # constructors:

    def __init__(self):
        scrapy.Spider.__init__(self)
        self.set_urls()

    # methods:

    def set_urls(self):
        """
        set the start urls attribute of this crawler.
        """
        with open(self.URLS_PATH) as urls_f:
            urls_json = json.load(urls_f)
            self.start_urls = self.json_to_urls(urls_json)

    @abc.abstractmethod
    def json_to_urls(self, urls_json):
        """
        parse the object obtained from loading the json fil and get the
         relevant urls from it.
        :param urls_json: dictionary containing urls. the dict is of the form:
        {category1: {species1: url}, ... }, category2: ...}
        :return: list of urls that this crawler will scrape.
        """
        return

    # Spider overridden methods:

    def yield_parameters(self, response):
        print("Ace2Spider - yield_parameters")

        # get the chromosome information
        chromosome_info = response.css(self.CHROMOSOME_SELECTOR).get().split(":")
        chromosome_num = chromosome_info[0][3:]
        [chromosome_start_loc, chromosome_end_loc] = chromosome_info[1].split("-")

        dic = {
            'species': re.search(self.NAME_REGEX,
                                 response.xpath(self.SPECIES_SELECTOR).get()).group()[23:-1],

            'size': response.css(self.BP_SELECTOR).get(),
            'chromosome': chromosome_num,
            'chromosome start location': chromosome_start_loc,
            'chromosome end location': chromosome_end_loc,
            'exons num': re.search(self.EXON_INTRON_REGEX, response.xpath(self.EXON_SELECTOR).get()).group()[1:],
            'introns num': re.search(self.EXON_INTRON_REGEX, response.xpath(self.INTRON_SELECTOR).get()).group()[1:],

        }

        return dic

    def parse(self, response):
        yield self.yield_parameters(response)
