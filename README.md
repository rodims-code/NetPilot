# NetPilot

> Remote MikroTik Management Platform

NetPilot est une plateforme de gestion, supervision et accès distant dédiée aux infrastructures MikroTik.

L'objectif est de permettre à un technicien, un WISP, un cybercafé, un hôtel ou une entreprise de visualiser et administrer plusieurs routeurs MikroTik depuis une seule interface.

---

# Problem

Aujourd'hui, gérer plusieurs MikroTik distants est compliqué :

* Il faut demander l'adresse IP au client.
* Il faut souvent utiliser AnyDesk ou TeamViewer.
* Les clients envoient des captures d'écran WhatsApp.
* Il est difficile de savoir rapidement si un routeur est en ligne.
* Le diagnostic à distance prend du temps.

Exemple réel :

```txt
Client :
"Le WiFi ne fonctionne plus."

Technicien :
"Envoie-moi ton IP."

Client :
"Je ne sais pas."

Technicien :
"Installe AnyDesk."

Client :
"Je n'arrive pas."
```

NetPilot simplifie ce processus.

---

# Vision

Devenir la plateforme de référence pour la gestion des infrastructures MikroTik en Afrique et dans les marchés émergents.

---

# MVP Goals

Version 1 :

* Détection automatique des MikroTik
* Gestion multi-sites
* Monitoring basique
* Dashboard centralisé
* Association simple des agents
* Ouverture rapide Winbox / WebFig / SSH

---

# Target Users

## Techniciens réseau

* Freelances
* Consultants

## WISP

* Fournisseurs Internet locaux

## Cybercafés

## Hôtels

## Écoles

## PME

---

# Core Features

## Agent Installation

Le client installe :

```txt
NetPilot Agent
```

L'agent génère :

```txt
Agent ID
NP-XXXX-XXXX
```

---

## Agent Registration

Le technicien ajoute l'agent depuis son dashboard.

```txt
Ajouter Agent
↓
Entrer Agent ID
↓
Validation
```

---

## MikroTik Discovery

L'agent détecte automatiquement :

* hAP Lite
* hAP ac²
* RB750
* CCR
* CRS
* autres modèles MikroTik

---

## Device Information

Pour chaque MikroTik :

* Identity
* IP Address
* MAC Address
* RouterOS Version
* Uptime
* CPU Load
* Free Memory
* Board Name

---

## Monitoring

État :

* Online
* Offline

Mesures :

* Latence
* CPU
* RAM

---

## Remote Access

Accès rapide :

* Winbox
* WebFig
* SSH

---

# Architecture

```txt
SvelteKit
      ↓
Tauri
      ↓
Go Network Engine
      ↓
Django API
      ↓
PostgreSQL
```

---

# Technology Stack

## Desktop

* SvelteKit
* TypeScript
* Tailwind CSS
* shadcn-svelte
* Tauri

## Network Engine

* Golang

## Backend

* Django
* Django REST Framework
* Django Channels
* Celery

## Database

* PostgreSQL

## Cache

* Redis

---

# Project Structure

```txt
netpilot/

├── desktop/
│   ├── src/
│   ├── routes/
│   ├── components/
│   └── tauri/
│
├── go-agent/
│   ├── scanner/
│   ├── mikrotik/
│   ├── monitoring/
│   ├── websocket/
│   └── launcher/
│
├── backend/
│   ├── users/
│   ├── sites/
│   ├── agents/
│   ├── mikrotik/
│   ├── monitoring/
│   ├── alerts/
│   └── api/
│
└── docs/
```

---

# Development Roadmap

## V1

* Auth
* Agent registration
* MikroTik discovery
* Dashboard
* Online/Offline status

## V2

* RouterOS information
* Monitoring
* Alerts

## V3

* Remote Winbox launch
* SSH access
* WebFig access

## V4

* Configuration backup
* Scheduled monitoring

## V5

* Multi-vendor support
* TP-Link
* Ubiquiti
* LB-LINK

---

# Business Model

## Free

* 1 site
* 3 MikroTik
* Monitoring basique

## Pro

* Sites illimités
* Monitoring avancé
* Alertes
* Historique

## Enterprise

* Multi-techniciens
* Organisation
* Audit logs
* API


---

# Project Vision

NetPilot aims to become a modern remote network management platform optimized for African technicians, ISPs, cybercafés, hotels, and enterprise networks.

The goal is to simplify remote network operations and reduce dependence on traditional remote desktop software.

---

# Author

Created by RODIMS-CODE.