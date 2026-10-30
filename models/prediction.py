from extensions import db

class Prediction(db.Model):
    __tablename__ = "predictions"

    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    result = db.Column(db.String(100), nullable=False)  # e.g., "Positive", "Normal", "Class A"
    confidence = db.Column(db.Float, nullable=True)     # e.g., 95.5
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    
    # Foreign Key linking to User
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    def __repr__(self):
        return f"<Prediction {self.filename} - {self.result}>"