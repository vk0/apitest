import unittest
import json
import requests


class SetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, type):
            return obj.__name__
        return json.JSONEncoder.default(self, obj)


class ApiTestCase(unittest.TestCase):
    API_URL_PATTERN = 'http://master.iac.it.tender.pro/rpc/{}'
    HEADERS = {
        'Content-type': 'application/json',
    }

    def get_call_params(self):
        raise NotImplementedError

    def get_function_name(self):
        raise NotImplementedError

    def get_response_format(self):
        raise NotImplementedError

    def __check_response_format(self, response_item):
        response_format = self.get_response_format()
        for param_key, param_type in response_format:
            if not (param_key in response_item and isinstance(response_item[param_key], param_type)):
                return False
        return True

    def test_run(self):
        try:
            response = requests.post(ApiTestCase.API_URL_PATTERN.format(self.get_function_name()),
                                     data=json.dumps(self.get_call_params()),
                                     headers=ApiTestCase.HEADERS).json()
        except NotImplementedError:
            return
        except ValueError:
            self.fail(u'Response is no valid JSON')

        invalid_response_pattern = u'\nInvalid response items: {}\n\nExpected item format: {}'
        invalid_response_items = filter(lambda _: not self.__check_response_format(_), response)
        self.assertEquals(len(invalid_response_items),
                          0,
                          msg=invalid_response_pattern.format(json.dumps(invalid_response_items,
                                                                         indent=True),
                                                              json.dumps(self.get_response_format(),
                                                                         indent=True,
                                                                         cls=SetEncoder)))
