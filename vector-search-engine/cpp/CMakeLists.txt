cmake_minimum_required(VERSION 3.10)
project(vector_search)

find_package(pybind11 REQUIRED)

pybind11_add_module(vector_search vector_search.cpp)