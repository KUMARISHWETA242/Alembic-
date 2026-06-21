# SQLAlchemy & Alembic

## What is SQLAlchemy?

SQLAlchemy is a Python ORM (Object Relational Mapper) that allows you to interact with databases using Python classes instead of writing raw SQL queries.

### Benefits

* Write database operations using Python.
* Supports PostgreSQL, MySQL, SQLite, Oracle, and more.
* Helps prevent SQL injection attacks.
* Database-independent code.
* Widely used in production applications.

---

## What is Alembic?

Alembic is the official database migration tool for SQLAlchemy.

It helps track and apply database schema changes over time.

### Benefits

* Auto-generates migration scripts.
* Supports upgrades and downgrades.
* Maintains schema version history.
* Integrates with CI/CD pipelines.

---

![Architecture Diagram](images/Alembic.png)

# One-Time Project Setup

## 1. Install Dependencies

```bash
pip install sqlalchemy alembic
```

## 2. Initialize Alembic

```bash
alembic init migrations
```

This creates:

```text
project/
│
├── alembic.ini
├── migrations/
│   ├── env.py
│   ├── script.py.mako
│   └── versions/
```

## 3. Configure Database URL

Update `alembic.ini`:

```ini
sqlalchemy.url = postgresql://username:password@localhost/dbname
```

## 4. Connect Alembic to SQLAlchemy Models

Update `migrations/env.py`:

```python
from models import Base

target_metadata = Base.metadata
```

This allows Alembic to detect schema changes from your SQLAlchemy models.

---

# Migration Workflow

Follow these steps whenever your database schema changes.

## Step 1: Update Your Models

Example:

```python
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
```

## Step 2: Generate Migration

```bash
alembic revision --autogenerate -m "create users table"
```

Alembic compares:

* SQLAlchemy models (`Base.metadata`)
* Current database schema

and generates a migration file inside:

```text
migrations/versions/
```

## Step 3: Review Generated Migration

Example:

```python
def upgrade():
    op.create_table(...)

def downgrade():
    op.drop_table(...)
```

## Step 4: Apply Migration

```bash
alembic upgrade head
```

Database schema is now updated.

---

# Useful Commands

### Check Current Revision

```bash
alembic current
```

Shows the migration currently applied to the database.

### View Migration History

```bash
alembic history --verbose
```

Displays all migrations in chronological order.

### Roll Back Last Migration

```bash
alembic downgrade -1
```

Reverts the most recently applied migration.

### Roll Back All Migrations

```bash
alembic downgrade base
```

Returns the database to its initial state.

### Apply All Pending Migrations

```bash
alembic upgrade head
```

Applies all pending migrations.

---

# Complete Workflow

```text
Update Models
      │
      ▼
alembic revision --autogenerate -m "message"
      │
      ▼
Review Generated Migration
      │
      ▼
alembic upgrade head
      │
      ▼
Database Updated
```

---

# Command Reference

| Command                                    | Purpose                  |
| ------------------------------------------ | ------------------------ |
| `alembic init migrations`                  | Initialize Alembic       |
| `alembic revision --autogenerate -m "msg"` | Generate migration       |
| `alembic upgrade head`                     | Apply latest migrations  |
| `alembic current`                          | Show current revision    |
| `alembic history --verbose`                | Show migration history   |
| `alembic downgrade -1`                     | Roll back one migration  |
| `alembic downgrade base`                   | Roll back all migrations |

---

# Summary

## One-Time Setup

```text
1. Install SQLAlchemy & Alembic
2. Initialize Alembic
3. Configure database URL
4. Set target_metadata
```

## For Every Schema Change

```text
1. Update models
2. Generate migration
3. Review migration
4. Apply migration
```

This is the standard workflow followed in SQLAlchemy + Alembic projects.
