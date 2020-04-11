# Patrick Lynch Bookmarks App Website

Milestone 3
One Project: Data Centric  Development - Code Institute

This project was built to be used either by the user or myself, to store or bookmark urls. 
The building of the project came from a need to organize my own bookmarks, 
which become bloated and cluttered. In the pursuit of learning to code, 
shopping online or just finding articles Im Interested In, I found myself bookmarking 
urls on google or copying and pasting links and texting them to myself as a way of saving when using my mobile. 
So I wanted to build something that fulfilled all of these needs. If it I could build 
something useful to me. I was  sure It would be useful to other users.  [Python](https://docs.python.org/3/), the micro framework [Flask](https://flask.palletsprojects.com/en/1.1.x/) and [Mongodb](https://docs.atlas.mongodb.com/) atlas as the cloud based storgare for the data.  



## UX
This project Is part of the Code Institute full stack developer course. It focuses on the data centric development module. The main objective is to create a website that uses the CRUD operations of Create,Read,Update, and the delete. With this In mind I wanted to create an app for myself and other users where I Implemented these CRUD operations. My Idea came from a very real need. Over the last year while learning to code I found myself almost everyday bookmarking countless useful websites, stack overflow links, tutorials, as well as links to something I might buy later on amazon! My bookmarks have become extremely bloated and I find it really difficult to search through them. So I decided why not try and build my own bookmark manager. If something Like this could be useful for myself. I hope It could also be useful for other users.   
I began using this app for myself as soon as the very basic functionality was set up. 
I used it to store useful links for building the app which gave me a good feel for what 
worked and what did not. What was a good user experience and what was not.
You can Search through the bookmarks and find them using the category name, a word from the description, 
the date or month it was added or a word from the url itself. I also wanted this to be a site where all 
bookmarks are added by each user and are shared among the community as I feel links to useful 
websites when learning a new skill can be a valuable resource. It could also be used to store a shopping 
wish list and for many other purposes.  Each user also has their own unique bookmarks on a user page 
and only they can edit or delete their own bookmarks. I myself as the admin could also directly delete 
them from the database.   

 

## User  stories
" as u a user I would like to ____________    "

- be able to view the website from all devices

-  to see Instructions on how to use the website.

-  to be able to register an account and then login

- see what other people have added to the website.

- be able to search what other users have added with ease.

- to be able to start my own personal collection of bookmarks.

- to add a a category and to edit or delete that category

- to add bookmark  delete or edit that bookmark

- to see my bookmark displayed after i have added it 

- To be able to log out


## Design

- Layout - The design for this website was done using bootstrap for layout. 
- Colors -  although I started out with blue and yellow as my primary colors of choice the developer tools told this was not a good choice. There was a contrast warning. This lead me to go for something completely different using two colors which I got from this [Hook agency](https://hookagency.com/website-color-schemes/]) website. At the time of writing this it was number two on the list on the home page which contains website color palette Ideas. The colors used where  <mark> #fceed1</mark> which Is listed as a very light shade of yellow but Is referred to as tan on the  [Hook egency](https://hookagency.com/website-color-schemes/]) website and <mark>#7d3cff</mark>  which Is described as a very light shade of purplish blue. I felt the two complement each other well and the developer contrast tools were happy!

- Fonts - The fonts used where taken from google fonts.I used mainly Oswald for larger texts an barlow semi condescended for smaller text I like this combination and i think it goes well together 

 





## Wireframe mockups
  Wireframing for this project was done the same as I like to do all my projects with a pencil and paper. Some of the forms pages would be near Identical on both mobile and larger devices so this was written on the sketch rather than sketching It out twice.

<details>
<summary>Home page</summary>
<br>
<table>
   <tr>
    <td>Mobile version<img src="https://res.cloudinary.com/plyn85/image/upload/c_scale,w_375/v1585946844/bookmarks-app/bookmarks%20wireframes/IMG_20200403_204146_kzcfmb.jpg" alt="wireframe mockup" style="width: 375px;"/> </td>
    <td>Tablets ard larger  <img src="https://res.cloudinary.com/plyn85/image/upload/v1585985056/bookmarks-app/bookmarks%20wireframes/IMG_20200403_180417_dhzhtx_hqugcg.jpg" style="width: 375px;"/> </td>
    </tr>
</table>
</details>
<br>
<details>
<summary>Register page</summary>
<br>
<table>
   <tr>
    <td> For all devices <img src="https://res.cloudinary.com/plyn85/image/upload/v1585983630/bookmarks-app/bookmarks%20wireframes%20pics/IMG_20200403_180614_se9vwj.jpg" alt="wireframe mockup" style="width:375px;"/> </td>
</table>
</details>

<br>
<details>
<summary>Login page</summary>
<table>
   <tr>
   For all devices
    <td> <img src="https://res.cloudinary.com/plyn85/image/upload/v1585983626/bookmarks-app/bookmarks%20wireframes%20pics/IMG_20200403_180628_avi2pa.jpg" alt="wireframe mockup" style="width: 250px;"/> </td>
</table>
</details>

<br>
<details>
<summary>User Bookmarks page</summary>
<br>
<table>
   <tr>
    <td>Mobile version<img src="https://res.cloudinary.com/plyn85/image/upload/c_scale,w_375/v1585946002/bookmarks-app/bookmarks%20wireframes/IMG_20200403_212751_am1rug.jpg" alt="wireframe mockup" style="width:375px;"/> </td>
    <td>Tablets and larger<img src="https://res.cloudinary.com/plyn85/image/upload/v1585984036/bookmarks-app/bookmarks%20wireframes/IMG_20200403_180520_2_svp7dc.jpg" alt="wireframe mockup" style="width: 375px;"/> </td>
    </tr>
</table>
</details>


<br>
<details>
<summary>User Categories page</summary>
<table>
   <tr>
    <td>For mobile devices<img src="https://res.cloudinary.com/plyn85/image/upload/c_scale,w_375/v1585946419/bookmarks-app/bookmarks%20wireframes/IMG_20200403_213108_fs3p8w.jpg" alt="wireframe mockup" style="width: 375px;"/> </td>
     <td>For Tablets and larger<img src="https://res.cloudinary.com/plyn85/image/upload/v1585984251/bookmarks-app/bookmarks%20wireframes/IMG_20200403_180535_2_ebxcuz.jpg" alt="wireframe mockup" style="width: 375px;"/> </td>
</table>
</details>

<br>
<details>
<summary>Add Bookmarks page</summary>
<br>
<table>
   <tr>
     For all devices
    <td><img src="https://res.cloudinary.com/plyn85/image/upload/v1585984389/bookmarks-app/bookmarks%20wireframes%20pics/IMG_20200403_180603_mtcmbh.jpg" style="width: 375px;"/> </td>
    </tr>
</table>
</details>

<br>
<details>
<summary>Add Category page</summary>
<br>
<table>
   <tr>
    <td>For all devices <img src="https://res.cloudinary.com/plyn85/image/upload/v1585984744/bookmarks-app/bookmarks%20wireframes/IMG_20200403_180544_sb0cdl_aykchn.jpg" style="width: 250px;"/> </td>
    </tr>
</table>
</details>
<br>
<details>
<summary>Confirm delete category bookmark page</summary>
<br>
<table>
   <tr>
    <td> For all devices<img src="https://res.cloudinary.com/plyn85/image/upload/c_scale,w_375/v1585945090/bookmarks-app/bookmarks%20wireframes/IMG_20200403_211610_l2eyfw.jpg" style="width: 375px;"/> </td>
    </tr>
</table>
</details>

<br>
<details>
<summary>Confirm delete bookmark page</summary>
<br>
<table>
   <tr>
    <td> For all devices <img src="https://res.cloudinary.com/plyn85/image/upload/c_scale,w_375/v1585944020/bookmarks-app/bookmarks%20wireframes/IMG_20200403_204353_zutzsh.jpg" style="width: 375px;"/> </td>
    </tr>
</table>
</details>

<br>
<details>
<summary>Index page search results page</summary>
<br>
<table>
   <tr>
    <td>Mobile version<img src="https://res.cloudinary.com/plyn85/image/upload/c_scale,w_375/v1585944024/bookmarks-app/bookmarks%20wireframes/IMG_20200403_205104_fnggng.jpg" alt="wireframe mockup" style="width: 375px;"/> </td>
    <td>Tablets ard larger <img src="https://res.cloudinary.com/plyn85/image/upload/v1585984834/bookmarks-app/bookmarks%20wireframes/IMG_20200403_204549_uavpyg.jpg" alt="wireframe mockup" style="width: 375px;"/> </td>
    </tr>
</table>
</details>

<br>
<details>
<summary>User bookmarks  page search results page</summary>
<br>
<table>
   <tr>
    <td>Mobile version <img src="https://res.cloudinary.com/plyn85/image/upload/c_scale,w_375/v1585944020/bookmarks-app/bookmarks%20wireframes/IMG_20200403_205349_psp1tx.jpg" alt="wireframe mockup" style="width: 375px;"/> </td>
    <td>For tablets and larger<img src="https://res.cloudinary.com/plyn85/image/upload/c_scale,w_375/v1585944679/bookmarks-app/bookmarks%20wireframes/IMG_20200403_210802_wsrgve.jpg" alt="wireframe mockup" style="width:375px;"/> </td>
    </tr>
</table>
</details>





## Technologies used 
- [Vs code](https://code.visualstudio.com/) - used as my IDE for coding
-  [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) - markup text language used  
-  [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference) - used for  cascading style sheets
- JavaScript 
- [Python](https://docs.python.org/3/) - Used as the back end programming language 
-  [Bootstrap](https://getbootstrap.com/docs/4.1/getting-started/introduction/)- to make the website responsive and used for layout.
- [MongoDb Atlas](https://www.mongodb.com/cloud/atlas) - Was used to store the database.
- [Cloudinary](https://cloudinary.com/home-03-20-20?utm_expid=.VHiV_aImSdyLqXD_FUrhEg.1&utm_referrer=https%3A%2F%2Fwww.google.com%2F) - All images were deployed using the cloudinary caching server.
- [Pymongo](https://api.mongodb.com/python/current/) -Used as a python api for MongoDb
- [Flask](https://flask.palletsprojects.com/en/1.1.x) - used as a microframework 
- [Heroku](www.heroku.com)  -Used to host the app 
- [Git and Github](https://github.com/) used for version control. GitHub used as a remote repository and the hosting of this site.


## Features
### Register  
 - Anyone can sign up, have an account and make use of the app. All passwords encrypted using hashed.
 
### Login 
 - If you are an existing user your username and password will be matched with the database before you can login.

### Home page
- On the home page a user can view every other user's bookmarks. They are displayed 6 at a time and can be navigated using pagination.

### Search 
- Using the search bar on the home page a user can search through evry users bookmarks. This Is done using a keyword search.  The same feature Is available on the users own bookmarks page the only difference being that the users now only search through their own bookmarks.

### Add a category
- A user can add a category which will then be displayed In a dropdown menu on the add bookmarks page as well as the users categories page. Defensive programming ensures that the users only see their unique categories in both the drop down menu and on the categories page.

### Add a bookmark
- A user can add a bookmark which will then be displayed on the user bookmarks page as well as the users home page.

### Edit a bookmark
- The user can edit their own bookmarks. Defensive programming ensured that no users can alter another users bookmarks.

### Edit a Category
- The user can edit their own categories. Defensive programming ensured that no users can alter another users categories.

### Delete a bookmark
- The user can delete their own bookmarks. Defensive programming ensured that no users can delete another users bookmarks.

### Delete a Category
- The user can delte their own categories. Defensive programming ensured that no users can delete another users categories.

## Features left to Implement
- As outlined in the the fixes section the first feature I will like to fix is the Issue with like buttons and pagination. 

- To make a quick add feature available to the user in the categories section  as the section does not do a lot but store the users categories. I would like to add a form on the page or a button which links to a form which allows the user to quickly add just a url 
With the date automatically added which will appear under the category name. This would allow the user the quickly add a url which would not be shared with other users 
With using the other parts of the app.

- A delete account feature which would allow the user to fully delete their account from the database 
 

## Testing 
I used [WSC CSS](https://jigsaw.w3.org/css-validator/) Validation and [HTML Markup](https://validator.w3.org/) Validation to validate the html and css. The only errors occurring was with the Jinja templating language which the HTML validator does not recognise   I used [PEP8](https://www.python.org/dev/peps/pep-0008/) to validate python.

Most of the testing was done In as I developed the app 
Most of the testing was done In as I developed the app. 
I used the flask built In debugger through the whole development phase. I had It set to flask_debug=1. This was a valuable resource. If there were any errors they were shown here and I used this to solve many Issues through the development process. 
As you become accustomed to the debugger you're able to quickly Identify what causes the app to crash. 

### Creating an account
I have created my own account along with 5 fake ones.The authentication for 
Creating an account Is working as expected. I could register login, logout an then log back In Seamlessly.

### CRUD TESTING
As well as my own bookmarks I added ten bookmarks for each of the  5 fake users for testing purposes

###  READ
The first aim was to get the categories displaying on the users categories page.   This was done by returning the categories collection from my database to the user categories route an checking to see If displayed correctly. The next step was to get the bookmarks  displaying correctly on both the homepage and the users page. This was done returning all the bookmarks from the bookmarks collection In my database and testing to see If they appeared on both home an index and user pages 


### UPDATE 
Once a user could display a bookmark  and a category. The next step was to allow them to edit both  bookmarks and categories. This was tested by manually checking the edit categories an edit bookmarks route brought the user to the correct edit categories and edit bookmarks pages. Then the  up_date bookmarks and up_date category routes were checked by confirming the edit In both pages first viewing In the app and then checking It in the database to see If the edit was successful. 


### DELETE 
Testing the delete function of both categories and bookmarks was done first  by manually checking the delete categories and an edit bookmarks route brought the user to the correct delete  categories and delete bookmarks pages. Then the  up_date bookmarks and up_date category routes were checked by confirming the delete In both pages first viewing In the app and then checking It in the database to see If the delete was successful.

### CREATE 
The testing for creating functionality of the app was done on a continuous basis. From the early stages of development I was using the app to store useful links from various sources. This gave me a great chance for any bugs that arose along the way. I also had my friends and family test it for my and I'm happy that CRUD is working without bugs    

### Defensive design 
A login and registration system was used  access to the main part of the website Is only 
Available to registered users.

 The defensive design was implemented throughout this project. Mainly my using the Jinia templating language on the front end. Making use of 
      
      {%if book.username != session.username%}     
      {%if cat.username != session.username%}
This was used to prevent users from having access to certain elements on the page 
Such as the access to delete or edit buttons on other users bookmarks or categories.
Or having the ability to like/upvote their own bookmark.
Certain elements were also hidden from view using 

    {% if session['logged_in']%}
    {% if session not ['logged_in']%}
 
This would restrict access to all the users bookmarks for an unregistered user just visiting the home page


My app is fully responsive across a range of devices. This was achieved using the bootstrap grid. 
The responsiveness and correct displaying of all elements has been tested on a number of devices, browsers, and resolutions. Chrome, Firefox, Opera, Safari, Edge, and IE all display without issue.

Chrome dev tools were used to simulate multiple devices and widths, and no issues were encountered.

The following physical devices where 
tested with no issues found.

 - Lenovo ideapad 320s
 - Apple iphone 8
 - Apple ipad 3 
 - Samsung galaxy A3
 - Huawei p20 lite  

 ## Bugs 
### Heroku error
 When debugging the application on heroku I found that the sort by feature was  sometimes causing an error. The heroku logs showed this was an [H18 Server Request error](https://devcenter.heroku.com/changelog-items/30) This occurs when  a HTTP request is interrupted by a closed socket before the router receives an HTTP response from your app’s web process as outlined In the heroku dev center documentation. I found through googling the Issue It was common and beyond my ability at this point to fix but something I will look to fix In future as It causes the user to have to reload the page and then It seems to work without error.

###  Internet Explorer and Internet Explorer and microsoft Edge Issue 
 
When veiwing the callout section In both edge and Internet explorer the  callout section text was barely visible. This was a problem I enconterd In milestone one and I used the same fix I used then In my current application. Its a problem  In which the col class from bootstrap was causing the text to condense. It was resolved by adding 

    .flex-box-fix {
    -webkit-box-flex: 0;
     flex: none;
    -ms-flex: none;
    -moz-box-flex: none;
    }
      
## fixes 
### upvote/Like button
The upvote feature combined with pagination caused me a major headache. Although both work as designed when a user likes another user's bookmark they are returned to the first page of the pagination the Index page. The solution In this problem which stops the page reload could be achieved by using ajax to send the data to the server. I tried to Implement It but unfourtally was unable to get It working . Given more time and with an Improved skill set I will return to the Issue as It makes for a bad user experience.  

## Deployment 
I deployed this application by:
 
- Pushing the code from my IDE vscode which has a  built In terminal to Github via git. 
- I created an app on heroku 
- In Heorku deployment method was set to github and automatic deploys set from the master branch
- Then the app was then deployed using the following link  [https://bookmarks-app-plyn85.herokuapp.com/](https://bookmarks-app-plyn85.herokuapp.com/)

 
Should you wish to clone this:

   1. On GitHub, navigate to the main page of the repository.
   2. Under the repository name, click Clone or download.
   3. In the Clone with HTTPs section, click the copy icon to copy the clone URL for the repository.
   4. Open terminal.
   5. Change the current working directory to the location where you want the cloned directory to be made.
   6. Type git clone, and then paste`[https://github.com/plyn85/bookmarks-app](https://github.com/plyn85/bookmarks-app)
   7. Press Enter. Your local clone will be created.




## Credits

### Content
 - All of the content In the data page was written by myself

### Media
The only Image and logo used on the website  where obtained from google Images
### Acknowledgements
 - Rahul Patil my Code Institute mentor, for his invaluable advice and guidance.
- The [Pretty printed](https://www.youtube.com/channel/UC-QDfvrRIDB6F0bIO4I4HkQ) Youtube channel and amazing resource for building flask apps 


 - The [Corey Schafer](https://www.youtube.com/watch?v=MwZwr5Tvyxo) Python Flask Tutorial. I found myself returning too reagulary for a better understanding of flask

  #### Disclaimer

   The content of this Website is for educational purposes only.
