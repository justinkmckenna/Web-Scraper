import time
from collections import Counter 
import nltk
from nltk.corpus import stopwords

def login(driver, email, password):
    index_email = driver.find_element_by_id('index_email')
    index_pass = driver.find_element_by_id('index_pass')
    index_login_button = driver.find_element_by_id('index_login_button')
    index_email.send_keys(email)
    index_pass.send_keys(password)
    index_login_button.click()
    time.sleep(5)

def remove_symbols(wordlist):
    new_wordlist = []
    for word in wordlist: 
        symbols = '!@#$%^&*()_-+={[}]|\;:"<>?/., '
        for i in range (0, len(symbols)): 
            word = word.replace(symbols[i], '')      
        if len(word) > 0: 
            new_wordlist.append(word) 
    return new_wordlist

def remove_stopwords(wordlist):
    stop_words = set(stopwords.words('russian'))
    new_wordlist = filter(lambda w: not w in stop_words, wordlist)
    return new_wordlist

def clean_wordlist(wordlist): 
    clean_wordlist = remove_symbols(wordlist)
    clean_wordlist = remove_stopwords(clean_wordlist)
    clean_wordlist = filter(lambda w: not w.isdigit(), clean_wordlist)
    return clean_wordlist

def get_word_count(clean_wordlist):
    word_count = {} 
    for word in clean_wordlist: 
        if word in word_count: 
            word_count[word] += 1
        else: 
            word_count[word] = 1
    return word_count

def get_top_ten_words(wordlist):
    word_count = get_word_count(wordlist)
    counter = Counter(word_count)
    top_ten_words = counter.most_common(10) 
    top_ten_words = [a for a, b in top_ten_words]
    return top_ten_words

def translate_wordlist(wordlist):
    from google.cloud import translate
    translate_client = translate.Client()
    translate = lambda w: translate_client.translate(w, target_language = 'en')['translatedText']
    new_wordlist = list(map(translate, wordlist))
    return new_wordlist