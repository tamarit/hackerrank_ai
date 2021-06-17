
import re

def keyword_present(sent):
    keywords = ["announce", "shares", "App Store", "Mac", "iPad", "iPhone", "censorship", "Apple products", "secretive", "declined"]
    for k in keywords:
        if k in sent:
            return True
    return False

def apple_or_apple(sentences):
    for sent in sentences:
        sent_without_first_apple =  re.sub("^Apple", "", sent)
        sent_without_apple_after_dot = re.sub("\.\s*Apple", "", sent_without_first_apple)
        if (
                    (("Apple" in sent_without_apple_after_dot or "Apple's" in sent) and ((re.search("apple(s?)", sent) is None and re.search("(an apple)|(apple (juice|crumble))", sent, re.I) is None )or keyword_present(sent))) 
                or  ("Apple" in sent and keyword_present(sent))
            ):
            print("computer-company")
        else:
            print("fruit")

if __name__ == "__main__":
    num_sentences = int(input().strip())
    sentences = [input().strip() for i in range(num_sentences)]
    apple_or_apple(sentences)