
Author: Dabana Intenque                  
Date: 01/27/ 2023

 Project description:

You don't need any other directions beyond the basics.
This project will get data from a filled form on the wufoo website and return 
the entire data that was entered in the form. Separate line by line in the
order entered.

Here is the wufoo link:
 https://dintenque.wufoo.com/build/cubes-project-proposal-submission

Everything is working fine.

Sprint 2 update:
 This is the continuation of the sprint 1
for this sprint I added a database.py, and cubes_records.py files 
to create a new database and update the previous entries in sprint 1.
Also, I updated my continuous Integration/devOps on GitHub in order to run the tests
Added my secret key value in action under the * Secrets and variables in 
gitHub

Here is my Database layout:
my cube database contains 9 fields for user to enter a data
 
Database Name: Cube_database
  
 Table Name: cubesProposal

  Entries are:
  id:
  prefix:
  first_name:
  last_name:
  title:
  organization_name:
  organization_website:
  email:
  phone:

I wrote two tests for this sprint and both passed.
Thank you!
everything is working fine as except. 


Sprint 3 Update:

 Directions to Run:
 You can run this sprint from two files 
     1- from Cubes_GUI.py (which I recommend)
     2- From main.py
 This sprint is the continuation of the sprint one and two
 the objective of this sprint is to create a GUI that displays the entries 
 from my database.
 
  First, I created a list of entry where the user can choose from to display 
  the information stored on that entry
  
  Second I made the values on the text field read only mode
  
  Third I wrote two tests
    One checks if the text fields contain a value
    and the checkbox is checked or uncheck.
    Second, check if there is a data in the cubesProposal table

  

 Sprint 4 Update.
    I create three new button 
    I added a teacher Database and add a foreign to cubes proposal
    Also, added a test for the sprint.
    
