# SingleWebPageApp

<h3><b>Data Representation and Querying Project</b></h3>
In this repository is the code to my Single Web Page Application which I created as a project for one of my College modules, Data Representation and Querying.

<h3>Overview of Project </h3>
I spent the first while debating on what to do my project on. I had initially came up with the ideas of:
   
    1. Shopping List Entry App
    2. Address Book App
    3. Anonymous Story Blog

After alot of brainstorming on these ideas, I opted for <b> 3.Anonymous Story Blog.</b> I went with the anonymous Story Blog idea as I felt it was something different and not as common as ideas 1 and 2. I also feel that this anonymous stroy blog could help alot of of people out there who feel trapped and lonely and  need to get something off their chest without being identified they they so wish.

<h3>Creating the Project </h3>
For creating my project i used the text editor <a  href = "https://www.sublimetext.com/"> <b>Sublime</b></a>.
Also the console <a href= "http://cmder.net/"> <b> CMDER </b> </a> to run my app and <a href ="http://couchdb.apache.org/"> <b>Couchdb </b> <a> for the database where I  save all the stories in the app. 

I chose to use these Applications, as first of all I have worked with them prior to the creation of this project with in class exercises and with other modules I study. <div>

Secondly, they arent difficult to use or navigate. Also I found that there is alot of helpful resources out there to help with any difficulties I may have faced.

<h3>App Details </h3>
<b>Here's My Story </b> is the name I gave to My Anonymous Blog App. The single web Page App allows you to write a story/joke/opinion you may have and to post it along with stories others have written. You can post Anonymously if you so wish by not signing off your name in your story or if you choose to you can sign off with your name/nickname so others can relate with you and other stories you may have posted. 

The App contains a Navbar linking you to the:

        Home Page : Where you write and submiit your story
        Stories Page: Where all stories are displayed
        About Page: Details to the reader about the Application


<h3> How to run the App </h3>

In order to run the application you must:
   
      1. cd to the Apps directory in CMDER
      2. Then you first want to run setup.py (This creates the database in which the app will write to)
             $  py setup.py
      3. Then you want to run webapp.py
             $  py webapp.py
      4. Once webapp.py is running, it will give you a url for you to run in your browser:  http://127.0.0.1:5000/
        
