from brownie import Nudam, network, config, accounts


def get_account():
    return accounts.add(config["wallets"]["from_key"])


def deploy_Nudam():
    account = get_account()
    nudam = Nudam.deploy(
        {"from": account, "gas_price": "5 gwei"},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract address: {nudam.address}")
    return nudam


def main():
    deploy_Nudam()
    contract = deploy_Nudam[-1]
    print(contract.balanceOf(get_account()))
