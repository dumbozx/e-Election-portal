# E-Elections Portal

A secure and user-friendly electronic voting system was developed for Anand International College of Engineering, Jaipur.

![E-Elections Portal](static/images/anand.jpg)

## Overview

The E-Elections Portal is a web-based application designed to facilitate transparent and secure electronic voting for college elections. Built with Flask and modern web technologies, this system allows students and faculty to participate in various college elections remotely.

## Features

- **Secure Authentication**: Role-based access control with admin and voter roles
- **Election Management**: Create, schedule, and manage multiple elections
- **Real-time Results**: View election results with visual representations
- **Candidate Management**: Add and manage candidates for different positions
- **Voter Verification**: Ensure only eligible voters can participate
- **Timezone Support**: All timestamps displayed in IST (Indian Standard Time)
- **Responsive Design**: Works on desktop and mobile devices

## Technology Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript, Bootstrap 5
- **Database**: SQLite (can be configured for other databases)
- **Authentication**: Flask-Login
- **Form Handling**: Flask-WTF
- **Time Management**: pytz for timezone handling

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/e-election.git
   cd e-election
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables (optional but recommended for production):
   ```
   # On Windows
   set SECRET_KEY=your_secure_secret_key
   set FLASK_APP=app.py
   set FLASK_ENV=development
   
   # On macOS/Linux
   export SECRET_KEY=your_secure_secret_key
   export FLASK_APP=app.py
   export FLASK_ENV=development
   ```

5. Initialize the database:
   ```
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

6. Run the application:
   ```
   python app.py
   ```

7. Access the application at `http://127.0.0.1:5000`

## Usage

### Admin Functions

1. **Create Elections**: Set up new elections with start and end times
2. **Manage Candidates**: Add candidates to elections
3. **Monitor Voting**: Track voter participation
4. **View Results**: Access detailed election results

### Voter Functions

1. **View Active Elections**: See all elections available for voting
2. **Cast Votes**: Vote in active elections
3. **View Results**: See results of completed elections

## Security Considerations

- All passwords are securely hashed
- CSRF protection enabled for all forms
- Session management with secure cookies
- Input validation and sanitization
- Protection against common web vulnerabilities

## Customization

The system can be customized for different institutions by modifying:

- College logo and branding
- Election types and positions
- User roles and permissions
- Email templates for notifications

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Acknowledgements

- Anand International College of Engineering, Jaipur for supporting this project
- Flask and its extensions for providing a robust framework
- Bootstrap for responsive design components

## Contact

For any queries or support, please contact:
- Email: nileshkumar257777@gmail.com
