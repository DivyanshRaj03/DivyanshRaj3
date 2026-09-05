import re

# Email pattern
EMAIL_PATTERN = r'[a-z A-Z 0-9_.+-]+@[a-z A-Z 0-9-]+\.[a-z A-Z 0-9.-]+'


# Function to find emails in a text
def find_emails(text):
    return re.findall(EMAIL_PATTERN, text)


# Function to validate a complete email
def is_valid_email(candidate):
    return re.fullmatch(EMAIL_PATTERN, candidate) is not None


# Sample text
sample_text = """
Hello everyone.
You can contact us at support@examplecorp.com.
Rahul's email is rajdivyansh567@gmail.com.
"""


# Find all emails
emails = find_emails(sample_text)

print("Emails found:")
for email in emails:
    print(email)

print("\nTotal emails found:", len(emails))


# Test individual email addresses
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