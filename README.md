# Workday Blockchain Prototype

This project is a prototype for verifying employee work history by integrating a mock Workday API with an Ethereum blockchain. It demonstrates how blockchain technology can enhance trust and transparency in HR verification processes.

## 🔧 Project Structure

| File | Description |
|------|-------------|
| `mock_workday.py` | Flask-based mock Workday API exposing employee data |
| `connector.py`    | Python script to fetch employee records and write to Ethereum smart contract |
| `EmploymentStorage.sol` | Solidity smart contract for storing and retrieving employee records |

---

## ⚙️ Requirements

- Python 3.x  
- Node.js & Ganache  
- MetaMask (for deploying via Remix)  
- Flask (`pip install flask`)  
- Web3.py (`pip install web3`)

---

## 🚀 How to Run

### 1. Start the Mock Workday API
```bash
python mock_workday.py
```

API available at: `http://localhost:5001/api/workday/employees`

### 2. Deploy the Smart Contract
- Open [Remix IDE](https://remix.ethereum.org)
- Paste `EmploymentStorage.sol`
- Deploy using `Injected Web3` and connect to Ganache
- Copy the deployed contract address and ABI

### 3. Run the Blockchain Connector
Edit `connector.py`:
- Paste your contract address and ABI
- Then run:
```bash
python connector.py
```

---

## 🧪 Example Output

```
Stored Alice Johnson on blockchain
Stored Bob Smith on blockchain
```

---

## 📄 License

MIT License

---

## ✍️ Author

Joao Coelho  
[NYU Tandon School of Engineering]
