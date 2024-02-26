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

This project is a part of the data science exemplar project. The base overview of what the project is aiming to do is to allow a user to put in a fact of their choice for example the user may put in "dogs can fly". The program will have access to a large group of papers that will be looked through for this fact. IF the fact is found then the user we be told yes their entry is a fact and if the user input is not found then the program will tell the user that the fact they wanted to verify is not a fact. This project can be useful in several cases. Currently, in social media, there continues to be factual info and news being passed on as fake. Using such a program can be very useful. A caveat to this project is it requires a user to input a fact they want to check but in a later version of this ideally it just automatically checks for facts on something like Twitter/X for users' posts and checks if it's a fact. Companies might find a more complex version of this type of project useful. Implementing this into their social media company can help users determine what info they should believe. Giving notifications in conjunction with a post that some info is fake can improve the quality of life for the users and the owners. Overall the fact checker can allow users to check their desired fact with a large database of academic papers and get feed back to whether or not this entry is true.

## Literature Review

TODO: Conduct literature review by describing relevant work related to the project and hence providing an overview of the state of the art in the area of the project. This section serves to contextualize the study within the existing body of literature, presenting a thorough review of relevant prior research and scholarly contributions. In clear and meaningful language, this section aims to demonstrate the problems, gaps, controversies, or unanswered questions that are associated with the current understanding of the topic. In addition, this section serves to highlight the current study's unique contribution to the field. By summarizing and critiquing existing works, this section provides a foundation for readers to appreciate the novelty and significance of the study in relation to the broader academic discourse. The "Literature Review" section further contributes to the `why is the project important?` question. The number of scholarly work included in the literature review may vary depending on the project.

## Methods

TODO: Discuss the methods of the project to be able to answer the `how` question (`how was this project completed?`). The methods section in an academic research outlines the specific procedures, techniques, and methodologies employed to conduct the study, offering a transparent and replicable framework for the research. It details the resources behind the work, in terms of, for example, the design of the algorithm and the experiment(s), data collection methods, applied software libraries, required tools, the types of statistical analyses and models which are applied to ensure the rigor and validity of the study. This section provides clarity for other researchers to understand and potentially replicate the study, contributing to the overall reliability and credibility of the research findings.

There are many methods to determine whether a fact is true or not but this project uses natural language processing. This project uses the library `spaCy` to do all the language processing. To get started you'll need `nlp = spacy.load("en_core_web_sm")`. This simply loads the pre-trained English language model within spaCy. The first step in coding to start the language processing is to get the database of papers. These papers are XML files so they need to be parsed through and converted into text that can be read by the program. After we get all the files read and inputted into the program we need to take all of the text and run it through the natural language database that we brought in earlier with the designated variable of nlp. An important detail for this project is how to interpret the user's input. To do this we use spaCy to get the nouns, verbs, adjectives, and adverbs of the user's input. This allows us to get the key terms and shorten the input to check for facts.

## Using the Artifact

TODO: The result of your work will be the delivery of some type of artifact which will likely contain software programming solutions (i.e., Python code, HTML pages, or similar). To allow the user to experience and execute your artifact, you must first explain how to set up the initial conditions to run or use the artifact. Be sure to offer explicit details and instructions regarding the installation of the necessary foundational libraries, drivers, external software projects, containers and similar types of tertiary software which are involved in executing your artifact. Once these initial software installations have been completed, then you are asked to offer the necessary instructions for actually executing the artifact. For this, please provide all command line parameters or associated bash commands for execution. Please remember that users are unwilling to "figure-out" how to use code in absence of the essential instructions concerning the execution of project artifacts.

## Results and Outcomes

TODO: Discuss the outcomes of your project in this section. Depending on the project type, the presented results and outcomes will vary. In some projects, you will be asked to present a theoretical analysis, and in others your experimental study and its results. In this section, you are also to demonstrate an enhanced version of your artifact by showing its capabilities and applications, in light of the evaluation metrics for assessing the artifact

---

## Exemplar Projects Discussions

The department's project descriptions can be found at [https://github.com/ReadyResearchers-2023-24/cmpsc-580-exemplar-projects](https://github.com/ReadyResearchers-2023-24/cmpsc-580-exemplar-projects)

## Schedule

The schedule for this work can be found at [https://github.com/CMPSC-580-Allegheny-College-Spring-2024/classDocs?tab=readme-ov-file#schedule](https://github.com/CMPSC-580-Allegheny-College-Spring-2024/classDocs?tab=readme-ov-file#schedule)
