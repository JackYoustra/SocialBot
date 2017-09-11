import json
from parsing.user import User
user_id_map = {"<redacted>" : "Jack", "<redacted>" : "<redacted>"}
<redacted>_focus = False
user_name_map = {v: k for k, v in user_id_map.items()}

user_words = {"Jack" : [], "<redacted>" : []}

with open("../resources/Hangouts.json", "r", encoding="utf8") as hangouts_file:
    parsed_file = json.load(hangouts_file)
conversation_shells = parsed_file["conversation_state"]
#exit(1)
for conversation_shell in conversation_shells:
    chat = conversation_shell["conversation_state"]
    #for focusing on conversations only between two ppl
    if <redacted>_focus:
        quit_early = True

        for participant in chat["conversation"]["participant_data"]:
            id = participant["id"]
            <redacted> = user_name_map["<redacted>"]
            if id["gaia_id"] == <redacted> or id["chat_id"] == user_name_map["<redacted>"]:
                quit_early = False
        if quit_early: continue

    events = chat["event"]
    for event in events:
        if event["event_type"] == "REGULAR_CHAT_MESSAGE":
            sender_id = event["sender_id"]
            current_user = user_id_map.get(sender_id["gaia_id"]) or user_id_map.get(sender_id["chat_id"])
            if current_user:
                segments = event["chat_message"]["message_content"].get("segment") or []
                for segment in segments:
                    if segment["type"] == "TEXT":
                        text = segment["text"]
                        user_words[current_user] += [text]

target_user_list = []
for name, words in user_words.items():
    user = User(name, words)
    target_user_list.append(user)