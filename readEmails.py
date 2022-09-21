from base64 import urlsafe_b64decode


def parse_parts(service, parts, message):
    """
    Utility function that parses the content of an email partition
    """
    if parts:
        for part in parts:
            mime_type = part.get("mimeType")
            body = part.get("body")
            data = body.get("data")
            if part.get("parts"):
                # recursively call this function when we see that a part
                # has parts inside
                parse_parts(service, part.get("parts"), message)
            if mime_type == "text/plain":
                # if the email part is text plain
                if data:
                    text = urlsafe_b64decode(data).decode()
                    print(text)


# modify read message function to return an email object??

def read_message(service, message):
    """
    This function takes Gmail API `service` and the given `message_id` and does the following:
        - Downloads the content of the email
        - Prints email basic information (To, From, Subject & Date) and plain/text parts
        - Downloads text/html content (if available) and saves it under the folder created as index.html
        - Downloads any file that is attached to the email and saves it in the folder created
    """
    msg = service.users().messages().get(userId='me', id=message['id'], format='full').execute()
    # parts can be the message body, or attachments
    payload = msg['payload']
    headers = payload.get("headers")
    parts = payload.get("parts")
    has_subject = False
    if headers:
        # this section prints email basic info
        for header in headers:
            name = header.get("name")
            value = header.get("value")
            # print_mail(name, value)
            if name.lower() == "subject":
                # make our boolean True, the email has "subject"
                has_subject = True
                location = value
                # we will also handle emails with the same subject name
            if name.lower() == 'from':
                return_to = value;
    if not has_subject:
        # set location to 0,0 to trigger error message
        location = "0,0"
    parse_parts(service, parts, message)
    return [location, return_to]

# helper function used in development and debugging
def print_mail(name, value):
    if name.lower() == 'from':
        # we print the From address
        print("From:", value)
    if name.lower() == "to":
        # we print the To address
        print("To:", value)
    if name.lower() == "subject":
        # make our boolean True, the email has "subject"
        has_subject = True
        # we will also handle emails with the same subject name
        print("Subject:", value)
    if name.lower() == "date":
        # we print the date when the message was sent
        print("Date:", value)
