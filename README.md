<table>
<tr>
<td width="340" valign="middle">

<img src="https://github.com/M3RICK/M3RICK/raw/main/jinx.webp" width="320" alt="Banner">

</td>
<td valign="middle">

# M3RICK

**Epitech Toulouse**
Cybersecurity • Digital Forensics • Reverse Engineering

<p>
  <img src="https://img.shields.io/badge/Focus-Security%20%26%20Systems-7c3aed?style=flat-square" alt="Focus">
  <img src="https://img.shields.io/badge/Location-Incheon%2C%20South Korea-7c3aed?style=flat-square" alt="Location">
  <img src="https://img.shields.io/badge/🇫🇷-0055A4?style=flat-square" alt="France">
</p>

<a href="https://github.com/M3RICK">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&duration=3000&pause=1000&color=7C3AED&vCenter=true&width=420&lines=Digital+Forensics+%28DFIR%29;Reverse+Engineering;Low-level+%26+Systems+%E2%80%94+Rust%2C+C%2C+C%2B%2B;Blue+Team" alt="Typing SVG">
</a>

</td>
</tr>
</table>

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:0055A4,50:ffffff,100:EF4135&height=4&width=880" alt="tricolore" />

---

## About

Student at Epitech Toulouse, focused on cybersecurity: **digital forensics (DFIR),
reverse engineering and low-level / systems programming**. I build security tooling
from scratch and practice on CTF and blue-team platforms. I came to reverse engineering through game integrity and
anti-cheat, which is still a side interest.

```yaml
Focus:             Digital Forensics (DFIR) · Reverse Engineering · Low-level / Systems
Currently Learning: Rust · Windows Internals · Binary Reverse Engineering
Exchange:          Inha University, Incheon, South Korea (2026-2027)
Languages:         French (Native) · English (C1 IELTS) · German (Fluent)
```

---

## Professional Experience

<table>
<tr>
<td>

### Neurofounders — Security & Technical Audit (Internship)
**Apr – Jul 2026 · 4 months**

- Conducted technical audits of a subscription media platform — product/UX, access control, privacy, and web performance
- Delivered 8 findings reports to the founder, each documenting the issue and a clear, actionable recommendation
- Translated technical risks into plain language for a non-technical decision-maker

<p>
  <img src="https://img.shields.io/badge/Security%20Audit-7c3aed?style=flat-square" alt="Security Audit">
  <img src="https://img.shields.io/badge/Technical%20Writing-0078D4?style=flat-square" alt="Technical Writing">
  <img src="https://img.shields.io/badge/Web%20Performance-FF6F00?style=flat-square" alt="Web Performance">
</p>

</td>
</tr>
<tr>
<td>

### Continental Automotive (now Aumovio), Embedded Software Intern
**Aug – Dec 2024 · Toulouse · R&D Passive Safety & Sensoring**

- Wrote the C proof of concept for a new sensor on a Renesas RL78/F13, from board bring-up to validated features
- Generated timed pulse patterns with hardware timers and prescalers; drove peripherals over SPI, I2C and UART
- Wrote toolchain setup and handover docs; the team then ran my code on the boards for their live lab tests

<p>
  <img src="https://img.shields.io/badge/C-00599C?style=flat-square&logo=c&logoColor=white" alt="C">
  <img src="https://img.shields.io/badge/Embedded-FF6F00?style=flat-square&logo=arm&logoColor=white" alt="Embedded">
  <img src="https://img.shields.io/badge/Microcontrollers-0078D4?style=flat-square" alt="MCU">
</p>

</td>
</tr>
</table>

---

## Cybersecurity & Research

<table>
<tr>
<td width="50%" valign="top">

**Security Research & Write-Ups**

DFIR investigations (HTB Sherlocks), a CVE analysis with Sigma and Suricata detection rules, and CTF machine write-ups.

<a href="https://github.com/M3RICK/WriteUps">
  <img src="https://img.shields.io/badge/View_Write--Ups-7c3aed?style=flat-square&logo=markdown&logoColor=white" alt="Write-ups">
</a>

</td>
<td width="50%" valign="top">

**Blue Team Labs Online**

Defensive security challenges and digital forensics investigations.

<a href="https://blueteamlabs.online/public/user/0bd62aebf339f4cb519d5b">
  <img src="https://img.shields.io/badge/View_Profile-0078D4?style=flat-square&logo=security&logoColor=white" alt="BTL Profile">
</a>

</td>
</tr>

<tr>
<td width="50%" valign="top">

**Cybersecurity Club @ Epitech**

Organized weekly CTF practice sessions (Root-Me, HackTheBox).

</td>
<td width="50%" valign="top">

**Bug Bounty & Conferences**

Took part in the WOCS'hACK 2025 bug bounty competition ([3 reports](https://github.com/M3RICK/WOCS_hACK2025)). Attended IoT pentesting workshops at Toulouse Hacking Convention (THC).

</td>
</tr>
</table>

---

## Featured Projects

### evtx_timeline
**Windows Event Log forensic tool — Rust**

