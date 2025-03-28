import argparse
from pubmed_fetcher.fetcher import PubMedFetcher

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers based on query.")
    parser.add_argument("query", type=str, help="PubMed query string")
    parser.add_argument("-f", "--file", type=str, help="Output CSV filename")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")
    
    args = parser.parse_args()

    fetcher = PubMedFetcher(tool="PubMedTool", email="your_email@example.com")

    if args.debug:
        print("Fetching papers with query:", args.query)

    papers = fetcher.fetch_papers(query=args.query)

    if args.file:
        fetcher.save_to_csv(papers, args.file)
        print(f"Results saved to {args.file}")
    else:
        for paper in papers:
            print(paper)

if __name__ == "__main__":
    main()
