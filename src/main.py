import xml.etree.ElementTree as ET
import spacy
import os
import streamlit as st

# Load English language model
nlp = spacy.load("en_core_web_sm")


# Parse XML file and extract text content
def extract_text_from_xml(xml_file):
   tree = ET.parse(xml_file)
   root = tree.getroot()
   text_content = ""
   for elem in root.iter():
       if elem.text is not None:
           text_content += elem.text + " "
       if elem.tail is not None:
           text_content += elem.tail + " "
   return text_content


# Process text content with spaCy
def process_text_with_spacy(text):
   return nlp(text)


# Extract keywords from user input
def extract_keywords(user_input):
   doc = process_text_with_spacy(user_input)
   return [token.text for token in doc if token.pos_ in ["NOUN", "VERB", "ADJ", "ADV"]]


# Check if the fact is true
def check_fact(xml_text, keywords, similarity_threshold=0.9):
   doc = process_text_with_spacy(xml_text)
   for keyword in keywords:
       keyword_doc = process_text_with_spacy(keyword)
       for token in doc:
           if token.similarity(keyword_doc) >= similarity_threshold:
               return True
   return False


# Main function
def main():
    st.title("Fact Verification App")
    # Directory containing XML files
    xml_dir = "/Users/kellerliptrap/desktop/PMC001xxxxxx"
    # User input for the fact to verify
    user_fact = st.text_input("Enter the fact you want to verify:")

    if st.button("Verify Fact"):
        # Extract keywords from user input
        user_keywords = extract_keywords(user_fact)

        # Flag to track if the fact is true in any file
        fact_true_in_any_file = False

        # Iterate through XML files
        for filename in os.listdir(xml_dir):
            if filename.endswith(".xml"):
                xml_file = os.path.join(xml_dir, filename)
                xml_text = extract_text_from_xml(xml_file)
                placeholder = st.empty()  # Create a placeholder for dynamic content
                placeholder.write(f"Checking file: {filename}")
                fact_found = check_fact(xml_text, user_keywords)
                if fact_found:
                    placeholder.write(f"The fact was found in this file {filename}.")
                    fact_true_in_any_file = True
                    break  # Exit loop if fact is found
                else:
                    placeholder.empty()  # Clear placeholder if fact is not found

        # Print result
        if fact_true_in_any_file:
            st.write("The fact is true in at least one file.")
        else:
            st.write("The fact is not true in any file.")


if __name__ == "__main__":
   main()
