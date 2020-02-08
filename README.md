# project_three

Online Shop Gorgeous
Table of Contents
Overview and goals
Pages
Design
Functionality
Validation and Testing
Deployment


# Intro and goals
This is Code Institute Stream Three Project as part of the Full Stack Development course. The project is focused on both Front End and Back End Development skills. It is a brand new Django project composed of multiple apps.

Reptile hub is the name of the website for this project. Reptile is a website where everyone can write a blog about how to care a specific reptile specie. Therefore this is a website for reptile caresheets. 


the website is user and mobile friendly
the homepage calls for action to register to also write reptile caresheets. 
A filter where visitors more easily find specific reptile caresheets. 


# Pages
The website has the following pages:

Homepage
Listpage
Caresheetpage
Profile page
Post form page
Update page
Register page
Login page

# Homepage (index)
Is a page where the website is presented when the visitor visits reptile hub. Is sees an overview of the three newest caresheets posted on the website. If people are not registered it has also an call to action for registering. The page has also for everyone a button where the can enter the page where all caresheets are posted. 

# Listpage (post_list)
This is the page where all caresheets are posted. It is also equiped with a filter where people can search for a reptile by typing a search query or select the type of reptile.

# Caresheetpage (post_detail)
This is the page with specific information of the reptile.

# profile page (profile)
This is the page where people who have post a caresheets can find them in their personal profile. No one can change, delete or post caresheets in from other authors. On this page the author is authorised to update and delete their posted caresheets or to post a new one.

Therefore the update and delete post are included on this page!

# Postform
Via the postform page the registered user is able to post an caresheet. The form used in this page is a bootstrap form

# register page
In this page users are able to make an account. The form which is used is styled by bootstrap forms.

The wireframes were created during the initial planning stage before starting the project development.
Registered users are automatically logged in once registered.

# Login
In this page registered users are able to login. 

# update password
this is also a form where registered users can update their password once the password is updated, they got to the:

# update password complete
Is a success page of the update password page.


# Apps and folders
  - accounts
  
  - caresheets
  
  - media
  - posts
  - search
  - static
  - staticfiles
  - templates

# Accounts
This app has two models custom user and caresheets. Every caresheet has one author but an author can have written more than one caresheets. The custom user model is used to display names of users in the backend. 

# Caresheets
Caresheets is the parant app of all apps. It ensures the interaction between apps in order run the website.

# Posts
This app has the class Animal and animalimages. Animal class is the blueprint of each written caresheet and animalimages is optional to add more than one picture.

# Search
Search is an app in order to deal with search queries by name.

# static
static is the folder where the css files are organised. Every css file in this project is used for one page. 

# staticfiles
staticfiles are the blueprint of static.

# templates
templates is used to store the base template.


# Creditations
I would like to give credits to stack overflow for providing my insights in how to get a working filter! I also want to thank my mentor Brian Macharia, who helped me out with an authentification issue and a issue of deleting a post. The footer of this website is from MDBootstrap the navbar from getbootstrap.com
