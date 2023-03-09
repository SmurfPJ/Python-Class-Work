email = """Hi everyone, 

There will be a book fair in our school next week for fundraising. If you would like to participate in this fair, kindly bring some spare books. The amount will go towards building a new computer lab in our school. 

Looking forward to your participation in this fundraising. 

SEE YOU ALL IN THE BOOK FAIR!"""

print(email)

email = email.replace("book","cash")
email = email.replace("books","cash")
email = email.replace("BOOK","cash")

email = email.replace("fair","investment")
email = email.replace("FAIR","investment")

email = email.replace("computer lab","casino")

email = email.replace("fundraising","$$$")

print(email)