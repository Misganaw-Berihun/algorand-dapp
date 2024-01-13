import yaml

def get_keys(account_name):
    with open("../config.yml", "r") as acct_file:
        keys = yaml.safe_load(acct_file)

    account_keys = {
        "address": keys["accounts"][account_name]["address"],
        "mnemonic": keys["accounts"][account_name]["mnemonic"],
        "private_key": keys["accounts"][account_name]["private_key"]
    }

    return account_keys
    
tutor_keys = get_keys("tutor")
print("Tutor Keys:", tutor_keys)

trainee_1_keys = get_keys("trainee_1")
print("Trainee 1 Keys:", trainee_1_keys)

trainee_2_keys = get_keys("trainee_2")
print("Trainee 2 Keys:", trainee_2_keys)
