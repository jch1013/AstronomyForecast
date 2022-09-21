import makeReport
import emailFunctions as email
import readEmails
import coordinates
import sendEmails


def main():
    # get all emails currently in the inbox
    service = email.gmail_authenticate()
    results = email.search_messages(service, "")

    # create a list of all subject lines for deletion later
    all_subjects = []
    replies = 0
    # get subject and sender from every email in inbox
    for mail in results:
        data = readEmails.read_message(service, mail)
        location = data[0]
        all_subjects.append(location)
        destination = data[1]
        coords = coordinates.lat_long(data[0])
        report_body = makeReport.make_report(coords[0], coords[1])
        sendEmails.send_message(service, destination, "Forecast for " + location, report_body)
        replies += 1

    print("Number of emails found: " + str(len(results)))
    print("Number of replies sent: " + str(replies))

    deletions = 0
    for subject in all_subjects:
        try:
            email.delete_messages(service, subject)
            deletions += 1
        except:
            continue

    print("Number of emails deleted: " + str(deletions))


main()






# -----Tests-----
