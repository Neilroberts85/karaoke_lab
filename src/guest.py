class Guest:
    def __init__(self, insert_name, insert_wallet):
        self.name = insert_name
        self.wallet = insert_wallet

    def pay_entry_fee(self, input_amount):
        self.wallet -= input_amount

    
