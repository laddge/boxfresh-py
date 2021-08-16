#!/usr/bin/env python3
import requests
import argparse


def main(slug, content):
    h = {'Content-Type': 'application/x-www-form-urlencoded'}
    d = {'slug': slug, 'content': content}
    r = requests.post('https://boxfresh.jp/apppage.php', headers=h, data=d)
    if r.status_code == 200:
        return {'slug': slug, 'content': content}
    else:
        print('Error')
        return


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('slug', help='target user id')
    parser.add_argument('content', help='content')
    args = parser.parse_args()
    print(main(args.slug, args.content))
