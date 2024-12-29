class Config:
    # For local use: SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:12345@localhost/postgres'
    # For Docker use: SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:12345@db/postgres'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:12345@db/postgres'
    SQLALCHEMY_TRACK_MODIFICATIONS = False