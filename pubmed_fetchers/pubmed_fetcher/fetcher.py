import csv
from pymed import PubMed
from typing import List, Dict

class PubMedFetcher:
    def __init__(self, tool: str, email: str):
        self.pubmed = PubMed(tool=tool, email=email)

    def fetch_papers(self, query: str, max_results: int = 100) -> List[Dict]:
        results = self.pubmed.query(query, max_results=max_results)
        papers = []
        for article in results:
            authors = article.authors if article.authors else []
            non_academic_authors = [
                author['name'] for author in authors if 'company' in author.get('affiliation', '').lower()
            ]
            company_affiliations = [
                author.get('affiliation', '') for author in authors if 'company' in author.get('affiliation', '').lower()
            ]
            corresponding_email = article.get('email', None)
            
            papers.append({
                "PubmedID": article.pubmed_id,
                "Title": article.title,
                "Publication Date": article.publication_date,
                "Non-academic Author(s)": non_academic_authors,
                "Company Affiliation(s)": company_affiliations,
                "Corresponding Author Email": corresponding_email,
            })
        return papers

    def save_to_csv(self, papers: List[Dict], filename: str):
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=[
                "PubmedID", "Title", "Publication Date", 
                "Non-academic Author(s)", "Company Affiliation(s)", 
                "Corresponding Author Email"
            ])
            writer.writeheader()
            writer.writerows(papers)
