# odoo-ex — Odoo 17 Learning Project

Local Odoo 17 dev environment for learning ERP/CRM.

## Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)

## Quick start

```bash
docker compose up -d
```

Open **http://localhost:8069**

| Field | Value |
|-------|-------|
| **Master password** | `odoo123` |
| Database name | `odoo_dev` (your choice) |
| Email / Password | your login |

> The master password is **not** your Odoo login password. It is only used on the database manager screen (create / delete database).

### Master password "Access Denied"?

1. Use exactly: `odoo123` (defined in `config/odoo.conf`).
2. If it still fails, reset Docker volumes and start fresh:

```bash
docker compose down -v
docker compose up -d
```

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
2. Phase 3: Custom modules in `addons/` — see `restaurant_menu`
3. Phase 4: Portfolio mini-project

## Install a custom module

1. Open **Apps** → top-right **⋮** → **Update Apps List** → Update
2. Remove the **Apps** filter in search, type `Restaurant Menu`
3. Click **Install**
4. Open **Restaurant Menu → Menu Items** and create dishes
