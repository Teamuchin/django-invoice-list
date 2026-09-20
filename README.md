# Invoice List (Django)

A small Django application exploring models, the ORM and URL routing: an invoice owns a list of line items, each of which can be marked complete.

**Personal project (not coursework)**

## Layout

| Path | Contents |
|---|---|
| `manage.py` | Django entry point |
| `main/models.py` | `FaturaList` (invoice) and `Item` (line item) models, with `Item` cascading from its invoice |
| `main/views.py` | Index view that looks up one invoice by id |
| `main/urls.py` | Routes `/<id>` to that view |
| `main/migrations/` | Schema migrations, including a later change to the item date field |
| `testsite/` | Project package — `settings.py`, root `urls.py`, `wsgi.py`, `asgi.py` |

## Running

```bash
python -m venv .venv && source .venv/bin/activate
pip install django
python manage.py migrate
python manage.py runserver
```

`db.sqlite3` is kept as `db.sqlite3.example` so a fresh database is created by `migrate`.

## Notes

The domain naming is Turkish — `FaturaList` means invoice list. `Item.name` is a
`ForeignKey` to its invoice rather than a plain field, and `last_date` is an `IntegerField`
carrying a `max_length`; both are left exactly as written.

---

Submitted reports, worksheets and lecture material are archived outside this
repository rather than committed, so the repo stays code-only.
