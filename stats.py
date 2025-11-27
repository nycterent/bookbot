
def get_num_words(text):
    words = len(text.split())
    print(f"Found {words} total words found in the document")

def get_num_chars(text):
    cdoct = {}
    for c in list(text.replace(" ", "")):
        c = c.lower()
        try:
            cdoct[c] = cdoct[c] + 1
        except:
            cdoct[c] = 1
    return cdoct

def sort_chars(cdoct):
    return sorted(cdoct.items(), key=lambda x: x[1], reverse=True)
