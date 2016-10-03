# -*- coding: utf-8 -*-

import unittest
from util import ApiTestCase


class FuncArgsTestCase(ApiTestCase):
    def get_call_params(self):
        return {
            'a_code': 'ru_company_price',
            'a_lang': 'ru',
        }

    def get_function_name(self):
        return 'func_args'

    def get_response_format(self):
        return [
            ('arg', unicode),
            ('type', unicode),
            ('def_is_null', bool),
        ]


class FuncResultTestCase(ApiTestCase):
    def get_call_params(self):
        return {
            'a_code': 'ru_company_price',
            'a_lang': 'ru',
        }

    def get_function_name(self):
        return 'func_result'

    def get_response_format(self):
        return [
            ('arg', unicode),
            ('type', unicode),
        ]


class IndexTestCase(ApiTestCase):
    def get_call_params(self):
        return {
            'a_lang': 'ru',
        }

    def get_function_name(self):
        return 'index'

    def get_response_format(self):
        return [
            ('code', unicode),
            ('nspname', unicode),
            ('proname', unicode),
            ('sample', unicode),
        ]


class RuAreaTestCase(ApiTestCase):
    def get_call_params(self):
        return {
            'a_path': '{}',
        }

    def get_function_name(self):
        return 'ru_area'

    def get_response_format(self):
        return [
            ('path', unicode),
            ('name', unicode),
        ]


class RuAreaPathTestCase(ApiTestCase):
    def get_call_params(self):
        return {
            'a_path': '',
        }

    def get_function_name(self):
        return 'ru_area_path'

    def get_response_format(self):
        return [
            ('path', unicode),
            ('name', unicode),
        ]


if __name__ == '__main__':
    unittest.main()
