# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField, DateTimeField, SelectField
from wtforms.validators import DataRequired, Length, Optional, EqualTo, ValidationError
from models import User
import datetime

# Login Form
class LoginForm(FlaskForm):
    user_id = StringField('College ID', validators=[DataRequired(), Length(min=4, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

# Vote Form
class VoteForm(FlaskForm):
    candidate_id = RadioField('Select a Candidate', validators=[DataRequired()], coerce=int)
    submit = SubmitField('Cast Vote')

# Election Form
class ElectionForm(FlaskForm):
    name = StringField('Election Name', validators=[DataRequired(), Length(max=100)])
    position = StringField('Position', validators=[DataRequired(), Length(max=100)])
    start_time = DateTimeField('Start Time', format='%Y-%m-%d %H:%M', validators=[DataRequired()])
    end_time = DateTimeField('End Time', format='%Y-%m-%d %H:%M', validators=[DataRequired()])
    is_active = BooleanField('Active')
    submit = SubmitField('Create Election')

    def validate_end_time(self, end_time):
        if end_time.data and self.start_time.data and end_time.data <= self.start_time.data:
            raise ValidationError('End time must be after start time.')

    # Removed validation that prevents start_time from being in the past
    # This allows elections to be created with a start time in the past
    # def validate_start_time(self, start_time):
    #     # Convert naive datetime to aware datetime for comparison
    #     naive_now = datetime.datetime.now()
    #     if start_time.data < naive_now:
    #         raise ValidationError('Start time cannot be in the past.')

# --- Registration Form ---
class RegisterForm(FlaskForm):
    user_id = StringField('College ID', validators=[DataRequired(), Length(min=4, max=50)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password', message='Passwords must match.')])
    submit = SubmitField('Register')

    # Custom validator to check if user_id already exists
    def validate_user_id(self, user_id):
        user = User.query.filter_by(id=user_id.data).first()
        if user:
            raise ValidationError('This College ID is already registered. Please login or use a different ID.')


# --- Admin Voter Management Form ---
class VoterForm(FlaskForm):
     user_id = StringField('College ID', validators=[DataRequired(), Length(min=4, max=50)])
     # Add validation for password complexity if desired
     password = PasswordField('Initial Password', validators=[DataRequired(), Length(min=8)])
     is_admin = BooleanField('Make Admin?')
     submit = SubmitField('Add Voter')

     # Custom validator to check if user_id already exists (for adding new voters)
     def validate_user_id(self, user_id):
        user = User.query.filter_by(id=user_id.data).first()
        if user:
            raise ValidationError('This College ID already exists.')

# --- Candidate Management Form ---
class CandidateForm(FlaskForm):
    name = StringField('Candidate Name', validators=[DataRequired(), Length(max=100)])
    submit = SubmitField('Add Candidate')