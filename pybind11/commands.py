# -*- coding: utf-8 -*-
import os

DIR = os.path.abspath(os.path.dirname(__file__))


def get_include(user=False):
    return '/usr/include/pybind11'

def get_cmake_dir():
    return '/usr/share/cmake/pybind11'
