import wikipedia

def get_text_for_topic(name_topic):
    # result = wikipedia.search(name_topic, results = 5)
    # print(result)
    # topic1 = wikipedia.page(result[1])
    topic1 = wikipedia.page(name_topic)
    print('Title of the topic : ', topic1.title)
    print(topic1.url)
    # print('Number of characters in the document : ',len(topic1.content))
    return topic1.content

if __name__ == "__main__":
    name_topic = 'Climate change'
    text = get_text_for_topic(name_topic)
