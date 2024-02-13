import xml.etree.ElementTree as ET
import spacy

# nlp = spacy.load("en_core_web_sm")

# tree = ET.parse("PMC1999407.xml")  # Replace "your_xml_file.xml" with the path to your XML file
# root = tree.getroot()

# doc = nlp(ET.tostring(root, encoding='unicode'))
# # for token in doc:
# #     print(token.text)
# nouns_only_text = ' '.join(token.text for token in doc if token.pos_ == "NOUN")

# print(nouns_only_text)


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

# Check if the fact is true
def check_fact(xml_text, user_fact):
    doc = process_text_with_spacy(xml_text)
    user_input_doc = process_text_with_spacy(user_fact)
    entities = [ent.text.lower() for ent in user_input_doc.ents]
    for entity in entities:
        if entity in xml_text.lower():
            return True
    return False

# Main function
def main():
    xml_file = "PMC1999407.xml"  # Replace with your XML file path
    xml_text = extract_text_from_xml(xml_file)

    user_fact = input("Enter the fact you want to verify: ")

    if check_fact(xml_text, user_fact):
        print("The fact is true.")
    else:
        print("The fact is not true.")

if __name__ == "__main__":
    main()

