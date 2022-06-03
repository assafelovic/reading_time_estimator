import bs4
import urllib.request, re

# Words per minute
WPM = 200
WORD_LENGTH = 5

# 1
def extract_text(url):
	html = urllib.request.urlopen(url).read()
	soup = bs4.BeautifulSoup(html, 'html.parser')
	texts = soup.findAll(text=True)
	return texts

def is_visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif isinstance(element, bs4.element.Comment):
        return False
    elif element.string == "\n":
    	return False
    return True

# 2
def filter_visible_text(page_texts):
	return filter(is_visible, page_texts)

def count_words_in_text(text_list, word_length):
	total_words = 0
	for current_text in text_list:
		total_words += len(current_text)/word_length
	return total_words

# 3
def estimate_reading_time(url):
	texts = extract_text(url)
	filtered_text = filter_visible_text(texts)
	total_words = count_words_in_text(filtered_text, WORD_LENGTH)
	return total_words/WPM

print(estimate_reading_time("http://www.assafelovic.com/blog/2017/6/27/estimating-an-articles-reading-time"))
