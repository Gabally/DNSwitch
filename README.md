# DNSwitch

Extremely simple DNS rebinding server

## Installation
`
pip install .
`

## Usage

- Point the name servers of a domain to the public IP of the server hosting DNSwitch

- Start the server using the following command:

`
DNSWitch --domain <domain> --ip <server public ip>
`

- Visit `http://<domain>:<port>/gen` to generate a payload