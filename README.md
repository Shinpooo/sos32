# SOS32: Solidity Optimize Storage

SOS32 is a tool to optimize solidity state variables packing in storage slots.

## Install 
`pip install -r requirements.txt`

## Usage

### Generate Storage data

You'll need to generate the [solidity standard JSON interface](https://docs.soliditylang.org/en/v0.8.17/internals/layout_in_storage.html#json-output). 

You do it by using [Foundry](https://book.getfoundry.sh/getting-started/installation) and run `forge inspect <ContractName> storage` to generate storage data in the standard json output in `out/<contractFileName>.sol/<ContractName>.json`

### Optimize storage packing

Run `python3 __main__.py "out/<ContractFileName>.sol/<ContractName>.json"`

## Example

Run `forge inspect SOS32Example storage` to generate storage data in the standard json output in `out/SOS32Example.sol/SOS32Example.json`

Run `python3 __main__.py "out/SOS32Example.sol/SOS32Example.json"`