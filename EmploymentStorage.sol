// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract EmploymentStorage {
    struct Record {
        string name;
        string title;
        string startDate;
    }

    mapping(string => Record) public employees;

    function storeRecord(string memory id, string memory name, string memory title, string memory startDate) public {
        employees[id] = Record(name, title, startDate);
    }

    function getRecord(string memory id) public view returns (string memory, string memory, string memory) {
        Record memory rec = employees[id];
        return (rec.name, rec.title, rec.startDate);
    }
}
