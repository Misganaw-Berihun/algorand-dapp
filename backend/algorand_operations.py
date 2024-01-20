import os,sys
from algosdk import transaction
rpath = os.path.abspath('..')
if rpath not in sys.path:
    sys.path.insert(0, rpath)

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
        unit_name="algos",
        asset_name="Certificate",
        manager=addr1,
        reserve=addr1,
        freeze=addr1,
        clawback=addr1,
        url=asset_url,
        total=1,
        decimals=0,
    )
    print("address1:", addr1)
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


def transfer_asset(acct1, acct2, created_asset):
    address1 = acct1["address"]
    pk1 = acct1["private_key"]
    address2 = acct2["address"]
    pk2 = acct2["private_key"]

    algod_client = AlgoClient("http://localhost:4001", "a" * 64).get_algod_client()
    sp = algod_client.suggested_params()

    xfer_txn = transaction.AssetTransferTxn(
        sender=address1,
        sp=sp,
        receiver=address2,
        amt=1,
        index=created_asset,
    )
    signed_xfer_txn = xfer_txn.sign(pk1)
    txid = algod_client.send_transaction(signed_xfer_txn)
    print(f"Sent transfer transaction with txid: {txid}")

    results = transaction.wait_for_confirmation(algod_client, txid, 4)
    print(f"Result confirmed in round: {results['confirmed-round']}")

def freeze_asset(acct1, acct2, created_asset):
    address1 = acct1["address"]
    pk1 = acct1["private_key"]
    address2 = acct2["address"]
    pk2 = acct2["private_key"]

    algod_client = AlgoClient("http://localhost:4001", "a" * 64).get_algod_client()
    sp = algod_client.suggested_params()
    freeze_txn = transaction.AssetFreezeTxn(
        sender=address1,
        sp=sp,
        index=created_asset,
        target=address2,
        new_freeze_state=True,
    )
    signed_freeze_txn = freeze_txn.sign(pk1)
    txid = algod_client.send_transaction(signed_freeze_txn)
    print(f"Sent freeze transaction with txid: {txid}")
    results = transaction.wait_for_confirmation(algod_client, txid, 4)
    print(f"Result confirmed in round: {results['confirmed-round']}")