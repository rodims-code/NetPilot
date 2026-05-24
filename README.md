# NetPilot

> AI-powered remote network management platform for technicians, MSPs, ISPs, cybercafés, hotels, schools, and enterprise networks.

NetPilot is a modern desktop + cloud platform built to simplify remote network operations across multiple locations.

The platform combines:

* Desktop networking tools
* Cloud synchronization
* Remote access
* Real-time monitoring
* LAN discovery
* Tunnel networking
* Device diagnostics
* AI-assisted operations

NetPilot is designed to work with AI coding assistants such as:

* GitHub Copilot
* OpenAI Codex
* Gemini
* Cursor AI
* Claude Code

The project architecture is intentionally modular and AI-friendly to accelerate development and scalability.

---

# Vision

The long-term vision of NetPilot is to become:

> The operating system for remote network technicians.

Instead of relying on:

* AnyDesk
* TeamViewer
* random Winbox sessions
* manual troubleshooting
* WhatsApp screenshots
* physical interventions

Technicians can manage entire infrastructures from one centralized dashboard.

NetPilot focuses specifically on:

* MikroTik ecosystems
* Wireless ISPs
* Small businesses
* Hotels
* Cybercafés
* Schools
* Multi-site infrastructures
* African networking environments

---

# Real-World Problem

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

# Real-World Problem

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

# Product Philosophy

NetPilot is NOT trying to replace:

* Winbox
* SSH
* WebFig
* Mikhmon

Instead, NetPilot acts as:

> a smart remote infrastructure hub.

The software simplifies:

* discovery
* access
* diagnostics
* monitoring
* multi-site management
* tunnel networking

while still allowing technicians to use their favorite tools.

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

# Global Architecture

```txt
┌──────────────────────────┐
│     Desktop Frontend     │
│  SvelteKit + Tauri UI    │
└────────────┬─────────────┘
             │
             │ invoke() / local API
             ↓
┌──────────────────────────┐
│    Golang Network Core   │
│ Scan / Discovery / LAN   │
└────────────┬─────────────┘
             │
             │ WebSocket / REST
             ↓
┌──────────────────────────┐
│     Django Cloud API     │
│ Auth / Devices / Sites   │
└────────────┬─────────────┘
             │
     ┌───────┴────────┐
     ↓                ↓
┌──────────┐   ┌────────────┐
│PostgreSQL│   │   Redis    │
└──────────┘   └────────────┘
             │
             ↓
┌──────────────────────────┐
│ Tunnel Infrastructure    │
│ Tailscale / ZeroTier     │
└────────────┬─────────────┘
             ↓
┌──────────────────────────┐
│ Remote Network Devices   │
│ MikroTik / AP / ONT etc  │
└──────────────────────────┘
```

---

# Frontend Pages Structure

## Authentication

* /login
* /register
* /forgot-password

---

## Dashboard

* /dashboard
* Global overview
* Active agents
* Device statistics
* Alerts
* Tunnel status

---

## Sites

* /sites
* /sites/[id]

Each site represents a physical client location.

Examples:

* Hotel Kinshasa
* Cyber Café Goma
* ISP Lubumbashi

---

## Devices

* /devices
* /devices/[id]

Device details include:

* IP address
* MAC address
* Vendor
* Open ports
* Monitoring metrics
* Logs
* Remote actions

---

## Monitoring

* /monitoring
* Real-time metrics
* Online/offline tracking
* Device latency

---

## Alerts

* /alerts
* Critical issues
* Device failures
* Connectivity issues

---

## Sessions

* /sessions
* Remote access history

---

## Settings

* /settings
* Tunnel settings
* User preferences
* Security configuration

---

# Backend Django Apps

```txt
backend/
│
├── users/
├── agents/
├── devices/
├── sites/
├── monitoring/
├── tunnels/
├── alerts/
├── billing/
├── sessions/
└── api/
```

---

# Go Network Engine Structure

```txt
go-engine/
│
├── scanner/
├── discovery/
├── monitoring/
├── websocket/
├── launcher/
├── tunnels/
└── utils/
```

---

# AI-Assisted Development Workflow

NetPilot is designed to be developed with AI-assisted programming.

Recommended workflow:

1. Define architecture manually
2. Generate boilerplate with AI
3. Validate networking/security manually
4. Iterate feature by feature
5. Use AI for repetitive tasks
6. Keep infrastructure logic human-reviewed

AI can accelerate:

* CRUD generation
* UI components
* API scaffolding
* Database models
* Type generation
* Dashboard layouts
* Documentation
* Testing boilerplate

Critical networking logic should always be reviewed manually.

---

# Desktop Application Architecture

```txt
SvelteKit UI
     ↓
Tauri Desktop Layer
     ↓
Golang Network Engine
     ↓
Remote LAN
```

---

# Backend Architecture

```txt
Django REST API
        ↓
Django Channels
        ↓
Redis
        ↓
PostgreSQL
        ↓
Celery Workers
```

---

# Communication Flow

```txt
User Action
    ↓
SvelteKit Frontend
    ↓
Tauri Commands
    ↓
Go Network Engine
    ↓
Django Cloud API
    ↓
Tunnel Infrastructure
    ↓
Remote Device
```

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

## Desktop Frontend

* SvelteKit
* TypeScript
* Tailwind CSS
* shadcn-svelte
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

The SvelteKit + Tauri desktop application communicates with the Go networking engine locally.

Architecture example:

```txt
SvelteKit UI
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

Created by RODIMS-CODE.