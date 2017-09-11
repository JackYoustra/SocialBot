from html.parser import HTMLParser
from parsing.user import User

target_names = {"Jack" : ["<redacted>@facebook.com", "Jack Youstra"], "<redacted>" : ["<redacted>@facebook.com", "<redacted>"], "<redacted>" : ["<redacted>@facebook.com", "<redacted>"]} #user ID or actual name

total_user_list = {}

class FBMessageParser(HTMLParser):
    def __init__(self):
        super(FBMessageParser, self).__init__()
        self.in_user = False
        self.in_message = False
        self.message_data_reading = False
        #self.user = ""

    def handle_starttag(self, tag, attrs):
        if tag == "div":
            if len(attrs) == 1 and attrs[0][0] == "class":
                first = attrs[0][1]
                if first == "message_header":
                    self.in_message = True
                else:
                    self.in_message = False
        if tag == "span":
            if len(attrs) == 1 and attrs[0][0] == "class":
                first = attrs[0][1]
                if first == "user":
                    self.in_user = True
                    pass
                if first == "meta":
                    pass
        elif tag == "p":
            if self.in_message:
                self.message_data_reading = True

    def handle_endtag(self, tag):
        if tag == "p":
            self.message_data_reading = False
        if tag == "span":
            self.in_user = False

    def handle_data(self, data):
        if self.in_user:
            self.user = data
        if self.message_data_reading:
            messages = total_user_list.get(self.user)
            if messages == None:
                total_user_list[self.user] = [data]
            else:
                messages.append(data)

data = ""
with open("../resources/jack_fb_messages.htm", "r", encoding="utf8") as myfile:
    data = myfile.read().replace('\n', '')

parser = FBMessageParser()
parser.feed(data)

end_user_set = {}

for name, aliases in target_names.items():
    for alias in aliases:
        target = total_user_list.get(alias)
        if target != None:
            # the alias exists in our messages list
            if not name in end_user_set:
                end_user_set[name] = target
            else:
                end_user_set[name] += target # append to list


target_user_list = []
for name, messages in end_user_set.items():
    user = User(name, messages)
    target_user_list.append(user)



