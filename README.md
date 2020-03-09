## Index
[Brief](#brief)
   * [My Solution](#mysolution)
   
[ERD and Diagrams](#erdanddiagrams)
   * [Initial ERD](#erd)
   * [Final ERD](#FinalErd)
   * [Risk Assessment](#riskassess)
   * [Risk Assessment Table](#risktable)
   * [User Stories](#userstories)

[Sprints & Planning](#spr1)
   * [Trello Board Sprint 1.0](#spr1)
   * [Trello Board Sprint 2.0](#spr2)
   * [Trello Board Sprint 2.1 Continued...](#sprF)
   * [Trello Board Completion Stage](#sprFF)
	
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
which will be used to log them into the website..

<a name="erdanddiagrams"></a>
## ERD and Diagrams

<a name="erd"></a>
### Initial Entity Relationship Diagrams
![Initial ERD](/images/initialERD.jpg)

The ERD Diagram above was the initial structure, After careful consideration I decided that the table for posts is not needed
and adds furthur complexity to the project. (Click image for higher quality image).

* Instead I decided to create a table called Adverts that makes a more logical connection to my solution as the Users table will connect
directly to the Adverts table (As users will create Adverts in which their cars will be posted) The relationship here will be a 1 to Many as each user can have many adverts. 

Finally I removed a few fields that were redundant and added fields such as password, profile image and more specific user information such as First names and Last names.  

<a name="FinalErd"></a>
### Final Entity Relationship Diagrams
![Final ERD](/images/finalerdtwo.jpg)

<a name="riskassess"></a>
## Risk Assessment
# MosCoW Prioritization / Requirements / Product Backlog

As seen below I have created a MosCoW Prioritisation list where all the requirements of the project are listed,
I used a colour labelling method On Trello to make sure that each requirement had its own importance category.
(Full Trello Board Later in the Document) (Click image for higher quality image)

![MosCow](/images/reqs.jpg) ![Labels](/images/Labels.jpg)

<a name="risktable"></a>
## Risk Assessment Table
![Risk Assessment Table](/images/risktable1.jpg)
![Risk Assessment Table Part 2](/images/risktable2.jpg)

<a name="userstories"></a>
## User Stories (Users and Developers)

The User Stories was also done on Trello, I listed all the use-cases for the product in the perspective of a user and a developer.
(Click image for higher quality image) 

![UserStories](/images/Userstories.jpg)

<a name="spr1"></a>
## Trello Board (Sprint 1)

Here is the First Sprint I did after defining the main requirements of the project. (Click image for higher quality image).

![Trello Image](/images/Trello.jpg)

<a name="spr2"></a>
## Trello Board (Sprint 2)

You can see tasks from the first Sprint have been moved to the Done list and further tasks have been actioned and moved to the second Sprint stage.
(Click image for higher quality image). 

![Sprint 2 Image](/images/sprint2.jpg)

<a name="sprF"></a>
## Final Stages (Sprint 2....)

Most of the project requirements have been fullfilled at this point and the final touches are being made, as you can see the items that needed actioning have been moved to the done stage and the few optional requirements are being finalised.
(Click image for higher quality image) 

![Sprint 2 Continued..](/images/finalsprint.jpg)

<a name="sprFF"></a>
## Last Sprint to completion

The project is now in the completion stage, all requirements have been met and optional features have been added, also some un-needed features were not implemented such as the search function and an additional DB table due to time restraints.

![Completion..](/images/finishedsprint.jpg)

<a name="testingmethod"></a>
## Testing Methodology

Decided to use Pytest to create my tests, Mostly testing all my routes and request codes to see if everything was working correctly
I automated the testing using Jenkins, making sure that the deployment would not go ahead unless the tests passed as the build/deploy
process was a trigger I set up in Jenkins.

<a name="testingreport"></a>
### Testing Report

Below is the HTML Coverage Report that was generated after the automated testing completed which was done using Jenkins, also after the testing was complete the file was moved to the test_results folder which is also can be found on my github repo here(https://github.com/code-wizard91/Performance-Motors/blob/master/test_results/index.html)

![HTML Coverage Report](/images/coveragereport.jpg)

<a name="deploymentmethod"></a>
## Deployment

![Deployment Pipeline](/images/pipeline.jpg)

The Deployment pipeline for this Flask application was done using Git/Github for source control and automating that process using
webhooks, the process would then go into automatically triggering the testing phase which I did using Pytest on a VM running Jenkins, after the tests Jenkins will be triggered into the build/deployment process if the testing was successful, Jenkins will then build and Deploy the app on a seperate VM (APP VM) on Azure. Also a seperate instance of Azures MySql will be used and connected to this VM for data storage. (Click image for higher quality image) 


<a name="techused"></a>
### List of Technologies Used

* MySQL for Application Database
* Python - Coding in Flask
* Flask - Framework 
* Jenkins - CI Server
* Testing - Pytest
* [Github Project](https://github.com/code-wizard91/Performance-Motors) - Version Control System
* [Trello Board](https://trello.com/b/5RcaZXRp) - Project Tracking Board
* Azure Services (MySQL Azure DB, Azure VM)

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
