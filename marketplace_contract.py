from pyteal import *


class Product:
    class variables:
        name = Bytes('NAME')
        image = Bytes('IMAGE')
        description =  Bytes('DESCRIPTION')
        price = Bytes('PRICE')
        location = Bytes('LOCATION')
        sold = Bytes('SOLD')

    class AppMethods:
        buy = Bytes('BUY')