import unittest
import xml.etree.ElementTree as ET
import spacy
import os
from main import check_fact, extract_keywords

class TestCheckFact(unittest.TestCase):

    def test_check_fact(self):
        # Sample XML text containing a fact
        xml_text = """
                    <document>
                        <text>Cats and dogs can fly.</text>
                    </document>
                   """
        # Extracting keywords from the fact
        fact_keywords = extract_keywords(xml_text)

        # Print extracted keywords for debugging
        print("Extracted Keywords:", fact_keywords)

        # Test with the sample XML text and extracted keywords
        result = check_fact(xml_text, fact_keywords)

        # Print result of similarity comparison for debugging
        print("Result of Similarity Comparison:", result)

        # Assert that the result should be True since all extracted keywords are present in the text
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()

