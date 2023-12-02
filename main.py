def split_wordlist(input_file, output_usernames, output_passwords):
    usernames = []
    passwords = []

    with open(input_file, 'r') as file:
        for line in file:
            parts = line.strip().split(':')
            if len(parts) == 2:
                usernames.append(parts[0])
                passwords.append(parts[1])

    with open(output_usernames, 'w') as usernames_file:
        usernames_file.write('\n'.join(usernames))

    with open(output_passwords, 'w') as passwords_file:
        passwords_file.write('\n'.join(passwords))


# Usage example
# Replace this with the path to your wordlist file
input_wordlist = 'ftp-betterdefaultpasslist.txt'
output_usernames_list = 'usernames.txt'  # Replace with the desired output path for usernames
output_passwords_list = 'passwords.txt'  # Replace with the desired output path for passwords

split_wordlist(input_wordlist, output_usernames_list, output_passwords_list)
