# ⚔️ Ticket Dossier

A unified ticket intelligence dashboard for IT technicians at Bradley Arant Boult Cummings LLP.

**Live Demo:** https://aikrehn-beep.github.io/ticket-dossier/tablet.html

## What It Is

When a technician gets assigned a ServiceNow ticket, they currently hunt across 4+ systems just to understand what's happening. Ticket Dossier pulls everything into one view:

- 👤 **Customer Profile** — Name, office, phone, device (from SharePoint Directory)
- 📝 **Ticket Details** — Priority, SLA countdown, category
- 🔍 **Similar Tickets** — Recent related issues with resolutions
- 📚 **KB Articles** — Relevant knowledge base articles ranked by match %
- 🌐 **Google Fallback** — When KB articles don't cover it, search Google for fixes
- ✅ **Guided Fix Steps** — Checklist pulled from past successful resolutions
- 📋 **Customer History** — Timeline of the user's past tickets

## Files

| File | Purpose |
|------|---------|
| `tablet.html` | **Main app** — touch-optimized tablet interface |
| `pitch.html` | **Presentation** — 8-slide pitch deck for management |
| `index.html` | Desktop view (older version) |
| `teams-package/` | Microsoft Teams app manifest + icons |

## Teams App (Sideload)

1. Open Teams desktop app
2. Click **Apps** in left sidebar
3. Bottom-left → **Manage your apps** → **Upload a custom app**
4. Select `teams-package/ticket-dossier-teams.zip`
5. "Ticket Dossier" appears in your sidebar

> ⚠️ **Note:** Your Teams tenant may have sideloading disabled. Ask your manager to enable "Allow sideloading of custom apps" for testing, or submit through Teams Admin Center for approval.

## Architecture

| Data Source | What It Provides |
|-------------|-----------------|
| **ServiceNow** (REST API) | Tickets, problems, change requests, KB articles |
| **SharePoint** (API) | Employee directory (office #, phone), asset tracking (devices) |

## Roadmap

| Phase | Timeline | Deliverables |
|-------|----------|-------------|
| 1. Proof of Concept | 2-3 weeks | Working mockup, API access requests |
| 2. MVP | 4-6 weeks | Live ServiceNow + SharePoint integration |
| 3. Scale | 8-10 weeks | Firm-wide rollout, Teams integration, tablet optimization |

## Built By

Joshua Alldredge — IT Technician, Bradley Arant Boult Cummings LLP

---

*Mockup built with HTML/CSS/JS. Production version planned as PWA + Teams app.*
