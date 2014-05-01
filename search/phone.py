#!/usr/bin/python
import urllib.request
from bs4 import BeautifulSoup


class Search(object):
    __search_url = "http://paginasblancas.pe/telefono/"

    def get(self, phone_nr):
        response = urllib.request.urlopen(self.__search_url + phone_nr)
        soup = BeautifulSoup(response)
        data = soup.find('div', {'class': 'm-results--sort-wrapper m-results--sort-wrapper-simple'})

        if data:
            return data
        else:
            return False