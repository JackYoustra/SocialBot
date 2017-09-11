from learning.markov_model import markovify_model
import parsing.fb_parser as fparse
#import parsing.hangouts_parser as hparse
#import parsing.skype_parser as sparse
from parsing import aggregator

if __name__ == "__main__":
    # for user in aggregator.target_user_list:
    #     print(user)
    # print("-----------------------------------")
    #
    # for user in fparse.target_user_list:
    #     print(user + "\n")
    #     print("------------------------")
    #     model = markovify_model(user.wordLinesList, state_size=3)
    #     i = 0
    #     while i < 10:
    #         sentence = model.make_sentence()
    #         if sentence:
    #             print(sentence)
    #             i += 1
    #
    # exit(1)

    for user in aggregator.target_user_list:
        print("\n" + str(user))
        model = markovify_model(user.wordLinesList, state_size=3)
        i = 0
        while i < 5:
            sentence = model.make_sentence()
            if sentence:
                print(sentence)
                i += 1