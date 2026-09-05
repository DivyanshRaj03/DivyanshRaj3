import re

EMAIL_PATTERN = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.-]+'



def find_emails(text):
    return re.findall(EMAIL_PATTERN, text)


def is_valid_email(candidate):
    return re.fullmatch(EMAIL_PATTERN, candidate) is not None


sample_text = """
Hello everyone.
You can contact us at support@examplecorp.com.
Rahul's email is rajdivyansh567@gmail.com.
"""

emails = find_emails(sample_text)

print("Emails found:")
for email in emails:
    print(email)

print("\nTotal emails found:", len(emails))


test_emails = [
    "support@examplecorp.com",
    "rajdivyansh567@gmail.com",
    "123@example.com"
]


print("\nEmail Validation:")
for email in test_emails:
    if is_valid_email(email):
        print(email, "-> VALID")
    else:
        print(email, "-> INVALID")