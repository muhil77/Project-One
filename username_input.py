#commandline interface to accept usernames and passwords

def enter_username(number_of_names, usernames_passwords):
    for num in range(0, number_of_names):
        username = raw_input("Enter username \n")
        password = raw_input("Enter password \n")
        usernames_passwords.update({username : password})
        #usernames_passwords.append(int(raw_input("Enter passwords")))

#function to save dictionary to CSV
def save_CSV(filename, dictionary,):
    import csv
    with open(filename, 'wb') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in dictionary.items():
            writer.writerow([key, value])

#function to read dictionary from csv
def read_CSV(filename, dictionary):
    import csv
    with open(filename, 'rb') as csv_file:
        reader = csv.reader(csv_file)
        mydict = dict(reader)
    print mydict

number_of_users = int(raw_input("Enter number of users \n"))
usernames_passwords = {}
enter_username(number_of_users, usernames_passwords)
save_CSV('usernames_passwords_plaintext.csv', usernames_passwords)
read_CSV('usernames_passwords_plaintext.csv', usernames_passwords)
