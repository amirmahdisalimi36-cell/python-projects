# Contact Book - Simple Validation

new_contact = input('Do you want to add a new contact? (yes/no): ').lower()

if new_contact == 'yes':
    # Get contact details
    first_name = input('Please insert your contact first name: ')
    last_name = input('Please insert your contact last name: ')
    
    # Phone number validation
    source_phone_prefix = ('0914', '0912', '0918', '0917', '0915',
                           '0916', '0911', '0993', '0992', '0990',
                           '0910', '0994', '0991', '0996', '0932',
                           '0930', '0933', '0900', '0998')
    
    phone_num = input('Contact Number (11 digits): ').strip()
    
    if len(phone_num) != 11:
        print('Error: phone number must be exactly 11 digits')
    elif not phone_num.isdigit():
        print('Error: phone number must contain only digits')
    elif phone_num[:3] not in source_phone_prefix:
        print('Error: invalid phone prefix')
    else:
        print('Your number is OK ✅')
    
    # Email validation
    email = input('Please insert your contact email: ').strip()
    
    if email.count('@') == 1:
        if email.startswith('@') or email.endswith('@'):
            print('Error: invalid email format')
        else:
            email_splitter = email.split(sep='@')
            domain = email_splitter[1]
            domain_list = ['yahoo.com', 'gmail.com']
            
            if domain in domain_list:
                print('Email is OK ✅')
            else:
                print('Error: domain not supported')
    else:
        print('Error: invalid email format (must contain exactly one @)')

else:
    print('No new contact added.')