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

[Visual Representation of my Solution](#visrep)

[Retrospective](#improve)

[Authors](#authorsinv)

[Acknowledgements](#acknowledgements)


[How To Install](#install)

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
### Testing Report (Pytest Generated HTML)

Below is the HTML Coverage Report that was generated after the automated testing completed which was done using Jenkins, also after the testing was complete the file was moved to the test_results folder which is also can be found on my github repo [here](https://github.com/code-wizard91/Performance-Motors/blob/master/test_results/index.html)

![HTML Coverage Report](/images/cov1.jpg)

### Testing Report (Generated after automated Jenkins Test)

Here is the coverage report which was generated on Jenkins after the automated Testing took place. You can also see that it triggers the build/deployment process if the tests pass and sends out a notification on Slack.

![Jenkins Coverage Report](/images/cov2.jpg)

<a name="deploymentmethod"></a>
## Deployment

![Deployment Pipeline](/images/pipeline.jpg)

The Deployment pipeline for this Flask application was done using Git/Github for source control and automating that process using
webhooks with Jenkins, the process would then go into automatically triggering the testing phase which I did using Pytest on a VM running Jenkins, after the tests Jenkins will be triggered into the build/deployment process if the testing was successful, Jenkins will then build and Deploy the app on a seperate VM (APP VM) on Azure. Also a seperate instance of Azures MySql will be used and connected to this VM for data storage. (Click image for higher quality image) 

## How the process looks

Here is the actual test and building process taking place.

![Jenkins Coverage Report](/images/automation.jpg)

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

<a name="visrep"></a>
### Front End Visual Representation of my Solution

### Homepage

![HomePage](/images/visrep1.jpg)

### View Advert (Clicked into)
![Advert View](/images/visrep2.jpg)

### Abouts Page
![Abouts Page](/images/visrep3.jpg)

### Login Page

![Login Page](/images/visrep4.jpg)

### Register Page

![Register Page](/images/visrep5.jpg)

### Registering New User

![Register new user](/images/visrep11.jpg)

### User Registered!

![Register new user](/images/visrep12.jpg)

### Logging in

![Uer Logging In](/images/visrep6.jpg)

### User Logged in

![User Logged In](/images/visrep7.jpg)

### Viewing User created Ad (Users can only edit and update their own ads)

![User Ad view](/images/visrep8.jpg)

### Accounts Page (Users can only see this if they are logged in

![Accounts Page](/images/visrep9.jpg)

### Create Adverts Page

![Create Ad Page](/images/visrep10.jpg)

<a name="evaluation"></a>
## Retrospect

Creating this application in an Agile way allowed me to understand and appreciate the benefits of this way of Project Mangement, I also enjoyed the process of putting Agile techniques into how the project was managed using Sprints, Product backlogs etc. Also using the CI/CD way of developing software played a key part in the success of this project as it allowed me to use tools such as Pycharm for testing and Jenkins to Automate the process that links everything together. I was also very happy with the way I was able to use Azure VMs (1 for Jenkins and 1 for the App) to split up processes that normally would happen on a single VM thus allowing for increased durability and extra contingencies to manage risk. The way the application was deployed using Jenkins and how a seperate Azure managed DB worked together was very satisfying to see as the end result was a process that had become very robust and impressive.

I faced many issues along the way, as I was learning the technologies whilst applying them but this ended up making the learning easier as I was able to fail fast and learn faster. 

If I had to go back and change something I would improve the front end functionality more and add furthur features such as search filters and also a Gallery feature so users can upload more than one image.

All together the project was a success and I would definitely use these technologies again in the future.

<a name="authorsinv"></a>
## Authors

Mahboob Ali

<a name="acknowledgements"></a>
## Acknowledgements

* Jay Grindrod - A true motivation, he helped me in far too many ways to list here, Inspired me to push hard and learn things that were beyond the scope of what I needed to acheive. Thanks for your help Jay!

<a name="install"></a>
## How to Run this App using Docker-Compose

- Step 1:

Get Docker and Docker-Compose set up on your Machine. (I used Linux)
Make sure you have the port 5000 open on your pc.

- Step 2: 

Git Clone this repository
From inside the repository run "docker-compose up -d"


## The app is now running on your localhost on port 5000
