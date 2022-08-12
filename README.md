# Lab 19
## Automation
### Author: Yu-Wei Hsieh
### Setup
Requirements:
- .venv

### Run the application
Inside [automation](automation) folder execute ``python check.py``

### Assets
- [potential-contacts.txt](/automation/assets/potential-contacts.txt)
-the raw text file
- [email.txt](automation/assets/emails.txt)
-the email list from raw text file
- [phone_numbers.txt](automation/assets/phone_numbers.txt)
-the phone number list from raw text file
- [existing-contacts.txt](automation/assets/existing-contacts.txt)
-(stretch goal) compare collected data with this file and only include info NOT already in system
- [NOT_IN_DATABASE_emails.txt](automation/assets/stretch_goal/NOT_IN_DATABASE_emails.txt)
-(stretch goal) the email list NOT in [existing-contacts.txt](automation/assets/existing-contacts.txt)
- [NOT_IN_DATABASE_phone_numbers.txt](automation/assets/stretch_goal/NOt_IN_DATABASE_phone_numbers.txt)
-(stretch goal) the phone number list NOT in [existing-contacts.txt](automation/assets/existing-contacts.txt)
- [NOT_IN_DATABASE_extensions.txt](automation/assets/stretch_goal/NOT_IN_DATABASE_extensions.txt)
-(stretch goal) the phone numbers with extension list NOT in [existing-contacts.txt](automation/assets/existing-contacts.txt)
- [extensions.txt](automation/assets/stretch_goal/extensions.txt)
-(stretch goal) handle phone numbers with extensions