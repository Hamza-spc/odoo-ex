# odoo-ex — Odoo 17 Learning Project

Local Odoo 17 dev environment for learning ERP/CRM (PFE prep).

## Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)

## Quick start

```bash
docker compose up -d
```

Open **http://localhost:8069**

| Field | Value |
|-------|-------|
| Master password | `admin` |
| Database name | `odoo_dev` (your choice) |
| Email / Password | your login |

## Project layout

```
odoo-practice/
├── docker-compose.yml   # Odoo 17 + PostgreSQL
├── config/odoo.conf     # Odoo server config
└── addons/              # Custom modules go here
```

## Useful commands

```bash
docker compose up -d      # start
docker compose down       # stop
docker compose logs -f odoo   # view logs
docker compose restart odoo   # after adding a new module
```

## Learning path

1. Phase 1–2: ERP concepts + Odoo Online trial
2. Phase 3: Custom modules in `addons/`
3. Phase 4: Portfolio mini-project
