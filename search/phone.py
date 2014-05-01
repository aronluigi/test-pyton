#!/usr/bin/python
import urllib.request
import json
from bs4 import BeautifulSoup


class Search(object):
    __search_url = "http://paginasblancas.pe/telefono/"

    def get(self, phone_nr):
        response = urllib.request.urlopen(self.__search_url + phone_nr).readall().decode('utf-8')
        soup = BeautifulSoup(response)
        data = soup.find('section', {'class': 'span-15 append-1 m-results--container'})

        if data:
            return self.extract_data(data)
        else:
            return False

    def extract_data(self, soup):
        container_data = soup.find('ul', {'class': 'l-plain m-results-businesses'})
        container_data = container_data.find('li', {'class': 'm-results-business m-results-subscriber'})

        data = {
            'name': None,
            'address': {
                'street': None,
                'locality': None
            },
        }

        name = container_data.find('h3', {'class': 'm-results-business--name'})
        name = name.find('a', {'class': 'no-link'}).string.strip()

        address = container_data.find('p', {'class': 'm-results-business--address'})
        street = address.find('span', {'itemprop': 'streetAddress'}).string.strip()
        locality = address.find('span', {'itemprop': 'addressLocality'}).string.strip()

        data['name'] = str(name)
        data['address']['street'] = street
        data['address']['locality'] = locality

        return json.dumps(data)