from app import db


class Hero(db.Model):
    id = db.Column("hero_id", db.Integer, primary_key=True, auto_increment=True)
    name = db.Column("hero_name", db.String(80), nullable=False)
