import re
def count_specific_word(text, search_word):
    if not text or not search_word:
        return 0
    
    text_lower = text.lower()
    search_lower = search_word.lower()
    
    words = re.findall(r'\b\w+\b', text_lower)
    count = words.count(search_lower)
    return count

def identify_most_common_word(text):
    if not text:
        return None
    text_lower = text.lower()
    words = re.findall(r'\b\w+\b', text_lower)
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] +=1
        else:
            word_count[word] = 1
    
    most_common = None
    max_count = 0    
    for word, count in word_count.items():
        if count > max_count:
            max_count = count
            most_common = word
    return most_common

def calculate_average_word_length(text):
    if not text or not text.strip():
        return 0.0
    words = re.findall(r'\b\w+\b', text)
    if not words:
        return 0.0
    total_length = 0
    for word in words:
        total_length += len(word)
        
    average_length = total_length / len(words)
    return average_length

def count_paragraphs(text):
    if not text or not text.strip():
        return 1
    paragraphs = text.split('\n\n')
    non_empty_paragraphs = []
    for para in paragraphs:
        if para.strip():
            non_empty_paragraphs.append(para)
    
    paragraph_count = len(non_empty_paragraphs)
    if paragraph_count == 0:
            return 1
    return paragraph_count                

def count_sentences(text):
    if not text or not text.strip():
        return 1
    sentences = re.split(r'[.!?]+', text)
    non_empty_sentences = []
    for sentence in sentences:
        if sentence.strip():
            non_empty_sentences.append(sentence)
            
    sentence_count = len(non_empty_sentences)
    if sentence_count == 0:
        return 1    
    return sentence_count
    
    
    
    
    
                    
                
                
    