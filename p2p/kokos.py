#!/usr/bin/python

import urllib


class DataController(object):
    __domain = "www.kokos.pl"
    __url = "/webapi/get-auction-data"
    __key = "06d7bdc105ad98e8cf6f94eda5ec3a92"
    __id = "8488"
    __comments = 1
    __type = "JSON"

    def get_data(self):
        params = urllib.urlencode(
            {
                'key': self.__key,
                'id': self.__id,
                'comments': self.__comments,
                'type': self.__type
            }
        )

        request = urllib.urlopen("https://" + self.__domain + self.__url + "?" + params)
        data = request.read

        print(request.code, request.info())