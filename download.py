import argparse
import os
from crs_downloader import download_from_all_categories

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--directory', type=str, default='./output', help='Output directory')
    parser.add_argument('--sleep', type=float, default=10, help='Sleep time for each submission (post)')
    parser.add_argument('--debug', dest='debug', action='store_true')

    args = parser.parse_args()
    directory = args.directory
    sleep = args.sleep
    debug = args.debug

    # check output directory
    if not os.path.exists(directory):
        os.makedirs(directory)

    download_from_all_categories(output, sleep, debug)

if __name__ == '__main__':
    main()