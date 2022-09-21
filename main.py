import getWeather
import makeReport
import emailFunctions as email
import readEmails
import coordinates
import sendEmails



test_location = [47.6, -122.3]


# report_text = makeReport.make_report(test_location[0], test_location[1])
# print(report_text)

def main():
    # get all emails currently in the inbox
    service = email.gmail_authenticate()
    results = email.search_messages(service, "miami")

    # get subject and sender from every email in inbox
    for mail in results:
        data = readEmails.read_message(service, mail)
        location = data[0]
        destination = data[1]
        coords = coordinates.lat_long(data[0])
        report_body = makeReport.make_report(coords[0], coords[1])
        sendEmails.send_message(service, destination, "Forecast for " + location, report_body)


    print("\nNumber of emails found: " + str(len(results)))

main()






# -----Tests-----
