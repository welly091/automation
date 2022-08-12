import re

def handle_phone_numbers(text):
    """
    Find the strings in text that match with phone number regular expression.
    :param text: text file content
    :return: None
    """
    #Define the regex for phone number
    regex_phone =r"\(?\d{3}\)?-?.?\d{3}-?.?\d{4}"

    #Find a list contains strings that match phone number
    phone_numbers = re.findall(regex_phone, text)
    for index in range(len(phone_numbers)):
        new_number = ""
        for i in phone_numbers[index]:
            if re.match(r"\d", i):
                new_number += i
        phone_numbers[index] = new_number[0:3] + "-" + new_number[3:6] + "-" + new_number[6:]

    #Sort the phone numbers
    phone_numbers = sorted(list(set(phone_numbers)))

    #Write into a file
    with open("assets/phone_numbers.txt", "w") as pn_file:
        for i in phone_numbers:
            pn_file.write(i + '\n')

def handle_emails(text):
    """
    Find the strings in text that match with email regular expression.
    :param text: text file content
    :return: None
    """
    #Define the regex for email
    regex_email = r"\w+\@[0-9a-zA-Z'-]+\.com|\w+\@[0-9a-zA-Z'-]+\.info|\w+\@[0-9a-zA-Z'-]+\.biz|\w+\@[0-9a-zA-Z'-]+\.edu|\w+\@[0-9a-zA-Z'-]+\.net|\w+\@[0-9a-zA-Z'-]+\.org"
    emails = re.findall(regex_email, text)

    #Sort the list
    emails = sorted(list((set(emails))))

    #Write into a file
    with open("assets/emails.txt", 'w') as email_file:
        for i in emails:
            email_file.write(i + '\n')

######################
#### Stretch Goal ####
######################

def handle_phone_numbers_extensions(text):
    """
    Find the strings in text that match with phone number with extentions regular expression.
    :param text: text file content
    :return: None
    """
    #Define the regex for phone number with extentions
    regex_phone = r"\(?\d{3}\)?-?.?\d{3}-?.?\d{4}x\d+"
    phone_numbers = re.findall(regex_phone,text)

    #Write into a file
    with open("assets/stretch_goal/extensions.txt", 'w') as extentions:
        for i in set(phone_numbers):
            extentions.write(i + '\n')

def compared_existing():
    """
    Compare your collected data against existing-contacts.txt and only include info NOT already in system.
    :return: None
    """
    def filter_out(lines_list, file_name, original_file_name):
        the_list = []
        with open(f"assets/{original_file_name}", "r") as o:
            lines = o.readlines()

            for i in lines:
                print(i[0:-1])
                if i[0:-1] not in lines_list:
                    the_list.append(i)
        with open (f"assets/stretch_goal/{file_name}", "w") as f:
            for i in the_list:
                f.write(i + '\n')
    p = []
    e = []
    x = []
    with open("assets/existing-contacts.txt") as existing_f:
            text = existing_f.read()
            # Handle phone numbers
            regex_phone = r"\(?\d{3}\)?-?.?\d{3}-?.?\d{4}"
            regex_email = r"\w+\@[0-9a-zA-Z'-]+\.com|\w+\@[0-9a-zA-Z'-]+\.info|\w+\@[0-9a-zA-Z'-]+\.biz|\w+\@[0-9a-zA-Z'-]+\.edu|\s\w+\@[0-9a-zA-Z'-]+\.net|\w+\@[0-9a-zA-Z'-]+\.org"
            regex_phone_ex = r"\(?\d{3}\)?-?.?\d{3}-?.?\d{4}x\d+"


            x = re.findall(regex_phone_ex, text)
            print(x)

            p = re.findall(regex_phone, text)
            for index in range(len(p)):
                new_number = ""
                for i in p[index]:
                    if re.match(r"\d", i):
                        new_number += i
                p[index] = new_number[0:3] + "-" + new_number[3:6] + "-" + new_number[6:]
            print(p)
            e = re.findall(regex_email, text)
            print(e)


    filter_out(p,"NOt_IN_DATABASE_phone_numbers.txt", "phone_numbers.txt")
    filter_out(e, "NOT_IN_DATABASE_emails.txt", "emails.txt")
    filter_out(x, "NOT_IN_DATABASE_extensions.txt", 'stretch_goal/extensions.txt')



if __name__ == '__main__':
    with open("assets/potential-contacts.txt") as file:
        text = file.read()
        handle_phone_numbers(text)
        handle_emails(text)
        handle_phone_numbers_extensions(text)
    compared_existing()
