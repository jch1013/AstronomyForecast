import makeReport
import emailFunctions as email
import readEmails
import coordinates




test_location = [47.6, -122.3]


# report_text = makeReport.make_report(test_location[0], test_location[1])
# print(report_text)

def main():
    # get all emails currently in the inbox
    service = email.gmail_authenticate()
    results = email.search_messages(service, "lemon")

    # get subject and sender from every email in inbox
    locations_and_users = []
    for mail in results:
        data = readEmails.read_message(service, mail)
        locations_and_users.append(data)

    print(locations_and_users)
    print("\nNumber of emails found: " + str(len(locations_and_users)))




main()
