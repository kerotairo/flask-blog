#Entry-point for executing our application

from app import app
import models
import views

if __name__ == '__main__':
    app.run()