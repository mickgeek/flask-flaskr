# Specify parameters of the application configuration.

ENV = 'development' # should be 'production' or 'development'
SECRET_KEY = 'xgAxGMb34dR1xCzGwu'

SQLALCHEMY_DATABASE_URI = 'postgresql://root:root@postgres/app'
SQLALCHEMY_TRACK_MODIFICATIONS = False
USERNAME = 'admin'
PASSWORD = 'admin'

TESTING = False
TEST_DATABASE_URI = 'postgresql://root:root@postgres/app_test'
