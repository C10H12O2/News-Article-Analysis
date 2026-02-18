import re
def count_specific_word(text, search_word):
    if not text or not search_word:
        return 0
    
    text_lower = text.lower()
    search_lower = search_word.lower()
    
    words = re.findall(r'\b\w+\b', text_lower)
    count = words.count(search_lower)
    return count