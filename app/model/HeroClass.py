from app import db


class HeroClass(db.Model):
    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    name = db.Column(db.String(80), nullable=False)
    max_hp = db.Column(db.Float, nullable=False, default=100)
    max_manna = db.Column(db.Float, nullable=False, default=100)