# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content():
    f = open('story.txt','r')
    content = f.read() 
    print(content)
    f.close()

read_file_content()


def count_words():
    text = open('story.txt','r')
    counts = dict()

    for line in text:
        line = line.strip()
        line = line.lower().replace('.', '').replace(',', '').replace('?', '')
        words = line.split(" ")
    
        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1

    for key in list(counts.keys()):
        print(key, ':', counts[key])
    text.close()

count_words()
