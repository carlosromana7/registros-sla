# SLA Tracking Application

This is a simple application designed to track and manage Service Level Agreements (SLA) records. It allows users to monitor performance metrics, track SLA compliance, and generate reports based on predefined criteria.

## Features

- Record management for SLA tracking
- Monitor SLA compliance with different metrics
- Generate reports and statistics on SLA performance
- User-friendly web interface for managing SLA data

## Project Structure

```bash
sla-tracking/
├── app
│   ├── database.py            # Database connection and configuration
│   ├── main.py                # Main application logic
│   ├── models.py              # Data models for SLAs and other entities
│   ├── static/                # Static files (CSS, JS, images)
│   └── templates/             # HTML templates for the web interface
│       ├── form.html          # Form to create/update SLA records
│       ├── registros.html     # View all SLA records
│       ├── stats.html         # SLA statistics and analysis
│       └── success.html       # Confirmation page for successful operations
├── data/                      # Database and diagnostic files
├── docker-compose.yml          # Docker Compose configuration
├── Dockerfile                  # Dockerfile to containerize the application
└── requirements.txt            # Python dependencies
