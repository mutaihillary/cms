import hashlib

user_entered_password = 'pa$$w0rd'
salt = "5gz"
db_password = user_entered_password + salt
h = hashlib.md5(db_password.encode())
print(h.hexdigest())
