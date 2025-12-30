#Taking URL input from the user
url = input("Enter URL: ")

#checks if the URL starts with "https://"
if "https://" in url:
    print("The URL is secure. It uses HTTPS.")
else:
    print("The URL is not secure. It does not use HTTPS.")

#Removing other things to get the domain and path
domain = url.split("//")[-1].split("/")[0] #Extracting domain
print("The domain of the URL is:", domain)
path = url.split("/")[-1] #Extracting path
print("The path of the URL is:", path)
