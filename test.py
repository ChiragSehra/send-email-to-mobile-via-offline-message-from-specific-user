import imaplib
import email

user = 'chiragsehradeveloper@gmail.com'
password = 'Chirag2212#'
imap_url = 'imap.gmail.com'


# Function to fetch email body and headers.

def get_body(msg):
    if msg.is_multipart():
        return get_body((msg.get_payload(0)))
    else:
        return msg.get_payload(None, True)


# Function to search for a key value pair in the email

def search(key, value, con):
    result, data = con.search(None, key, '"{}"'.format(value))
    return data


# Function to get list of emails under a label

def get_emails(result_bytes):
    msgs = []  # to push all email data here
    for num in result_bytes[0].split():
        typ, data = con.fetch(num, '(RFC822)')
        msgs.append(data)

    return msgs


# making an SSL connection with GMAIL
con = imaplib.IMAP4_SSL(imap_url)

# logging the user in
con.login(user, password)

# Check email under a label
con.select('Inbox')

# fetching emails from specific user 'srijan.anand@valiancesolutions.com '
msgs = get_emails(search('FROM', 'chiragsehra42@gmail.com', con))

# print(msgs)


for msg in msgs[::-1]:
    for sent in msg:
        if type(sent) is tuple:

            # encoding set as utf-8
            content = str(sent[1], 'utf-8')
            data = str(content)

            # Handling errors related to unicodenecode
            try:
                indexstart = data.find("ltr")
                data2 = data[indexstart + 5: len(data)]
                indexend = data2.find("</div>")

                # printtng the required content which we need
                # to extract from our email i.e our body
                print(data2[0: indexend])

            except UnicodeEncodeError as e:
                pass
