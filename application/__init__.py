from flask import Flask

app = Flask(__name__)
app.secret_key = "123456789oihabdadjKJADJEj&@YJDSjhde32FDqwaeudycer"
from application import routes