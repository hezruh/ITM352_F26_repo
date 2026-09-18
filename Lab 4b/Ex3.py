# Get a URL from the user, clean it, and extract the domain name and TLD
# Name: Hezra Calventas
# Date: September 18, 2026

url = input("Enter a URL: \n")
cleanedUrl = url.replace("https://", "")
cleanedUrl = cleanedUrl.replace("/","")
print("Cleaned URL:", cleanedUrl)

parts = cleanedUrl.split(".")
print("The parts are: ", parts)

domainName = parts[1]
tld = parts[2]
print("Domain name:", domainName)
print("TLD:", tld)
