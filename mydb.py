# Install mysql on server
# https://dev.mysql.com/downloads/installer
# pip install python-dev-tools
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python
# edited settings.py update application and database settings
#  python3 manage.py migrate



import mysql.connector

dataBase = mysql.connector.connect(
    host = '172.28.80.1',
    port = '4407',
    user = 'django',
    passwd = 'django101'
)

# prepare cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE djangoproject")

print("ALl Done!")