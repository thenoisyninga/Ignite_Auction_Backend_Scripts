# Ignite_Auction_Backend_Scripts
Automated database tasks for the test rounds and main execution of FPS Ignite Auction.

The package contains modules that:
- Log out all delegations.
- Delete all Login History.
- Delete all previously placed bets.
- Log out a single delegation.
- Populate database with test user data.
- Populate databases with new delegation data (not serviced for consistent usage).
- Set all hasBid status' (int the database) to no.
- Add a new Backup User in case of problems.
- Get the number of delegations not logged in, and the delegation numbers of the ones not logged in.
- Run all the modules needed to prepare things for a new final or test round.
## Installation
- The only needed package other than the ones installed by default is mysql-connector-python.
- All files should be downloaded in a single directory.
- A file named 'password.txt' should be created, containing the database authentication password and kept in the same directory as the other python files.
## Usage
The Admin Controls scripts uses all these modules in one program to provide ease of use.
