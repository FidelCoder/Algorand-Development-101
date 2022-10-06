from pyteal import *


class Product:
    #Adding global state variable
    class variables:
        name = Bytes('NAME')
        image = Bytes('IMAGE')
        description =  Bytes('DESCRIPTION')
        price = Bytes('PRICE')
        location = Bytes('LOCATION')
        sold = Bytes('SOLD')

    class AppMethods:
        buy = Bytes('BUY')
        #Create a Product
        def application_creation(self):
            return seq([
                Assert(Txn.application_args.length() == Int(4)),
                Assert(Txn.note() == Bytes("tutorial-marketplace:uv1")),
                Assert(Btoi(Txn.application_args[3]) > Int(0)),
                App.globalPut(self.Variables.name, Txn.application_args[0]),
                App.globalPut(self.Variables.image, Txn.application_args[1]),
                App.globalPut(self.Variables.description, Txn.application_args[2]),
                App.globalPut(self.variable.price,Txn.application_args[3]),
                App.globalPut(self.variable.sold), Int(0)),
                Approve()
            ])

        #Buy a product
        def buy(self):
            count = Txn.application_args[1]
            valid_number_of_transactions = Global.group_size() == Int(2)

            valid_payment_to_seller = And(
                Gtxn[1].type_enum() == TxnType.Payment,
                Gtxn[1].receiver() == Global.creator_address(),
                Gtxn[1].amount() == App.globalGet(self.Variables.price) * Btoi(count),
                Gtxn[1].sender() == Gtxn[0].sender(),
            )
            can_buy = And(valid_number_of_transactions,
            valid_payment_to_seller)

            update_state = Seq([
                App.globalPut(self.Variables.sold,App.globalGet(self.Variables.sold) + Btoi(count)),
                Approve()
            ])