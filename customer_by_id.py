#!/usr/bin/env python

import argparse

import requests

ID = 'id'


def main():
    # Parse cli args
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--id', required=True, dest=ID, help='Customer ID')
    args = vars(parser.parse_args())

    resp = requests.get('http://localhost:8080/customers/{}'.format(args[ID]))

    print('URL: {}\n'.format(resp.url))

    data = resp.json()
    cust = data['customer']

    print('Customer:')
    for k, v in cust.items():
        print('{}: {}'.format(k, v))
    print('')


if __name__ == "__main__":
    main()
