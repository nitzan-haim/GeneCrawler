from ncbi_ref_ace2_scraper import NCBIReferenceScraper
from ref_gene_scraper import RefGeneScraper
from human_scraper import HumanScraper
from mouse_scraper import MouseScraper
from scrapy.crawler import CrawlerProcess

process = CrawlerProcess()
process.crawl(MouseScraper)
process.crawl(HumanScraper)
process.crawl(NCBIReferenceScraper)
process.crawl(RefGeneScraper)
process.start()
