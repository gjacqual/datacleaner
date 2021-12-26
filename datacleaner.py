from passwordGenerator import passgen
import re


# Function for creating email addresses from first and last names
# The code of the email_gen function was originally specified in the task and slightly changed
def email_generator(names):
    emails = []

    for name in names:
        letter = 2
        while name[1] + '.' + name[0][0:letter] + '@corporation.com' in emails:
            letter += 1
        emails.append(name[1] + '.' + name[0][0:letter] + '@corporation.com')
    return emails


def check_names(string):
    if re.findall(r'^[A-Za-z]*$', string) and re.match(r'^[A-Z][a-z]', string):
        return True
    else:
        return False


# Below is my task implementation code
f = open('task_file.txt', 'r')
file_errors = open('error_file.txt', 'w')
list_names = []
lines = []
for line in f:
    tmp_list = []
    split_line = line.split(', ')
    lines.append(split_line)
    if split_line[1] != '' and split_line[2] != '' and len(split_line[3]) == 7 and split_line[4] != '':
        tmp_list.append(split_line[1])
        tmp_list.append(split_line[2])
        list_names.append(tmp_list)
list_emails = email_generator(list_names)
f.close()
f = open('task_file.txt', 'w')
j = 0

for line in lines:
    if line[0] == 'EMAIL':
        line[4] = 'CITY'
        line.append('PASSWORD\n')
        line = ", ".join(line)
        f.write(line)
        continue
    if line[1] != '' and line[2] != '' and len(line[3]) == 7 and line[4] != '':
        if not check_names(line[1]) or \
                not check_names(line[2]) or \
                not re.findall(r'^[A-Za-z-.]*$', line[4]) or \
                not re.findall(r'^[0-9]*$', line[3]):
            line = ", ".join(line)
            file_errors.write(line)
            continue
        line[4] = line[4][:-1]
        password = passgen(12)
        line.append(password)
        line = ", ".join(line)
        line = list_emails[j] + line + '\n'
    else:
        line = ", ".join(line)
        file_errors.write(line)
        continue
    f.write(line)
    j += 1
f.close()
file_errors.close()
