import pytest
from pubmed_fetcher.fetcher import PubMedFetcher

@pytest.fixture
def fetcher():
    return PubMedFetcher(tool="TestTool", email="test@example.com")

# tests/test_fetcher.py


# tests/test_sample.py

def test_sample():
    assert True



def test_fetch_papers(fetcher):
    papers = fetcher.fetch_papers("cancer")
    assert len(papers) > 0

from pubmed_fetcher.fetcher import some_function

def test_some_function():
    result = some_function()
    assert result == "expected_output"


def test_save_to_csv(fetcher):
    papers = [{"PubmedID": "12345", "Title": "Test Paper", 
               "Publication Date": "2025-03-27",
               "Non-academic Author(s)": ["John Doe"], 
               "Company Affiliation(s)": ["Pharma Inc."],
               "Corresponding Author Email": "john.doe@example.com"}]
    
    fetcher.save_to_csv(papers, "test.csv")
    with open("test.csv") as file:
        lines = file.readlines()
        assert len(lines) > 1  # Header + data rows
