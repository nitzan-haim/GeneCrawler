from known_gene_ace2_scraper import KnownGeneScraper
from ncbi_ref_ace2_scraper import NCBIReferenceScraper
from ref_gene_scraper import RefGeneScraper

from scrapy.crawler import CrawlerProcess

process = CrawlerProcess()
process.crawl(KnownGeneScraper)
process.crawl(NCBIReferenceScraper)
process.crawl(RefGeneScraper)
process.start()
