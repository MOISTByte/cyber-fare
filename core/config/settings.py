def temp():
    return {
        "day": 1,
        "cash": 12400,
        "daily_revenue": 1800,
        "daily_expenses": 950,
        "reputation": 85,
        "paused": True,
        "selected_device": "firewall",
        "devices": [
            {
                "id": "firewall",
                "name": "Edge Firewall",
                "kind": "Firewall",
                "x": 450,
                "y": 280,
                "status": "Needs review",
            },
            {
                "id": "web",
                "name": "Web Server",
                "kind": "Server",
                "x": 330,
                "y": 410,
                "status": "Online",
            },
            {
                "id": "database",
                "name": "Database",
                "kind": "Database",
                "x": 570,
                "y": 410,
                "status": "Online",
            },
        ],
        "incidents": [
            "Suspicious login pattern",
            "Database backup overdue",
        ],
    }