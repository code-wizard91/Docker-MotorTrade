## Index
[Brief](#brief)
   * [My Solution](#mysolution)
   
[ERD and Diagrams](#erdanddiagrams)
   * [Initial ERD](#erd)
   * [Final ERD](#FinalErd)
   * [Risk Assessment](#riskassess)
   * [User Stories](#userstories)
   * [Trello Board Sprint 1](#spr1)
	
[Testing Methadology](#testingmethod)
   * [Generated Report](#testingreport)
     
[My Deployment Method](#deploymentmethod)
   * [What I used](#techused)
     
[Front End ](#frontend)

[Visual Representation of my Solution](#visrep)

[Evaluation](#improve)

[Authors](#authorsinv)

[Acknowledgements](#acknowledgements)

<a name="brief"></a>
## The Product Brief

To create:
* OOP-based application
* Utilisation of tools methodologies and technologies that encapsulate all core modules covered during training. 
* The application must manipulate two tables
* Application must have full CRUD functionality.

<a name="mysolution"></a>
### Solution

I decided to create a website using Flask and Boostrap for the Front-End, the website is essentially a online marketplace where
users can create Car Adverts that will take details such as; Images, Descriptions, Price, Mileage, Location and Phone numbers.
Users will also have the ability to view cars for sale as well as update and delete their adverts. Users will have accounts 
which will be used to log them into the website.

<a name="erdanddiagrams"></a>
## ERD and Diagrams

<a name="erd"></a>
### Initial Entity Relationship Diagrams
![Initial ERD](/images/initialERD.jpg)

The ERD Diagram above was the initial structure, After careful consideration I decided that the table for posts is not needed
and adds furthur complexity to the project. (Click image for higher quality image)

* Instead I decided to create a table called Adverts that makes a more logical connection to my solution as the Users table will connect
directly to the Adverts table (As users will create Adverts in which their cars will be posted)

<a name="FinalErd"></a>
### Final Entity Relationship Diagrams
![Final ERD](/images/FinalErd.jpg)

<a name="riskassess"></a>
## Risk Assessment
# MosCoW Prioritization / Requirements / Product Backlog

As seen below I have created a MosCoW Prioritisation list where all the requirements of the project are listed,
I used a colour labelling method On Trello to make sure that each requirement had its own importance category.
(Full Trello Board Later in the Document) (Click image for higher quality image)

![MosCow](/images/reqs.jpg) ![Labels](/images/Labels.jpg)

<a name="userstories"></a>
## User Stories (Users and Developers)

The User Stories was also done on Trello, I listed all the use-cases for the product in the perspective of a user and a developer.
(Click image for higher quality image) 

![UserStories](/images/Userstories.jpg)

<a name="spr1"></a>
## Trello Board (Sprint 1)

Here is the First Sprint I did after defining the main requirements of the project. (Click image for higher quality image)

![Labels](/images/Trello.jpg)

<a name="testingmethod"></a>
## Testing Methodology

Will list all the testing methods I used here.


<a name="testingreport"></a>
### Testing Report

Link to report here

<a name="deploymentmethod"></a>
## Deployment

Explain deployment etc jenkins, GitHub and put the diagram here

![Deployment Pipeline](/Documentation/CI_pipeline.jpg)

<a name="techused"></a>
### List of Technologies Used

* MySQL for Application Database
* Python - Coding in Flask
* Flask - Framework 
* Jenkins - CI Server
* Testing - Selenium, Pytest
* [Github Project](https://github.com/code-wizard91/Performance-Motors) - Version Control System
* [Trello Board](https://trello.com/b/5RcaZXRp) - Project Tracking Board
* Azure Services (SQL Server, Azure VM)

<a name="frontend"></a>
## Front End Framework
### Wireframes


<a name="visrep"></a>
### Visual Representation of my Solution

<a name="evaluation"></a>
## Evaluation and Retrospect

Add Evaluation here

<a name="authorsinv"></a>
## Authors

Mahboob Ali

<a name="acknowledgements"></a>
## Acknowledgements

* Honorable mentions
