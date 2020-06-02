## import modules here 
import math
################# Question 1 #################
def multinomial_nb(training_data, sms):# do not change the heading of the function
    #create a list to store all word
    word_list = set([])
    #create two dictionaries to store ham/spam word and their frequencies
    ham_dict = {}
    spam_dict = {}
    #init
    count_ham = count_spam = 0
    num_ham = 0
    num_spam = 0

    for (dict, category) in training_data:
        #store all word in training data
        for i in dict.keys():
            word_list.add(i)
        #ham sms
        if category == 'ham':
            for key, value in dict.items():
                #new ham word
                if key not in ham_dict:
                    ham_dict[key] = value
                #existed ham word
                else:
                    ham_dict[key] += value
                count_ham += value
            num_ham += 1
        #spam sms
        elif category == 'spam':
            for key, value in dict.items():                                             
                #new spam word
                if key not in spam_dict:
                    spam_dict[key] = value
                #existed spam word
                else:
                    spam_dict[key] += value
                count_spam += value
            num_spam += 1
    
    #compute probability of ham and spam
    #use log to prevent underflow(The probability is too small and there are too many words)
    pro_ham = math.log(num_ham)
    pro_spam = math.log(num_spam)

    for i in sms:
        #not in word list, keep value
        if i not in word_list:
            pro_ham += 0
            pro_spam += 0
        #word in ham dictionary
        elif i in ham_dict:
            pro_ham += math.log((ham_dict[i] + 1) / (count_ham + len(word_list)))
            pro_spam += math.log(1 / (count_spam + len(word_list)))
        #word in spam dictionary
        else:
            pro_ham += math.log(1 / (count_ham + len(word_list)))
            pro_spam += math.log((spam_dict[i] + 1) / (count_spam + len(word_list)))
    
    #get result and return
    ratio = math.exp(pro_spam) / math.exp(pro_ham)
    return ratio