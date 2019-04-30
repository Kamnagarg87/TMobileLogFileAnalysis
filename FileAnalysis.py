import datetime
import csv

timestamp = ""
callId = ""
timestamp = ""
callPressed = ""
voiceAccessNetworkband = "0"
RTPDownlinkStatusDelay = "0"
RTPDownlinkStatusLossRate = "0"
ENDED = "0"
line = ""
rows = []
fields = ["Timestamp","Call_Pressed","CallID","RTPDownlinkStatusJitter","RTPDownlinkStatusDelay","RTPDownlinkStatusLossRate","ENDED"]


logFile = input("Enter path to file to read? ")
writefile = input("Enter name of the CSV file with .csv extension")

with open(logFile, 'rt') as myfile:
        for myline in myfile:

            if myline.__contains__("oemIntentTimestamp"):
                timestamp = datetime.datetime.fromtimestamp(int(myline.split(" ")[1]) / 1000)

            if myline.__contains__("CallID"):
                callId = myline.split(" ")[1]
            if myline.__contains__("CALL_PRESSED"):
                callPressed = "CALL_PRESSED"
            if myline.__contains__("VoiceAccessNetworkStateBand "):
                voiceAccessNetworkband = myline.split(" ")[1]
            if myline.__contains__("RTPDownlinkStatusDelay"):
                RTPDownlinkStatusDelay = myline.split(" ")[1]
            if myline.__contains__("RTPDownlinkStatusLossRate"):
                RTPDownlinkStatusLossRate = myline.split(" ")[1]
            if myline.__contains__("ENDED"):
                ENDED = "ENDED"

            if myline == "\n" and timestamp != "":
                line = timestamp.strftime(
                    '%m/%d/%y %H:%M:%S.%f%z') + "," + callPressed + "," + callId + "," + voiceAccessNetworkband + ","\
                       + RTPDownlinkStatusDelay + "," + RTPDownlinkStatusLossRate + "," + ENDED
                print(line)
                rows.append(line)
                callId = ""
                timestamp = ""
                callPressed = ""
                voiceAccessNetworkband = "0"
                RTPDownlinkStatusDelay = "0"
                RTPDownlinkStatusLossRate = "0"
                ENDED = "0"
myfile.close()
with open(writefile, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)

    for row in rows:
        csvfile.write(row + "\n")
    csvfile.close()


