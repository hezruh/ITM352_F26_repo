# Parse through portions of email address, print out username and domain name
# Name: Hezra Calventas
# Date: September 18, 2026

emailAddress = input("Enter an email address: \n")
parts = emailAddress.split("@")
username = parts[0]

print("Parts of the email address:", parts)
print("Username:", username)

domainName = parts[1]
print("Domain name:", domainName)

atSignIndex = emailAddress.index("@")
username2 = emailAddress[:atSignIndex]
domainName2 = emailAddress[atSignIndex + 1:]

print("Username (method 2):", username2)
print("Domain name (method 2):", domainName2)