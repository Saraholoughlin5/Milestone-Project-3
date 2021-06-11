# **Milestone Project 3**
## **Kooky Kids Recipes**
# Table of Contents

1. [Purpose and Value](#purpose)
2. [Site Pages](#sitepgs)
	1. ['Home' page](#homepage)
	2. ['Log In'](#login)
	3. ['Join' page](#join)
	4. ['Profile' page](#profile)
	5. ['Add Recipe' page](#addrecipe)
	6. ['Edit Recipe' page](#editrecipe)
	7. ['Delete Recipe' button](#delrecipe)
	8. ['Log Out' menu item](#logout)
3. [Responsivity](#responsivity)
4. [UX (User Experience)](#userexperience)
	1. [Strategy Plane](#strategy)
	2. [Scope Plane](#scope)
	3. [Structure Plane](#structure)
    4. [Skeleton Plane](#skeleton)
	5. [Surface Plane](#surface)


## Kooky Kids Recipe App

### **Purpose and Value**<a name="purpose"></a>

The purpose of the Kooky Kids recipe app is to display easy to follow, cooking-free recipes, aimed at children, young teenagers and their parents or caretakers.  
The recipes are easy to find and view, and easy to follow.  
Users can read each recipe without logging in, however, if users do join the site (create a user profile) and log in they can then also create, edit and delete their own recipes. 
An Admin account can police the site and edit or delete any unsuitable additions.
Users can document and edit their own recipes, visible to them on their own Profile page. The site is visually appealing to younger users, and this aims to encourage repeated use.

### **Site Pages**<a name="sitepgs"></a>

#### **'Home' page**<a name="homepage"></a>
The 'Home' page contains the navigation menu (side navigation menu in mobile/medium view), a 'Welcome' message, a search bar that enables users to search the recipe ingredients, the current list of recipes displayed in a collapsible accordion element and social media links (via a floating action button on large view, and a footer in medium and small views).
Users can click on the name of any recipe to view it in full (invited to do so by use of a caret symbol that precedes each recipe title).
Users who are logged in can see an 'Edit' button on their own recipes, which identifies their recipes and allows them to make changes. Users cannot delete recipies via the homepage.

#### **'Log In' page**<a name="login"></a>
The 'Log In' page contains a card which displays the 'Username' and 'Password' fields, a 'Submit' button and a link to sign up via the 'Join' page.
The background image is prominent in this view, which invites inspection of the imagery and appeals to the target demographic.  

#### **'Join' page**<a name="join"></a>
Similar layout to the 'Log In' page. This page contains a card which displays the 'Username' and 'Password' fields, a 'Submit' button, and a link to the 'Log In' page, should the user have a profile already set up.

#### **'Profile' page**<a name="profile"></a>
The 'Profile' page displays a 'Welcome' flash message on login, information related to the page contents, the list of recipes submitted by this user, and 'Edit' and 'Delete' buttons per recipe.
Clicking on each recipe title displays the recipe details in full.

#### **'Add Recipe' page**<a name="addrecipe"></a>
The 'Add Recipe' page can only be accessed when a user is logged in (if the url is updated to try and cheat this (e.g. user is logged out), a message is displayed to notify the user that they have no access to the page. 
The page displays some relevant text information, followed by the 'Recipe Details' form.
The form contains inputs, textareas, select options field and a date-picker. A 'Submit' button is also displayed.
Once a recipe is submitted, the user is redirected to the 'Home' page to view their submission.

#### **'Edit Recipe' page**<a name="editrecipe"></a>
The 'Edit Recipe' page can be accessed in two ways; via the 'Edit' button on the collapsible headings per recipe on the homepage, and also in the same place on the user's 'Profile' page. 
The user must be logged in to edit their recipes. 
Admin can edit their own recipes via the homepage, but can edit all user's recipes via their Admin 'Profile' page

#### **'Delete Recipe' button**<a name="delrecipe"></a>
The 'Delete Recipe' button is only accessible on a logged in user's 'Profile' page. It is available to the right of the 'Edit' button on the collapsible header (recipe title). 
When the 'Delete' button is clicked on, a modal is displayed to confirm with the user that they want to permanently delete their recipe. This prevents accidental deletion of the user's submission. 
Once a recipe is deleted, the user is redirected back to their 'Profile' page, and they can confirm that the recipe is indeed no longer listed. It is also removed from the list on the homepage.
Admin can delete every user's recipe via the Admin 'Profile' page.

#### **'Log Out' menu item**<a name="logout"></a>
The 'Log Out' menu item can be clicked to end the user session. A flash message alerts the user that they have been successfully logged out of their profile.
The 'Log In' page is displayed once more.

### **Responsivity**<a name="responsivity"></a>
The app is responsive on a variety of screen types and sizes. It has been checked via the browser 'Inspect' tool list of responsive devices, both portrait and landscape.
It has also been checked on a variety of browsers, including Chrome, Microsoft Edge, and Safari.
[Materialize](https://materializecss.com/) classes and helpers were used to ensure that each page looks and behaves and expected on each screen size.
The [mock-ups](http://ami.responsivedesign.is/?url=http%3A%2F%2Fmilestone-3-kids-recipes.herokuapp.com%2Fget_recipe#) display various sections of the 'Home' and 'Log In' pages: 

![alt Responsive Design](static/img/layout/am_i_responsive.PNG "Responsive Design")

### **UX (User Experience)** <a name="userexperience"></a>

#### **Strategy Plane**<a name="strategy"></a>
The Kooky Kids app could be used in schools or summer-camps, or as part of an initiative to encourage independent or healthy eating amongst children and young adults.  
The background image and colour scheme are fun and draws the correct age group in, and are dynamic enough to appeal to a variety of users. It is clear to the user how the site operates, and each feature is easy to use. 

#### **Scope Plane**<a name="scope"></a>
The app is simple to use, and each feature is clear and straight-forward to user. Users can click on the ‘Log In’ or ‘Join’ menu options to start submitting recipes. The can edit or delete their recipes easily via the buttons provided. 
A floating button can be clicked on to view the social media links (visible in the footer on small and medium screens).  
Relevant flash messages are also displayed for key functions, such as joining the app, logging in or out, updating or deleting a recipe, or as a warning when e.g. a username is already taken. 
The recipe display (collapsible) is intuitive and provides the expected information. 

#### **Structure Plane**<a name="structure"></a>
The app is structured so that the layout is consistent on many of the pages. 'Log In' and 'Join' pages are uniform, and non-jarring to the user. 
The 'Home', 'Profile', 'Add Recipe' and 'Edit Recipe' views are consistent and provide enough information for the user to be comfortable with navigating each step of each page. 
The background image is also consistent throught the app.
Links and buttons work as expected.

#### **Skeleton Plane**<a name="skeleton"></a>
Balsamiq wireframes were used to plan the initial layout of the app (desktop and portrait mobile view). The app appears similar to the wireframes, but looks much more vivacious due to the addition of the background image and related colour scheme.

#### **Surface Plane**<a name="surface"></a>
The colour scheme of the app was drawn heavily from the background image, which suits the them of the database content very well. The panels, buttons and borders are very subdued and mainly black and white, but the colour in the background image and navigation bar/footer/action buttons counteract this simplicity.