DFIR tool that parses `.evtx` logs into a normalized, chronologically sorted timeline and flags suspicious activity: per-EventID rules (log cleared, service install, privilege-group changes...) and a stateful brute-force detection. Unit tested.

<p>
  <img src="https://img.shields.io/badge/Rust-000000?style=flat-square&logo=rust&logoColor=white" alt="Rust">
  <img src="https://img.shields.io/badge/DFIR-7c3aed?style=flat-square" alt="DFIR">
  <img src="https://img.shields.io/badge/Forensics-FF6F00?style=flat-square" alt="Forensics">
  &nbsp;
  <a href="https://github.com/M3RICK/evtx_timeline">
    <img src="https://img.shields.io/badge/View_Repository-181717?style=flat-square&logo=github&logoColor=white" alt="Repository">
  </a>
</p>

<img src="https://github.com/M3RICK/M3RICK/raw/main/assets/evtx_timeline_demo.png" width="620" alt="evtx_timeline sample output — account creation escalating to local Administrators">

<sub><i>Real output on a sample Security.evtx — a sequence of account-creation events escalating to the local Administrators group, flagged by severity.</i></sub>

**Other projects**

<table>
<tr>
<td width="33%" valign="top">

### GLaDOS
**Language & Compiler**

Compiler in Haskell: C-like syntax, type inference, bytecode compiler, custom VM, and a linker for multi-file compilation with relocatable object files.

<p>
  <img src="https://img.shields.io/badge/Haskell-5D4F85?style=flat-square&logo=haskell&logoColor=white" alt="Haskell">
  <img src="https://img.shields.io/badge/Compiler-7c3aed?style=flat-square" alt="Compiler">
</p>

<a href="https://github.com/M3RICK/GLaDOS">
  <img src="https://img.shields.io/badge/View_Repository-181717?style=for-the-badge&logo=github&logoColor=white" alt="Repository">
</a>

</td>
<td width="33%" valign="top">

### Samuride
**Multiplayer game — custom binary protocol (C++)**

Client-server game in C++/SFML with a custom binary TCP protocol (typed message headers, state sync). My entry point into networking and anti-cheat / game integrity.

<p>
  <img src="https://img.shields.io/badge/C++-00599C?style=flat-square&logo=cplusplus&logoColor=white" alt="C++">
  <img src="https://img.shields.io/badge/Binary_Protocol-7c3aed?style=flat-square" alt="Binary Protocol">
  <img src="https://img.shields.io/badge/Networking-FF6F00?style=flat-square" alt="Networking">
</p>

<a href="https://github.com/M3RICK/Samuride">
  <img src="https://img.shields.io/badge/View_Repository-181717?style=for-the-badge&logo=github&logoColor=white" alt="Repository">
</a>

</td>
<td width="33%" valign="top">

### Rift Rewind
**AWS x Riot Games Hackathon — prize winner**

League of Legends analysis platform with Riot API integration and AI-driven feedback.

🏆 *Roast Master 3000 Prize — AWS x Riot Games Hackathon 2025*

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazonaws&logoColor=white" alt="AWS">
</p>

<a href="https://github.com/M3RICK/Jinx-s_Magical_Rewind_Machine">
  <img src="https://img.shields.io/badge/View_Repository-181717?style=for-the-badge&logo=github&logoColor=white" alt="Repository">
</a>

</td>
</tr>
</table>

---

## Technical Stack

<details>
<summary><b>Click to expand</b></summary>
<br>

**Languages**

![C](https://img.shields.io/badge/C-00599C?style=flat-square&logo=c&logoColor=white)
![C++](https://img.shields.io/badge/C++-00599C?style=flat-square&logo=cplusplus&logoColor=white)
![Rust](https://img.shields.io/badge/Rust-000000?style=flat-square&logo=rust&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Haskell](https://img.shields.io/badge/Haskell-5D4F85?style=flat-square&logo=haskell&logoColor=white)
![Assembly](https://img.shields.io/badge/x86_Assembly-0078D4?style=flat-square)

**Security & Forensics**

![Wireshark](https://img.shields.io/badge/Wireshark-1679A7?style=flat-square&logo=wireshark&logoColor=white)
![Burp Suite](https://img.shields.io/badge/Burp_Suite-FF6633?style=flat-square)
![Exegol](https://img.shields.io/badge/Exegol-7c3aed?style=flat-square)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)

**Learning / Familiar**

![IDA](https://img.shields.io/badge/IDA_Pro-00599C?style=flat-square)
![Ghidra](https://img.shields.io/badge/Ghidra-FF0000?style=flat-square)
![Windows](https://img.shields.io/badge/Windows_Internals-0078D6?style=flat-square&logo=windows&logoColor=white)

</details>

---

## Connect

<p align="center">
  <a href="mailto:aymeric.lamanda@epitech.eu">
    <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email">
  </a>
  <a href="https://github.com/M3RICK">
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
  </a>
  <a href="https://blueteamlabs.online/public/user/0bd62aebf339f4cb519d5b">
    <img src="https://img.shields.io/badge/Blue_Team_Labs-0078D4?style=for-the-badge&logo=security&logoColor=white" alt="Blue Team Labs">
  </a>
</p>
