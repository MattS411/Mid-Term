##  Part 1 – Socket Connection

Two Python scripts establish a TCP socket connection between client and server:
- `server.py`: Listens on localhost, accepts client connections, and responds to messages.
- `client.py`: Connects to the server, sends a message, and receives the response.

###  Features
- TCP connection using `socket` module
- Error handling for disconnection or inactive server
- Clear client-server message exchange
- Graceful shutdown

### 📸 Demonstrated Test Cases
- Server listening
- Client connects and sends message
- Server response received by client
- Error handling when server is not running
- Timestamps included in screenshots

---

##  Part 2 – Port Scanner

The `port_scanner.py` script scans a given host over a specified port range to identify open ports.

### Features
- Scans `localhost` and `scanme.nmap.org` (per ethical guidelines)
- User-defined port ranges
- Handles invalid inputs and unreachable hosts
- Timestamps recorded

### 📸 Demonstrated Test Cases
- Scanning ports 20–25 on 127.0.0.1
- Scanning scanme.nmap.org for common ports
- Handling invalid port ranges
- Host unreachable error handling


---

## 🛠️ Technologies Used
- Python 3.13+
- PowerShell & Command Prompt
- Manual testing via terminal

---

## 🔒 Ethical Scanning Guidelines Followed
- Scanned only `127.0.0.1` and `scanme.nmap.org`
- No aggressive scanning or DOS attempts
- Delays and ranges limited as per instructions

---

## 📸 Screenshots

All testing steps were documented with screenshots located in the `/screenshots/` directory, including:
- Server/Client interaction
- Scanner results
- Invalid input tests
- Timestamps for verification
