<table>
<tr>
<td width="340" valign="middle">

<img src="https://github.com/M3RICK/M3RICK/raw/main/jinx.webp" width="320" alt="Banner">

</td>
<td valign="middle">

# M3RICK

<img src="assets/hexdump.svg?v=7" width="420" alt="Built: evtx_timeline, EVTX forensics in Rust. Now: fuzzing a C filesystem parser. Learning: DFIR investigations, HTB Sherlocks. Open to: part-time security role, Sept 2027.">

</td>
</tr>
</table>

<img src="assets/tricolore.svg" width="880" alt="tricolore" />

---

## Open Source Contributions

**exfatprogs** (Linux exFAT filesystem utilities): found an undefined-behaviour shift on crafted boot sectors by fuzzing the parser with libFuzzer and UBSan. Fixed it in the shared library used by five of the tools; the patch was reviewed by the maintainer, merged upstream and shipped in [exfatprogs 1.4.5](https://github.com/exfatprogs/exfatprogs/releases/tag/1.4.5) ([commit f976d4d](https://github.com/exfatprogs/exfatprogs/commit/f976d4d0b033e72518fb67f1d805fd49f2aebd95), [PR #403](https://github.com/exfatprogs/exfatprogs/pull/403)).

<a href="https://github.com/exfatprogs/exfatprogs/commit/f976d4d0b033e72518fb67f1d805fd49f2aebd95">
  <img src="https://img.shields.io/badge/Merged_upstream-exfatprogs_1.4.5-E0267A?style=for-the-badge&logo=linux&logoColor=white" alt="Merged upstream in exfatprogs 1.4.5">
</a>

How it was found: [fuzzing harnesses](https://github.com/M3RICK/exfatprogs-fuzzer) · [write-up (PDF)](https://github.com/M3RICK/WriteUps/blob/main/VulnResearch/exfatprogs/exfatprogs-WriteUp.pdf)

---

## Professional Experience

<table>
<tr>
<td>

### Neurofounders - Security & Technical Audit (Internship)
**Apr - Jul 2026 · 4 months**

- Conducted technical audits of a subscription media platform - product/UX, access control, privacy, and web performance
- Delivered 8 findings reports to the founder, each documenting the issue and a clear, actionable recommendation
- Translated technical risks into plain language for a non-technical decision-maker

<p>
  <img src="https://img.shields.io/badge/Security%20Audit-30363D?style=flat-square" alt="Security Audit">
  <img src="https://img.shields.io/badge/Technical%20Writing-30363D?style=flat-square" alt="Technical Writing">
  <img src="https://img.shields.io/badge/Web%20Performance-30363D?style=flat-square" alt="Web Performance">
</p>

</td>
</tr>
<tr>
<td>

### Continental Automotive (now Aumovio), Embedded Software Intern
**Aug - Dec 2024 · Toulouse · R&D Passive Safety & Sensoring**

- Wrote the C proof of concept for a new sensor on a Renesas RL78/F13, from board bring-up to validated features
- Generated timed pulse patterns with hardware timers and prescalers; drove peripherals over SPI, I2C and UART
- Wrote toolchain setup and handover docs; the team then ran my code on the boards for their live lab tests

<p>
  <img src="https://img.shields.io/badge/C-30363D?style=flat-square&logo=c&logoColor=white" alt="C">
  <img src="https://img.shields.io/badge/Embedded-30363D?style=flat-square&logo=arm&logoColor=white" alt="Embedded">
  <img src="https://img.shields.io/badge/Microcontrollers-30363D?style=flat-square" alt="MCU">
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
  <img src="https://img.shields.io/badge/View_Write--Ups-30363D?style=flat-square&logo=markdown&logoColor=white" alt="Write-ups">
</a>

</td>
<td width="50%" valign="top">

**Blue Team Labs Online**

Defensive security challenges and digital forensics investigations.

<a href="https://blueteamlabs.online/public/user/0bd62aebf339f4cb519d5b">
  <img src="https://img.shields.io/badge/View_Profile-30363D?style=flat-square&logo=security&logoColor=white" alt="BTL Profile">
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
**Windows Event Log forensic tool - Rust**

DFIR tool that parses `.evtx` logs into a normalized, chronologically sorted timeline and flags suspicious activity: per-EventID rules (log cleared, service install, privilege-group changes...) and a stateful brute-force detection. Unit tested.

<p>
  <a href="https://github.com/M3RICK/evtx_timeline">
    <img src="https://img.shields.io/badge/View_Repository-E0267A?style=for-the-badge&logo=github&logoColor=white" alt="Repository">
  </a>
</p>

<img src="https://github.com/M3RICK/M3RICK/raw/main/assets/evtx_timeline_demo.png" width="620" alt="evtx_timeline sample output - account creation escalating to local Administrators">

<sub><i>Real output on a sample Security.evtx - a sequence of account-creation events escalating to the local Administrators group, flagged by severity.</i></sub>

**Other projects**

- [GLaDOS](https://github.com/M3RICK/GLaDOS): compiler in Haskell, with type inference, a bytecode VM and a linker for relocatable object files
- [Samuride](https://github.com/M3RICK/Samuride): C++/SFML multiplayer game with a custom binary TCP protocol
- [Rift Rewind](https://github.com/M3RICK/Jinx-s_Magical_Rewind_Machine): AWS x Riot Games Hackathon 2025, [Roast Master 3000 Prize](https://devpost.com/software/jinx-s-workshop)

---

## Technical Stack

| | |
|:--|:--|
| **Languages** | C · C++ · Rust · Python · Haskell · x86 Assembly |
| **Forensics & Detection** | Windows Event Logs (EVTX) · Sysmon · Linux auth logs · Sigma · Suricata · MITRE ATT&CK |
| **Fuzzing & Debugging** | libFuzzer · AddressSanitizer · UBSan · Clang |
| **Network & Web** | Wireshark · Nmap · Burp Suite · Hydra · Chisel |
| **Embedded** | Renesas RL78 · SPI · I2C · UART |
| **Environment** | Linux · Exegol · Docker · Git · jq · Typst |
| **Learning** | Ghidra |

---

## Background

```yaml
Nationality: French
Exchange:    Inha University, South Korea (2026-2027): Computer Networks, Operating Systems, IoT
Languages:   French (Native) · English (C1 IELTS) · German (Fluent) · Korean (Beginner)
```

---

## Connect

<p align="center">
  <a href="mailto:aymeric.lamanda@epitech.eu">
    <img src="https://img.shields.io/badge/Email-57606A?style=for-the-badge&logo=gmail&logoColor=white" alt="Email">
  </a>
  <a href="https://www.linkedin.com/in/aymeric-l-667657311/">
    <img src="https://img.shields.io/badge/LinkedIn-57606A?style=for-the-badge" alt="LinkedIn">
  </a>
  <a href="https://github.com/M3RICK">
    <img src="https://img.shields.io/badge/GitHub-57606A?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
  </a>
  <a href="https://blueteamlabs.online/public/user/0bd62aebf339f4cb519d5b">
    <img src="https://img.shields.io/badge/Blue_Team_Labs-30363D?style=for-the-badge&logo=security&logoColor=white" alt="Blue Team Labs">
  </a>
</p>
