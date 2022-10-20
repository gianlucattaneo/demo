from email import header
from requests_html import HTMLSession
import bs4

def download_file(url):
    local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename



def download_serie(url):
    session = HTMLSession()
    r = session.get(url)
    # r.html.render()

    doc = bs4.BeautifulSoup(r.html.raw_html, 'html.parser')
    doc = doc.findAll('div', {'id':'video-top'})

    print(doc)

if __name__ == '__main__':
    url = "https://www.animeunity.tv/anime/274-inazuma-eleven-go-ita"
    download_serie(url)
