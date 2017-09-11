from parsing import aggregator
import winsound

def guess_user(phrase, user_list):
    user_score = {k:0 for k in user_list}
    for word in phrase.split():
        for user in user_list:
            result = user.wordMap.get(word)
            if result != None and result != 0:
                user_score[user] += result/len(user.wordLinesList)
    flipped = {v:k for k, v in user_score.items()}
    return flipped[max(flipped.keys())]

if __name__ == "__main__":
    user_list = aggregator.target_user_list
    num_correct = 0
    num_tried = 0
    nailed_it = {}
    problems = {} #(guess:real)
    for user in user_list:
        for message in user.messageList:
            result = guess_user(message, user_list)
            if result == user:
                num_correct += 1
                if nailed_it.get(user) == None:
                    nailed_it[user] = 0
                else:
                    nailed_it[user] += 1
            else:
                tp = "Guess: " + result.name + ", Real: " + user.name
                if problems.get(tp) == None:
                    problems[tp] = 0
                else:
                    problems[tp] += 1
            num_tried += 1
    print("Accuracy: " + str((num_correct / num_tried) * 100) + "%")
    for statement, v in problems.items():
        print(statement + " " + str(v) + " number of times")
    for user, v in nailed_it.items():
        print("Nailed it for " + user.name + " " + str(v) + " times. Subaccuracy: " + str((v / len(user.messageList)) * 100) + "%")
    winsound.MessageBeep() # come back when it beeps :)