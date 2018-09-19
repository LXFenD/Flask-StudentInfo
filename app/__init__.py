from flask import  Flask
 
import config
app = Flask(__name__,static_folder='static',template_folder='templates')
app.config.from_object('config')






