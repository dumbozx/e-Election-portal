from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.String(50), primary_key=True)  # College ID or unique identifier
    password_hash = db.Column(db.String(256))
    is_admin = db.Column(db.Boolean, default=False)
    has_voted = db.Column(db.Boolean, default=False) # Simple flag - needs refinement for multiple elections/positions

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    # Required by Flask-Login
    def get_id(self):
        return self.id

class Election(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    start_time = db.Column(db.DateTime, default=lambda: datetime.datetime.now(datetime.timezone.utc))
    end_time = db.Column(db.DateTime)
    is_active = db.Column(db.Boolean, default=True)

class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    election_id = db.Column(db.Integer, db.ForeignKey('election.id'), nullable=False)
    election = db.relationship('Election', backref=db.backref('candidates', lazy=True))
    # Add fields for photo, manifesto_url, etc.

# VERY Simplified Vote Model - Needs careful design for security/anonymity
class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    election_id = db.Column(db.Integer, db.ForeignKey('election.id'), nullable=False)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidate.id'), nullable=False)
    # WARNING: Storing voter_id directly links vote to user - NOT ANONYMOUS!
    # A better approach involves cryptographic techniques or careful decoupling
    # For this example, we might rely on the User.has_voted flag (simplistic)
    timestamp = db.Column(db.DateTime, default=lambda: datetime.datetime.now(datetime.timezone.utc))

# Track which users have voted in which elections
class UserVoteStatus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), db.ForeignKey('user.id'), nullable=False)
    election_id = db.Column(db.Integer, db.ForeignKey('election.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=lambda: datetime.datetime.now(datetime.timezone.utc))

    # Relationships
    user = db.relationship('User', backref=db.backref('vote_statuses', lazy=True))
    election = db.relationship('Election', backref=db.backref('vote_statuses', lazy=True))

    # Ensure a user can only vote once per election
    __table_args__ = (db.UniqueConstraint('user_id', 'election_id', name='_user_election_uc'),)