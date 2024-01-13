from algosdk import transaction
from scripts.algo_client import AlgoClient

def create_asset(acct1, asset_url):
    addr1 = acct1["address"]
    pk1 = acct1["private_key"]
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
    
    txid = algo_client.send_transaction(stxn)
    print(f"Sent asset create transaction with txid: {txid}")
    
    results = transaction.wait_for_confirmation(algo_client, txid, 4)
    print(f"Result confirmed in round: {results['confirmed-round']}")

    created_asset = results["asset-index"]
    return created_asset


def opt_in_asset(trainee_email, asset_id, acct2):
    addr2 = acct2["address"]
    pk2 = acct2["private_key"]
    algo_client = AlgoClient("http://localhost:4001", "a" * 64).get_algod_client()

    sp = algo_client.suggested_params()
    optin_txn = transaction.AssetOptInTxn(
        sender=addr2, sp=sp, index=asset_id
    )

    signed_optin_txn = optin_txn.sign(pk2)
    txid = algo_client.send_transaction(signed_optin_txn)
    print(f"Sent opt-in transaction with txid: {txid}")

    results = transaction.wait_for_confirmation(algo_client, txid, 4)
    print(f"Result confirmed in round: {results['confirmed-round']}")

