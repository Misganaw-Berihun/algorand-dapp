from algosdk import transaction
from scripts.algo_client import AlgoClient

def create_asset(addr1, asset_url):
    algo_client = AlgoClient("http://localhost:4001", "a" * 64).get_algod_client()

    sp = algo_client.suggested_params()
    txn = transaction.AssetConfigTxn(
        sender=addr1,
        sp=sp,
        default_frozen=False,
        unit_name="Certificate",
        asset_name="Certificate",
        manager=addr1,
        reserve=addr1,
        freeze=addr1,
        clawback=addr1,
        url=asset_url,
        total=1,
        decimals=0,
    )
    stxn = txn.sign(pk1)
    
    # Send the transaction to the network and retrieve the txid.
    txid = algo_client.send_transaction(stxn)
    print(f"Sent asset create transaction with txid: {txid}")
    
    # Wait for the transaction to be confirmed
    results = transaction.wait_for_confirmation(algo_client, txid, 4)
    print(f"Result confirmed in round: {results['confirmed-round']}")

    # grab the asset id for the asset we just created
    created_asset = results["asset-index"]
    return created_asset
