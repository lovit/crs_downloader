import os
import requests
import time


category_links = [
    ('General National Security Topics', 'https://fas.org/sgp/crs/natsec/index.html'),
    ('Defense Primers', 'https://fas.org/sgp/crs/natsec/primer.html'),
    ('Middle East', 'https://fas.org/sgp/crs/mideast/index.html'),
    ('Foreign Policy and Regional Affairs', 'https://fas.org/sgp/crs/row/index.html'),
    ('Secrecy and Information Policy', 'https://fas.org/sgp/crs/secrecy/index.html'),
    ('Intelligence', 'https://fas.org/sgp/crs/intel/index.html'),
    ('Homeland Security', 'https://fas.org/sgp/crs/homesec/index.html'),
    ('Nuclear Weapons and Arms Control', 'https://fas.org/sgp/crs/nuke/index.html'),
    ('Conventional Weapons Systems', 'https://fas.org/sgp/crs/weapons/index.html'),
    ('Terrorism', 'https://fas.org/sgp/crs/terror/index.html'),
    ('Miscellaneous Topics', 'https://fas.org/sgp/crs/misc/index.html')
]


def download(url, fname):
    """
    Arguments
    --------
    url : str
        URL address of file to be downloaded
    fname : str
        Download file address
    Returns
    -------
    flag : Boolean
        It return True if downloading success else return False
    """

    # If you do not set user-agent, downloading from url is stalled.
    headers = {'user-agent': 'Wget/1.16 (linux-gnu)'}
    try:
        r = requests.get(url, stream=True, headers=headers)
        with open(fname, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        return True
    except Exception as e:
        print(e)
        return False

def parse_href(link):
    href = link.attrs['href']
    if url_pattern.match(href):
        return href
    return None

def as_url(url_base, category, fname):
    return '{}{}/{}'.format(url_base, category, fname)

def download_from_a_category(category_url, directory, sleep=0.1, debug=False):
    """
    Arguments
    ---------
    category_url : str
        URL of front page
        eg. https://fas.org/sgp/crs/natsec/index.html
    directory : str
        Directory path to save downloaded files
    sleep : float
        Sleep time for downloading a file.
        Default is 0.1
    debug : Boolean
        If True, download onlt three files

    Returns
    -------
    None. Just download files in a category
    """

    category = category_url.split('/')[-2]
    # get soup
    soup = get_soup(category_url)
    # get links
    links = soup.select('a')
    # get file name if match url_page
    fnames = [parse_href(link) for link in links]
    fnames = [fname for fname in fnames if fname is not None]
    # form as url
    urls = [as_url(url_base, category, fname) for fname in fnames]

    if debug:
        urls = urls[:3]
    for fname, url in zip(fnames, urls):
        outpath = '{}/{}-{}'.format(directory, category, fname)
        download(url, outpath)
        print('downloaded {} to {}'.format(url, outpath))
        time.sleep(sleep)

def download_from_all_categories(directory, sleep=0.1, debug=False):
    """
    Arguments
    ---------
    directory : str
        Directory path to save downloaded files
    sleep : float
        Sleep time for downloading a file.
        Default is 0.1
    debug : Boolean
        If True, download onlt three files for each category
    """

    if not os.path.exists(directory):
        os.makedirs(directory)

    for _, category_url in category_links:
        download_from_a_category(category_url, directory, sleep, debug)
        print('done {}'.format(category_url), end='\n\n')