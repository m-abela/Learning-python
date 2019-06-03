OSlist = ["android","ANDROID","IOS"]
yes = ["YES","Y","y","yes"]
no = ["NO","no","N","n"]
options = ["NO","no","N","n","YES","Y","y","yes"]
speclist = []
OS = ""
camera = ""
fingerprint = ""
movies = ""
gaming = ""
printer = ""
print("IOS is safer and has a nice interface, however, IOS devices are generally expensive. Android is better for developers")
while OS not in OSlist:
    OS = input("what operating system do you want for you phone?")
    print(OS)
speclist.append(OS)
while fingerprint not in options:
    fingerprint = input("are you concerned about security? Do you have important files to keep safe?")
if fingerprint in yes:
    speclist.append("fingerprint")
while camera not in options:
    camera = input("do you often take pictures?")
if camera in yes:
    speclist.append("16mpcamera")
else:
    speclist.append("2mpcamera")
photos = int(input("how many pictures do you think you'll take"))
storage = 0.036*photos
while movies not in options:
    movies = input("Do you want to watch movies on your phone?")
if movies in yes:
    storage = storage + 32
speclist.append((str(storage)+"GB"))

while gaming not in options:
    gaming = input("Do you want to do gaming on your phone?")
if gaming in yes:
    speclist.append("4gbram")
    speclist.append("snapdragonprocessor8455")
else:
    speclist.append("kirin950")
    speclist.append("1gbram")
while printer not in options:
    printer = input("Do you want to print stuffs")
if printer in yes:
    speclist.append("printer")
print(speclist)

