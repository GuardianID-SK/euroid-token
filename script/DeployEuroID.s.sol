// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "forge-std/Script.sol";
import "../src/EuroID.sol";

/**
 * @dev Deployment script for EuroID on Tron MainNet
 *
 * Usage:
 *
 * For Tron MainNet:
 * forge script script/DeployEuroID.s.sol:DeployEuroID \
 *   --rpc-url https://rpc.trongrid.io \
 *   --private-key <YOUR_PRIVATE_KEY> \
 *   --broadcast
 *
 * For testing locally (Anvil):
 * anvil --fork-url https://rpc.trongrid.io
 * forge script script/DeployEuroID.s.sol:DeployEuroID --broadcast --rpc-url http://localhost:8545
 *
 */
contract DeployEuroID is Script {
    function run() external {
        // Read from environment or use defaults for testing
        address guardianOwner = vm.envOr(
            "GUARDIAN_OWNER",
            // Test address: TBgF1uJktsUYBy3ffMvDkxPzJhCJ6ySgiE
            // For actual deployment, export GUARDIAN_OWNER=0x...
            address(0x1b1053887700691Fc6AF89fFc5Cab725BF6a00d9)
        );

        address treasuryAddress = vm.envOr(
            "GUARDIAN_TREASURY",
            // Same as owner for this deployment
            address(0x1b1053887700691Fc6AF89fFc5Cab725BF6a00d9)
        );

        require(
            guardianOwner != address(0),
            "GUARDIAN_OWNER not set or is zero address"
        );
        require(
            treasuryAddress != address(0),
            "GUARDIAN_TREASURY not set or is zero address"
        );

        vm.startBroadcast();

        EuroID token = new EuroID(guardianOwner, treasuryAddress);

        vm.stopBroadcast();

        // Print deployment info
        console.log("=== EuroID Deployment ===");
        console.log("Token Address:", address(token));
        console.log("Owner:", token.owner());
        console.log("Treasury:", token.treasury());
        console.log("Total Supply:", token.totalSupply());
        console.log("Treasury Balance:", token.balanceOf(treasuryAddress));
        console.log("");
        console.log("Add this contract to MetaMask:");
        console.log("Contract Address:", address(token));
        console.log("Network: Tron MainNet");
        console.log("Symbol: EID");
    }
}
