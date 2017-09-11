import re
from parsing.user import User

blacklist = ["| Removed", "Call to ", "Call ended", "***  ***"]

raw_lines = []
with open("../resources/messages-<redacted>.txt", "r") as ins:
    for line in ins:
        raw_lines.append(line)

unremoved_list = []
for line in raw_lines:
    inclusion = True
    for black in blacklist:
        if black in line:
            inclusion = False
            break
    if inclusion:
        unremoved_list.append(line)

unremoved_<redacted> = []
unremoved_jack = []
pattern = re.compile("\[.*\][^:]*")
lastMatchingIndex = 0
current_list = None
for index, line in enumerate(unremoved_list):
    last = pattern.search(line)
    if last == None:
        #append to previous, replace newline with space
        unremoved_list[lastMatchingIndex] = unremoved_list[lastMatchingIndex] + " " + line
        current_list[len(current_list) - 1] = unremoved_list[lastMatchingIndex]
    else:
        if last.string.find("Jack") != -1:
            current_list = unremoved_jack
        elif last.string.find("<redacted>") != -1:
            current_list = unremoved_<redacted>
        else:
            print("error:" + line)
        message_start = last.span()[1] + 2
        unremoved_list[index] = line[message_start:-1]
        current_list.append(unremoved_list[index])
        lastMatchingIndex = index

<redacted> = User("<redacted>", unremoved_<redacted>)
jack = User("Jack", unremoved_jack)
target_user_list = [<redacted>, jack]

if __name__ == "__main__":
    for user in target_user_list:
        print(user)