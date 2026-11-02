from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods


def index(request):
    """Landing page — confirms the app and the database are reachable."""
    from django.db import connection

    db_status = "unknown"
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            cursor.fetchone()
        db_status = "connected"
    except Exception:
        db_status = "unreachable"

    return render(request, "demo/index.html", {"db_status": db_status})


@require_http_methods(["GET"])
def health(request):
    """Lightweight health probe (e.g. for Docker healthchecks / uptime pings)."""
    return JsonResponse({"status": "ok"})
