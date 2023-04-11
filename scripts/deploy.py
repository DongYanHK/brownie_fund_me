from brownie import FundMe, network, config, MockV3Aggregator
from scripts import helpful_scripts
from web3 import eth


def deploy_fund_me():
    account = helpful_scripts.get_account()
    # pass the price ETH/USD price feed to build FundMe contract
    # if we are on a persisent network like sepolia, using the associated address
    # otherwise, deploy mock
    if network.show_active() not in helpful_scripts.LOCAL_BLOCKCHAIN_ENVIRONMANTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        helpful_scripts.deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )

    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()
