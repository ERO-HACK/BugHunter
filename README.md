# 🐞 BugHunter - Advanced Bug Hunting Tool

**BugHunter** is a powerful and modular CLI-based bug hunting tool designed for discovering common web vulnerabilities like **XSS**, **SQL Injection**, **Local File Inclusion (LFI)**, and **Open Redirect**.  
It is ideal for **bug bounty hunters**, **penetration testers**, and **security researchers**.

---

## 🚀 Features

- 🔍 Scan for XSS, LFI, SQLi, and Redirect vulnerabilities
- 🧪 Payload injection system (customizable via `.txt` files)
- 🎨 Colorful CLI output for better readability
- 🧰 Easy-to-use Command Line Interface
- 🧠 Intelligent detection patterns
- 📁 Support for file-based payloads
- 🕓 Execution delay/timing control
- 📦 Modular architecture (each vulnerability has its own module)

---

## 🛠️ Installation

```bash
git clone https://github.com/yourusername/BugHunter.git
cd BugHunter
pip install -r requirements.txt
python bughunter.py -h
