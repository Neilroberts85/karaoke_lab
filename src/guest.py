class Guest:
    def __init__(self, insert_name, insert_wallet, insert_fav_song):
        self.name = insert_name
        self.wallet = insert_wallet
        self.fav_song = insert_fav_song
        
    def pay_entry_fee(self, input_amount):
        self.wallet -= input_amount

    
