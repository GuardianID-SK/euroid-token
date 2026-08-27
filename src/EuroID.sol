// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable2Step.sol";

/**
 * @title EuroID
 * @dev ERC-20 token for GUARDIAN ID with fixed supply of 500,000,000 EID.
 * No minting after deployment. No transfer taxes. No rebasing.
 * Transparent ownership via Ownable2Step.
 */
contract EuroID is ERC20, Ownable2Step {
    // Fixed supply: 500,000,000 EID with 18 decimals
    uint256 public constant TOTAL_SUPPLY = 500_000_000 * 10 ** 18;

    // Treasury address receives initial allocation
    address public treasury;

    // Event emitted on deployment
    event EuroIDDeployed(
        address indexed owner,
        address indexed treasury,
        uint256 totalSupply
    );

    /**
     * @dev Deploy EuroID with fixed supply.
     * @param guardianOwner The owner address (GUARDIAN ID multisig, eventually)
     * @param treasuryAddress The treasury address receiving all EID
     */
    constructor(
        address guardianOwner,
        address treasuryAddress
    ) ERC20("EuroID", "EID") Ownable(guardianOwner) {
        require(
            guardianOwner != address(0),
            "EuroID: owner cannot be zero address"
        );
        require(
            treasuryAddress != address(0),
            "EuroID: treasury cannot be zero address"
        );

        treasury = treasuryAddress;

        // Mint all supply to treasury in a single operation
        _mint(treasuryAddress, TOTAL_SUPPLY);

        emit EuroIDDeployed(guardianOwner, treasuryAddress, TOTAL_SUPPLY);
    }

    /**
     * @dev Verify that there is no path to mint additional tokens.
     * This contract does not expose any mint(), burn(), or rebasing functions.
     * Only the constructor creates tokens exactly once.
     */
    function decimals() public override pure returns (uint8) {
        return 18;
    }

    /**
     * @dev Standard ERC-20 functions are inherited and work unchanged.
     * Transfer, approve, transferFrom all function normally.
     * No transfer taxes. No blacklisting. No hidden restrictions.
     */
}
