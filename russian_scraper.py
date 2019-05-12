from selenium import webdriver
import time
import utils

driver = webdriver.Chrome()
driver.get('https://vk.com')
utils.login(driver, 'yourEmail', 'yourPassword') # vk creds go here

# scroll a bunch
for i in range(50):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

# get words from posts
posts = driver.find_elements_by_class_name('wall_post_text')
wordlist = []
for post in posts:
    words = post.text.lower().split()
    for word in words:
        wordlist.append(word)

clean_wordlist = utils.clean_wordlist(wordlist)
top_ten_words = utils.get_top_ten_words(clean_wordlist)
top_ten_words_eng = utils.translate_wordlist(top_ten_words)

print('Words Collected: ', len(wordlist))
print('Russians are saying these words today:')
for i in range(10):
    print(' ', top_ten_words[i], ': ', top_ten_words_eng[i])

driver.close()