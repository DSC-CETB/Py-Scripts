import requests, os, sys

print("Enter Your URL: ", end="")
url = input()
short = "http://tinyurl.com/api-create.php?url=" + url
final = requests.get(short)  # direct link is passed and shortened is returned here
if final.text == "Error":
    print("Link is Not valid! Retry")
    sys.exit(1)

else:
    print (short)
    print("Shortened Link: " + final.text)
