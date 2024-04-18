fav_lang = {
    'eli':'python',
    'josue':'java',
    'joab':'c',
    'lulu':'cobol',
    'eli':'sql',
}

keys = []
values = []

for key, value in fav_lang.items():
    keys.append(key)
    values.append(value)

# print("Keys:", keys)
# print("Values:", values)


# for i in fav_lang.values():
#     print(i)
# for i in fav_lang.keys():
#     print(i.title())

# lou_preferred = fav_lang['lou']
# print(lou_preferred)# Will error bc lou does not exist. Instead do this:

lou_preferred = fav_lang.get('lou', 'User Not found')
# print(lou_preferred)

credentials = {
    'eli':'kjkhfn4163!',
    'lulu':'santiagok1981!',
    'joab':'f70r3ncias',
    'josue':'20050865!'
}

for name in credentials.keys():
    print("User Name: ", name.title())

get_pasword = credentials.get(input("Username: ").lower(), "User not found")
print(f"Password : {get_pasword} ")