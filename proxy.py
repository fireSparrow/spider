
from grab import Grab
from random import choice

def get_proxy():
    g = Grab()
    g.go('http://www.freeproxy-list.ru/api/proxy?anonymity=false&token=demo')
    res = g.doc.select('/html/body/p').text()
    res = res.split()
    return choice(res)