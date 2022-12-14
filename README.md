# SOS32: Solidity Optimize Storage

SOS32 is a tool to optimize solidity state variables packing in storage slots.

![Example](https://i.ibb.co/bWsnSW6/Screenshot-2022-10-10-at-19-17-59.png)

## Installation 

Create a virtual env and activate it
`python3 -m venv .venv`


Install in your virtual environment `pip install -r requirements.txt`

### GLPK Solver installation

To solve problems to optimality, SOS32 uses [GLPK](https://www.gnu.org/software/glpk/#TOCdownloading) solver.

You can install it via [conda](https://docs.conda.io/en/latest/miniconda.html)
Install GLPK `conda install glpk`



## Usage

### Generate Storage data

You'll need to generate the [solidity standard JSON interface](https://docs.soliditylang.org/en/v0.8.17/internals/layout_in_storage.html#json-output). 

You do it by using [Foundry](https://book.getfoundry.sh/getting-started/installation) and run `forge inspect <ContractName> storage` to generate storage data in the standard json output in `out/<contractFileName>.sol/<ContractName>.json`

### Optimize storage packing

Run `python3 __main__.py "out/<ContractFileName>.sol/<ContractName>.json"`

## Example

Run `forge inspect SOS32Example storage` to generate storage data in the standard json output in `out/SOS32Example.sol/SOS32Example.json`

Run `python3 __main__.py "out/SOS32Example.sol/SOS32Example.json"`