// contracts/OurToken.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract Nudam is ERC20 {
    constructor() ERC20("Nudam", "NDM") {
        _mint(msg.sender, 1000);
    }
}