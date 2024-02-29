[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/Y4rZMh1t)
# Junior Seminar (CMPSC 580) Exemplar Project Repository

## Semester: Spring 2024

This repository contains student project materials, including project report, data, code, and references to literature for this departmentally-sponsored project. __As you complete each of the below sections in this document, please be sure to remove the preamble text so that it does not appear in your work.__ Please work with your first reader to answer any questions or concerns that you may have.

## GitHub Handle: kellerliptrap

## Name: Keller Liptrap

## Major: Computer Science

## Project Name: Fact or Fiction?

---

## Overview

This project is a part of the data science exemplar project. The base overview of what the project is aiming to do is to allow a user to put in a fact of their choice for example the user may put in "dogs can fly". The program will have access to a large group of papers that will be looked through for this fact. IF the fact is found then the user we be told that their entry is a fact and if the user input is not found then the program will tell the user that the fact they wanted to verify is not a fact. This project can be useful in several cases. Currently, in social media, there continues to be factual info and news being passed on as fake. Using such a program can be very useful. A caveat to this project is it requires a user to input a fact they want to check but in a later version of this ideally it just automatically checks for facts on something like Twitter/X for users' posts and checks if it's a fact. Companies might find a more complex version of this type of project useful. Implementing this into their social media company can help users determine what info they should believe. Giving notifications in conjunction with a post that some info is fake can improve the quality of life for the users and the owners. Overall the fact checker can allow users to check their desired fact with a large database of academic papers and get feedback back to whether or not this entry is true.

## Literature Review

The paper I looked at about this project's topic of fact-checking is titled Automated `Fact Checking: Task Formulations, methods, and future directions`. This paper is written by `James Thorne` and `Andreas Vlachos` who are both in the Department of Computer Science at the University of Sheffield in the UK. This paper discusses the growing need for fact-checking online especially since true and false information can reach a large audience with ease. To do this there is an uptaking in the need for automated fact-checking processes. To do this the authors investigate the use of natural language processing and the automation of factcheking. They aim to test this mostly in the journalism area. They follow this by explaining the various inputs into a fact-checking machine. There are two that stood out to me for the use of this project Subject-Predicate-Object Triples and Textual Claims. Where textual claims are the users put into the program they want to see if this claim is true or false and Subject-Predicate-Object Triples is are large database of papers and known statements that are true. This paper pointed out some ways in which we can do fact checking but not without issues. Some evidence will be hard to verify and may still need human interaction to determine if it is true or false. The author's overall consensus is there are still strides that need to be taken in the form of automated fact-checking but it can still be viable. 

Link: https://arxiv.org/pdf/1806.07687.pdf

## Methods

There are many methods to determine whether a fact is true or not but this project uses natural language processing. This project uses the library `spaCy` to do all the language processing. To get started you'll need `nlp = spacy.load("en_core_web_sm")`. This simply loads the pre-trained English language model within spaCy. The first step in coding to start the language processing is to get the database of papers. These papers are XML files so they need to be parsed through and converted into text that the program can read. After we get all the files read and inputted into the program we need to take all of the text and run it through the natural language database that we brought in earlier with the designated variable of nlp. An important detail for this project is how to interpret the user's input. To do this, we use spaCy to get the user's input's nouns, verbs, adjectives, and adverbs. This allows us to get the key terms and shorten the input to check for facts. To determine a fact the program goes line by line in each of the papers within the file and checks for similarity which is built into the spaCy library. In addition to this, there is a similarity threshold to determine how close together the words are to help determine a fact. A user can use this dashboard to compare a statement they want to confirm is a fact or not to a large database of scholarly papers.

## Using the Artifact

To run this code you will require a couple of installs for the project to function as intended. Below is what is needed and the command to install the requirements. This should be done after cloning the repository.
| Requirement             | Description                                                                                                          |
|-------------------------|----------------------------------------------------------------------------------------------------------------------|
| Python                  | Version 3.6 or later.                                                                                                |
| xml.etree.ElementTree  | Part of Python's standard library. No separate installation is needed.                                                  |
| spacy                   | `pip install spacy`.                                                |
| en_core_web_sm          |  `python -m spacy download en_core_web_sm`.                            |
| os                      | Part of Python's standard library. No separate installation is needed.                                                  |
| streamlit               | `pip install streamlit` This is the dashboard section of the project                        |
| XML Files               |    https://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_bulk/oa_noncomm/xml/oa_noncomm_xml.PMC001xxxxxx.baseline.2023-12-18.tar.gz   This is the download to the xml files that you will need to path to  |

The path to the xml files will be contained in the main in this line of code `xml_dir = ""`. Between quotations is where you will need to provide your path to the download xml file database. To run the program you must use this command `streamlit run main.py`. This will create a local host where the dashboard will appear and your desired fact can be inputted.



## Results and Outcomes

After building and running my tool to fact-check a user input to be true or false it does what it is intended to do but there can be some improvements done. Generally, the user's experience is good when running this program to find whether the input is a fact or not. The issue falls into the runtime of the program. The database that the fact is compared to is large. The user's input is broken down and used for a threshold of similarity by looping through each line in each file. Based on testing input if it is a fact then the program will run faster depending on where the file is located in the database due to the program stopping when the fact is found and displaying it. If a fact is not true the runtime is long. For the user running the program, they will have a text box to enter their fact in the dashboard. Once the fact is entered they flick a button and the program begins. Each file will be displayed as the fact is checked. IF the fact is found it will display which file it is found in.

---

## Exemplar Projects Discussions

The department's project descriptions can be found at [https://github.com/ReadyResearchers-2023-24/cmpsc-580-exemplar-projects](https://github.com/ReadyResearchers-2023-24/cmpsc-580-exemplar-projects)

## Schedule

The schedule for this work can be found at [https://github.com/CMPSC-580-Allegheny-College-Spring-2024/classDocs?tab=readme-ov-file#schedule](https://github.com/CMPSC-580-Allegheny-College-Spring-2024/classDocs?tab=readme-ov-file#schedule)
