# NetPilot

> Intelligent remote network management platform for MikroTik, repeaters, routers, access points, and network equipment.

## Overview

NetPilot is a desktop + cloud platform designed for network technicians, MSPs, installers, cybercafés, hotels, schools, and small ISPs.

The platform allows technicians to:

* Detect network devices automatically
* Access remote networks securely
* Open Winbox / WebFig / SSH remotely
* Monitor equipment status
* Track IP changes
* Diagnose network issues
* Centralize multiple sites

Unlike general remote desktop software, NetPilot focuses specifically on network infrastructure management.

---

# Main Problem

Technicians often face problems such as:

* Lost router IP addresses
* Inaccessible repeater interfaces
* Devices behind NAT
* Remote troubleshooting difficulties
* Need for AnyDesk/TeamViewer sessions
* Unstable access after configuration changes
* Difficulty managing multiple sites

NetPilot solves these issues by creating a centralized remote network management system.

---

# MVP Goals

The first MVP focuses on:

* Remote network access
* Automatic LAN scanning
* Device discovery
* Secure tunnel connection
* Remote Winbox/Web access
* Basic monitoring dashboard

---

# Target Devices

Supported network equipment:

* MikroTik
* TP-Link
* LB-LINK
* Ubiquiti
* Huawei
* ONT devices
* IP Cameras
* Switches
* WiFi Repeaters

---

# Architecture

```txt
Desktop App (React + Tauri)
        ↓
Django API + WebSocket
        ↓
Agent Service
        ↓
Tailscale / ZeroTier Tunnel
        ↓
Remote LAN
        ↓
Network Equipment
```

---

# Tech Stack

## Frontend Desktop

* React
* TypeScript
* Tailwind CSS
* shadcn/ui
* Tauri

## Backend

* Django
* Django REST Framework
* Django Channels
* PostgreSQL
* Redis
* Celery

## Networking

* Golang (network engine)
* Tailscale
* ZeroTier
* WebSocket
* TCP/IP
* ARP Scan
* Ping Discovery

---

# Golang Network Engine

NetPilot uses Golang for all low-level networking operations.

The Go engine is responsible for:

* LAN scanning
* ARP discovery
* Ping sweep
* Open ports detection
* Network diagnostics
* Tunnel communication
* Device monitoring
* Reconnection handling
* Multi-threaded network operations
* System-level networking tasks

Why Golang:

* Excellent network performance
* Lightweight binaries
* Cross-platform compilation
* High concurrency support
* Efficient socket management
* Stable desktop integration

The React + Tauri desktop application communicates with the Go networking engine locally.

Architecture example:

```txt
React UI
   ↓
Tauri Desktop Layer
   ↓
Golang Network Engine
   ↓
Remote Network Devices
```

---

# Desktop Application

The NetPilot desktop app is built with Tauri.

The application will provide:

* LAN scanning
* Device discovery
* Real-time monitoring
* Remote access dashboard
* Tunnel management
* Winbox launcher
* SSH launcher
* Web interface launcher

Cross-platform support:

* Windows (.exe / .msi)
* macOS (.dmg)
* Linux

---

# Core Features

## 1. Device Discovery

Automatically detect:

* IP address
* MAC address
* Vendor
* Device status
* Open ports

---

## 2. Remote Access

Securely access remote equipment through encrypted tunnels.

Supported access:

* Winbox
* WebFig
* SSH
* HTTPS
* Telnet

---

## 3. Monitoring

Monitor:

* Online/offline status
* IP changes
* Device availability
* Ping latency
* CPU usage
* Temperature

---

## 4. Multi-Site Management

Manage multiple client locations from one dashboard.

Example:

```txt
- Hotel Kinshasa
- Cyber Café Goma
- ISP Lubumbashi
- School Brazzaville
```

---

## 5. Smart Diagnostics

Automatic diagnostics for:

* Unreachable devices
* HTTP failures
* Gateway conflicts
* DHCP issues
* Network instability

---

# Future Features

## Planned Features

* Automated backups
* Config restore
* Push configurations
* MikroTik scripts deployment
* Notifications & alerts
* Team collaboration
* Mobile companion app
* Cloud hotspot management
* Mikhmon integration

---

# Workflow Example

## Client Side

1. Install NetPilot Agent
2. Login to account
3. Agent scans LAN automatically
4. Devices are synchronized to the cloud

---

## Technician Side

1. Open NetPilot dashboard
2. Select remote site
3. View detected equipment
4. Click "Connect"
5. Open Winbox/WebFig remotely

---

# Security

Security priorities:

* Encrypted communication
* Secure authentication
* VPN tunnel isolation
* Access permissions
* Device authorization
* Activity logging

---

# Business Model

## Free Plan

* Limited devices
* Basic monitoring
* Single user

## Pro Plan

* Unlimited devices
* Advanced monitoring
* Multi-site management
* Backups
* Alerts
* Team collaboration

---

# Development Roadmap

## Phase 1 — MVP

* Authentication
* Device discovery
* Dashboard
* Tunnel connection
* Remote access

## Phase 2 — Monitoring

* Real-time metrics
* Alerts
* Logging
* Diagnostics

## Phase 3 — Automation

* Backup system
* Script deployment
* Multi-client support
* Advanced analytics

---

# Project Vision

NetPilot aims to become a modern remote network management platform optimized for African technicians, ISPs, cybercafés, hotels, and enterprise networks.

The goal is to simplify remote network operations and reduce dependence on traditional remote desktop software.

---

# Author

Created by Rodims-Code.
