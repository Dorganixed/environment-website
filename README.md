# Environment Website

Welcome to the Environment Website repository! This project aims to raise awareness about environmental pollution and provide tools and resources to help individuals and organizations reduce their carbon footprint. The website includes features like a Carbon Footprint Calculator, information about environmental issues, and ways to take action.

## Table of Contents

- [Environment Website](#environment-website)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Technologies Used](#technologies-used)
  - [Installation](#installation)
  - [Usage](#usage)
  - [File Structure](#file-structure)
  - [Contributing](#contributing)
  - [License](#license)
  - [Contact](#contact)

## Features

- **Home Page**: An introduction to the website with a beautiful hero image and a brief description.
- **Carbon Footprint Calculator**: Calculate your carbon footprint based on distance traveled and fuel efficiency.
- **Past Calculations**: View your past carbon footprint calculations.
- **About Section**: Learn about carbon footprints, pollution reduction, and global efforts to combat climate change.
- **Mission Goals**: Understand the mission and goals of the organization.
- **Contact Page**: A contact form to reach out to the organization.
- **Dark/White Mode Toggle**: Switch between dark and light themes for a better user experience.
- **Responsive Design**: Optimized for different screen sizes and devices.
- **Ads Integration**: Integrated with Google AdSense to display ads on the website.

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask (Python)
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Migrations**: Flask-Migrate
- **Pagination**: Flask-Paginate (optional)
- **Other Libraries**: Bootstrap, jQuery

## Installation

Follow these steps to set up the project locally:

1. **Clone the repository**:
   ```  
   git clone https://github.com/your-username/environment-website.git
   cd environment-website
Create a virtual environment:

  
 
python -m venv venv
Activate the virtual environment:

On Windows:
  
 
venv\Scripts\activate
On macOS/Linux:
  
 
source venv/bin/activate
Install the dependencies:

  
 
pip install -r requirements.txt
Run the initial migration:

  
 
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
Run the application:

  
 
flask run
The application should now be running at http://127.0.0.1:5000/.

Usage
Carbon Footprint Calculator
Navigate to the "Calculator" section.
Enter the distance traveled (in km) and fuel efficiency (in km/l).
Click "Calculate" to see your carbon footprint.
View your past calculations under the "View Calculations" section.
Dark/White Mode Toggle
Use the "Dark/White" toggle button in the navigation bar to switch between dark and light themes.
Mission Goals
Learn about the organization's mission and goals by navigating to the "Mission Goals" section.
Contact
Fill out the contact form under the "Contact" section to get in touch with the organization.
File Structure
css
 
environment-website/
├── enviro_calculator/
│   ├── __init__.py
│   ├── calculator.py
│   ├── models.py
│   ├── views.py
├── enviro_website/
│   ├── __init__.py
│   ├── config.py
│   ├── app.py
│   ├── wsgi.py
├── instance/
│   ├── enviro.db
├── migrations/
├── static/
│   ├── css/
│   │   ├── animations.css
│   │   ├── main.css
│   │   ├── responsive.css
│   │   ├── theme.css
│   ├── images/
│   │   ├── hero-bg.png
│   │   ├── icon1.png
│   │   ├── icon2.png
│   │   ├── icon3.png
│   ├── js/
│   │   ├── interactivity.js
│   │   ├── main.js
│   │   ├── scripts.js
├── templates/
│   ├── layouts/
│   │   ├── base.html
│   ├── partials/
│   │   ├── header.html
│   │   ├── footer.html
│   │   ├── navbar.html
│   │   ├── sidebar.html
│   ├── about.html
│   ├── about_carbon_footprint.html
│   ├── calculate.html
│   ├── calculations.html
│   ├── contact.html
│   ├── global_efforts.html
│   ├── index.html
│   ├── mission_goals.html
│   ├── reduce.html
├── tests/
├── venv/
├── .gitignore
├── README.md
├── requirements.txt
Contributing
We welcome contributions to the Environment Website project! Here are some ways you can contribute:

Report bugs and issues
Suggest new features and improvements
Submit pull requests to fix bugs or add new features
How to Contribute
Fork the repository
Create a new branch (git checkout -b feature/your-feature)
Make your changes
Commit your changes (git commit -m 'Add some feature')
Push to the branch (git push origin feature/your-feature)
Create a pull request
License
This project is licensed under the MIT License. See the LICENSE file for more information.

Contact
For questions or inquiries, please contact us at dorukemregurler@gmail.com.com.
