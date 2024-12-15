# A Chatter Box App 


Chatter Box is a dynamic and interactive messaging application built with Django. It provides a user-friendly platform for creating, editing, and sharing tweets in real time. The application prioritizes simplicity, interactivity and security to enhance the user experience. Whether you’re sharing thoughts, exploring trending topics or connecting with others, Chatter Box offers an engaging space to interact.


# Features

User Registration & Login:
Users can register for an account and securely log in using Django's built-in authentication system, which ensures data security and effective user session management.

Tweet Creation:  
Users can post their thoughts or ideas and have the option to attach a photo. Each tweet is associated with the user who created it.

Tweet Editing:
Users can edit their existing tweets, allowing them to refine or update their content. However, they can only edit their own posts.

Tweet Deletion:
Users can delete their tweets securely, with a confirmation prompt to prevent accidental deletions. Users are only able to delete their own tweets.

List Tweets:  
Users can view a curated list of tweets displayed in reverse chronological order, presented in a visually appealing and scrollable feed.

Mobile-Friendly UI:  
The design is responsive and clean, ensuring an engaging experience across all devices.

CSRF Token Protection:  
Django's CSRF (Cross-Site Request Forgery) protection is implemented to safeguard against malicious attempts to manipulate form submissions.

Input Validation and Error Feedback:
Forms include strong input validation and provide helpful error messages, ensuring user-friendly interactions and a secure, error-free experience.



# CRUD Operations

The application implements the following CRUD (Create, Read, Update, Delete) functionalities:

Create: Users can create new tweets, optionally attaching images. This is facilitated through Django forms and is securely linked to the logged-in user.
  
Read: A comprehensive feed displays all tweets in reverse chronological order, showcasing content in an aesthetically pleasing and interactive format.
  
Update: Logged-in users can edit their tweets, modify text and update images while ensuring data integrity.
 
Delete: Users can securely delete their tweets. A confirmation prompt prevents accidental deletions.

Project link :  https://django-chatterbox-app.onrender.com

<img width="235" alt="Screenshot 2024-12-15 192623" src="https://github.com/user-attachments/assets/822b8211-447e-419e-95ca-af64fab3abd6" />

# Technologies Used

Backend: Django Framework
Frontend: Bootstrap 5, HTML5, CSS3
Database: SQLite (default Django database)
Authentication: Django’s built-in authentication system

# Installation & Setup

Clone the Repository:

git clone https://github.com/your-username/chatter-box.git
cd Twitter
Install Dependencies: Create a virtual environment and install the required packages:


python -m venv .venv
On Windows use .\.venv\Scripts\activate
pip install -r requirements.txt

Apply Migrations:

python manage.py makemigrations
python manage.py migrate

Run the Development Server:

python manage.py runserver









