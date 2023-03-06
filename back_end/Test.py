from flask import redirect, request, url_for
from flask import request
from JsonWrap import jsonwrap


def test():
    a = 1
    return jsonwrap(0, "login success.", 1)
