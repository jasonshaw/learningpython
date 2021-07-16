import requests
import re
import json

def request_dandan(url):
    try:
        #Sync request
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
         return None

def parse_result(html):
    pattern = re.compile('<li>.*?list_num.*?(\d+).</div>.*?class="name".*?title="(.*?)">',re.S)
    items = re.findall(pattern, html)
    return items

def write_item_to_file(item):
    print('Start writing data ====> ' + str(item))
    with open('book.txt', 'a', encoding='UTF-8') as f:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')

def main(page):
    url = 'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-' + str(page)
    html = request_dandan(url)
    items = parse_result(html)
    for item in items:
        write_item_to_file(item)

if __name__ == "__main__":
    for i in range(1,5):
        main(i)