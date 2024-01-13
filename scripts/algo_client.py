from algosdk.v2client import algod

class AlgoClient:
    def __init__(self, node_address, node_token):
        self.node_address = node_address
        self.node_token = node_token
        self.algod_client = algod.AlgodClient(self.node_token, self.node_address)

    def get_account_info(self, address):
        account_info = self.algod_client.account_info(address)
        return account_info

    def get_balance(self, address):
        account_info = self.get_account_info(address)
        return account_info.get('amount')

    def get_algod_client(self):
        return self.algod_client
