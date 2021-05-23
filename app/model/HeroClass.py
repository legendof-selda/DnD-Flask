from app import db


class HeroClass(db.Model):
    id = db.Column("hero_class_id", db.Integer, primary_key=True, auto_increment=True)
    name = db.Column("class_type", db.String(80), nullable=False)
    max_hp = db.Column("max_hp", db.Float, nullable=False, default=100)
    max_manna = db.Column("max_manna", db.Float, nullable=False, default=100)