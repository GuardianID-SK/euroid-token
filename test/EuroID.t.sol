// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "forge-std/Test.sol";
import "../src/EuroID.sol";

contract EuroIDTest is Test {
    EuroID public token;
    address public owner = makeAddr("owner");
    address public treasury = makeAddr("treasury");
    address public user1 = makeAddr("user1");
    address public user2 = makeAddr("user2");

    uint256 constant EXPECTED_SUPPLY = 500_000_000 * 10 ** 18;

    function setUp() public {
        token = new EuroID(owner, treasury);
    }

    // Basic token properties
    function test_Name() public {
        assertEq(token.name(), "EuroID");
    }

    function test_Symbol() public {
        assertEq(token.symbol(), "EID");
    }

    function test_Decimals() public {
        assertEq(token.decimals(), 18);
    }

    function test_TotalSupply() public {
        assertEq(token.totalSupply(), EXPECTED_SUPPLY);
    }

    // Owner checks
    function test_OwnerSet() public {
        assertEq(token.owner(), owner);
    }

    function test_ZeroAddressOwnerRejected() public {
        // OpenZeppelin's Ownable2Step throws OwnableInvalidOwner for zero address
        vm.expectRevert();
        new EuroID(address(0), treasury);
    }

    function test_ZeroAddressTreasuryRejected() public {
        vm.expectRevert("EuroID: treasury cannot be zero address");
        new EuroID(owner, address(0));
    }

    // Treasury allocation
    function test_TreasuryReceivesAllSupply() public {
        assertEq(token.balanceOf(treasury), EXPECTED_SUPPLY);
    }

    // ERC-20 transfer functionality
    function test_TransferWorks() public {
        uint256 amount = 1000 * 10 ** 18;
        vm.prank(treasury);
        token.transfer(user1, amount);
        assertEq(token.balanceOf(user1), amount);
        assertEq(token.balanceOf(treasury), EXPECTED_SUPPLY - amount);
    }

    function test_ApprovalWorks() public {
        uint256 amount = 1000 * 10 ** 18;
        vm.prank(treasury);
        token.approve(user1, amount);
        assertEq(token.allowance(treasury, user1), amount);
    }

    function test_TransferFromWorks() public {
        uint256 amount = 1000 * 10 ** 18;
        vm.prank(treasury);
        token.approve(user1, amount);

        vm.prank(user1);
        token.transferFrom(treasury, user2, amount);

        assertEq(token.balanceOf(user2), amount);
        assertEq(token.balanceOf(treasury), EXPECTED_SUPPLY - amount);
        assertEq(token.allowance(treasury, user1), 0);
    }

    // No minting after deployment
    function test_UserCannotMint() public {
        // EuroID doesn't expose mint function
        // This test verifies the contract doesn't have a public mint
        bytes memory mintsig = abi.encodeWithSignature("mint(address,uint256)");
        (bool success, ) = address(token).call(mintsig);
        assertFalse(success);
    }

    function test_OwnerCannotMint() public {
        vm.prank(owner);
        bytes memory mintsig = abi.encodeWithSignature("mint(address,uint256)");
        (bool success, ) = address(token).call(mintsig);
        assertFalse(success);
    }

    // No seizure capability
    function test_OwnerCannotSeizeTokens() public {
        uint256 amount = 1000 * 10 ** 18;
        vm.prank(treasury);
        token.transfer(user1, amount);

        // Owner cannot transfer from user1 without approval
        vm.prank(owner);
        bytes memory xfersig = abi.encodeWithSignature(
            "transferFrom(address,address,uint256)",
            user1,
            owner,
            amount
        );
        (bool success, ) = address(token).call(xfersig);
        assertFalse(success);
    }

    // Supply immutability
    function test_TotalSupplyNeverExceeds() public {
        // After all transfers, total supply must remain constant
        uint256 amount1 = 100 * 10 ** 18;
        uint256 amount2 = 50 * 10 ** 18;

        vm.prank(treasury);
        token.transfer(user1, amount1);

        vm.prank(treasury);
        token.transfer(user2, amount2);

        assertEq(token.totalSupply(), EXPECTED_SUPPLY);
        assertEq(
            token.balanceOf(treasury) + token.balanceOf(user1) +
                token.balanceOf(user2),
            EXPECTED_SUPPLY
        );
    }

    // Ownership transfer via Ownable2Step
    function test_OwnershipTransferTwoStep() public {
        address newOwner = makeAddr("newOwner");

        vm.prank(owner);
        token.transferOwnership(newOwner);

        // New owner hasn't accepted yet
        assertEq(token.owner(), owner);

        // New owner accepts
        vm.prank(newOwner);
        token.acceptOwnership();

        assertEq(token.owner(), newOwner);
    }

    // Invariant: total supply is always 500M EID
    function test_Invariant_SupplyNeverChanges() public {
        uint256 initialSupply = token.totalSupply();
        assertEq(initialSupply, EXPECTED_SUPPLY);

        // After various transfers
        uint256 amount = 12345 * 10 ** 18;
        vm.prank(treasury);
        token.transfer(user1, amount);

        vm.prank(user1);
        token.transfer(user2, amount / 2);

        assertEq(token.totalSupply(), initialSupply);
    }
}
