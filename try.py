import dbconfig

user = dbconfig.db_users.users.find_one({'username':'FranciscoElGrande'})

print(user)