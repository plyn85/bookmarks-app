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

## Demo
A live demo can be found [here]
![Desktop Demo]("Desktop Demo")

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

 

## Database Schemea 

## User  stories
" as u a user I would like to ____________    "

- be able to view the website from all devices

-  to see Instructions on how to use the website.

-  to be able to register an account and then login

- sseeb what other people have added to the website.

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



## Features left to Implement

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
 Anyone can sign up, have an account and make use of the app. All passwords encrypted using hashed.
 
### Login 
If you are an existing user your username and password will be matched with the database before you can login.

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





 










 


## Testing 

## Manual testing of all elements on website

## Deployment 

## Credits

### Content

### Media

#### Disclaimer

   The content of this Website is for educational purposes only.