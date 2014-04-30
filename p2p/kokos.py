#!/usr/bin/python
import urllib.request
import urllib.parse
import json
import csv


class DataController(object):
    __domain = "www.kokos.pl"
    __url = "/webapi/get-auction-data"
    __key = "06d7bdc105ad98e8cf6f94eda5ec3a92"
    __comments = 1
    __type = "JSON"

    def get_data(self, trans_id):
        params = urllib.parse.urlencode(
            {
                'key': self.__key,
                'id': trans_id,
                'comments': self.__comments,
                'type': self.__type
            }
        )

        response = urllib.request.urlopen("https://" + self.__domain + self.__url + "?" + params)
        response_data = response.readall().decode('utf-8')

        try:
            data = json.loads(response_data)
        except ValueError:
            return False

        return data

    def build_id_range(self, from_nr, to_nr):
        nr_len = from_nr.__len__()
        from_nr = int(from_nr)
        to_nr = int(to_nr)
        id_list = []

        i = from_nr
        while i <= to_nr:
            missing_zero = nr_len - len(str(i))
            new_id = ""

            if missing_zero > 0:
                for j in range(0, missing_zero):
                    new_id += "0"

            new_id += str(i)
            id_list.append(new_id)

            i += 1

        return id_list

    def build_single_export_data(self, data):
        data = data['response']['auction']
        new_data = []
        data_head = []

        for dt, key in enumerate(data):
            new_data.append(data[key])
            data_head.append(key)

        return_data = {
            'header': data_head,
            'content': new_data
        }

        return return_data

    def sigle_csv_export(self, data, trans_id):
        with open('export/transactions/' + str(trans_id) + '.csv', 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            write_data = self.build_single_export_data(data)

            writer.writerow(write_data['header'])
            writer.writerow(write_data['content'])

    def gross_export(self, data):
        with open('export/transation_status.csv', 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            writer.writerow(['Status', '# of transactions'])

            for key, status in enumerate(data):
                writer.writerow([str(status), str(data[status])])

    def make_export(self, id_list):
        status_data = {}

        for trans_id in id_list:
            data = self.get_data(trans_id)

            if data:
                self.sigle_csv_export(data, trans_id)

                status = data['response']['auction']['status']

                if status in status_data:
                    status_data[status] += ',' + trans_id
                else:
                    status_data[status] = trans_id

        self.gross_export(status_data)