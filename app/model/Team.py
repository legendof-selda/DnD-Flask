from app import db


class Team(db.Model):
    id = db.Column("team_id", db.Integer, primary_key=True, auto_increment=True)
    name = db.Column("team_name", db.String(80), nullable=False, unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Team {self.name}>"
