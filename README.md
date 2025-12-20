# SAYeTECH Investor Dataroom

A comprehensive, secure investor dataroom platform built with FastAPI, MongoDB, and Python. This system enables SAYeTECH to manage investor access, share documents, track analytics, and facilitate investor engagement seamlessly.

**Live API Documentation**: https://dataroom-backend-api.onrender.com/docs#/ Application for IT Developer Position

![Version](https://img.shields.io/badge/version-2.0.0-blue)
![Python](https://img.shields.io/badge/python-3.9+-green)
![FastAPI](https://img.shields.io/badge/fastapi-0.109.0-teal)
![MongoDB](https://img.shields.io/badge/mongodb-4.6+-brightgreen)

## Platform Overview

![Landing Page](https://ik.imagekit.io/lleqzwfovk/WhatsApp%20Image%202025-11-27%20at%2010.44.47%20AM.jpeg)
*Secure investor due diligence platform with OTP authentication and NDA-protected access*


--
## Table of Contents

- [Features](#features)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Database Setup](#database-setup)
- [API Documentation](#api-documentation)
- [Project Structure](#project-structure)
- [Usage Examples](#usage-examples)
- [Security Features](#security-features)
- [Deployment](#deployment)
- [Testing](#testing)
- [Performance](#performance-optimization)
- [Contributing](#contributing)
- [License](#license)

---

## Features

### Landing Page Experience
The platform features a clean, professional landing page showcasing:
- **Deal-Ready Data Room**: Streamlined investor due diligence process
- **Secure Access Controls**: OTP authentication and NDA-protected entry
- **Key Statistics**: Quick overview of security features and document categories
- **Dual Entry Points**: Request access for new investors or login for approved users

### Access Management
- **Investor Access Requests**: Email-based access request system with approval workflow
- **OTP Verification**: Two-factor authentication for enhanced security
- **Admin Approval System**: Review, approve, deny, or set expiration dates
- **Investor ID Generation**: Automatic unique investor ID assignment upon approval
- **Audit Logging**: Complete trail of all access changes and actions

### Document Management
The platform organizes documents into six strategic categories:

1. **Company Overview**: Mission, vision, team bios, and organizational structure
2. **Market & Impact**: Market analysis, competitive landscape, and social impact metrics
3. **Financials**: Historical financials, projections, and unit economics
4. **IP & Technology**: Product roadmap, technical architecture, and patents
5. **Traction**: Customer metrics, growth data, and key partnerships
6. **Legal**: Cap table, contracts, compliance, and governance documents

**Document Features:**
- **Secure Upload**: Support for PDF, DOC, DOCX, XLS, XLSX, PPT, PPTX (up to 50MB)
- **Version Control**: Track document versions with clear version badges (v1, v2, v3)
- **Full-Text Search**: Search documents by title, description, tags, and content
- **Auto-suggestions**: Smart search suggestions as you type
- **View/Download Tracking**: Monitor document engagement with eye and download icons
- **Quick Stats**: Total document count and last updated timestamp

### Investor Dashboard
Upon login, investors see a comprehensive dashboard featuring:

**Key Information Cards:**
- **Round Details**: Current funding round (e.g., Series A - Raising $2M-$5M)
- **Key Metrics**: Impact statistics (e.g., 50K+ farmers reached across Africa)
- **Access Status**: Current access level (Active with full data room access)

**Quick Access Sections:**
- **Pitch Deck**: Company overview presentation
- **Financial Model**: Projections and actuals
- **Legal Documents**: Cap table, contracts, and compliance materials

The dashboard provides a high-level overview with intuitive navigation to detailed documents.
- **Multi-filter Search**: Filter by type, date, category, and tags
- **Search History**: Track investor search patterns for analytics
- **Quick Access**: Recently viewed documents for easy reference

### Real-time Analytics
- **Activity Dashboard**: Live tracking of active users and engagement metrics
- **Document Heatmap**: Visualize most-viewed and downloaded documents
- **Investor Activity Reports**: Time spent, documents viewed, last active status
- **Export Functionality**: Generate CSV/PDF reports for any date range
- **30-second Auto-refresh**: Real-time dashboard updates

### Smart Alert System
- **High-Value Investor Alerts**: Notifications when key investors log in
- **Critical Document Tracking**: Alerts when specific documents are accessed
- **Session Duration Alerts**: Trigger notifications on extended session times
- **Multi-channel Notifications**: Email and Slack integration support
- **Configurable Triggers**: Customize alert conditions per requirement

### Q&A System
- **In-app Questions**: Investors submit questions directly through the platform
- **Category Tagging**: Organize questions by topic for easy management
- **Public/Private Responses**: Choose visibility level for each answer
- **Email Notifications**: Automatic notifications when questions are answered
- **Search Q&A History**: Find answers to previously asked questions

### Meeting Scheduler
- **Calendar Integration**: Compatible with Google Calendar and Outlook
- **Available Time Slots**: Dynamic slot availability checking (9 AM - 5 PM)
- **Automated Reminders**: 24-hour and 1-hour email reminders before meetings
- **Reschedule/Cancel**: Easy meeting management with email notifications
- **Meeting Links**: Auto-generated secure meeting URLs
- **Timezone-Aware**: Proper handling of UTC and local timezones

### Company Showcase
- **Executive Dashboard**: Key metrics and impact indicators
- **Dynamic Metrics**: Real-time company performance data
- **Testimonials**: Customer success stories and social proof
- **Media Coverage**: Press mentions and industry awards
- **Investment Summary**: Downloadable company one-pagers

### Security & Compliance
- **TLS/SSL Encryption**: Secure data transmission
- **MongoDB Encryption**: Data at rest protection
- **JWT Authentication**: Token-based secure access
- **Password Hashing**: Bcrypt encryption for all passwords
- **GDPR Compliance**: Data export and deletion capabilities
- **Audit Trails**: Complete security and action logging
- **IP Tracking**: Monitor access locations and patterns

---

## Architecture

```
┌─────────────────┐
│   FastAPI API   │
│   (Python)      │
└────────┬────────┘
         │
    ┌────┴────┐
    │         │
┌───▼────┐ ┌─▼──────────┐
│MongoDB │ │   Redis    │
│Database│ │   Cache    │
└────────┘ └────────────┘
```

**Technology Stack:**
- **Backend Framework**: FastAPI (Python 3.9+)
- **Database**: MongoDB Atlas
- **Cache Layer**: Redis (optional, recommended for production)
- **File Storage**: Local filesystem or Cloud storage (S3, Azure Blob)
- **Email Service**: SMTP (Gmail, SendGrid, AWS SES)
- **Notifications**: Slack Webhooks, Email alerts
- **Authentication**: JWT tokens with bcrypt password hashing

---

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.9 or higher
- MongoDB Atlas account (or local MongoDB instance)
- SMTP email account (Gmail recommended for development)
- Redis server (optional, recommended for production)
- Minimum 2GB RAM
- Minimum 10GB storage space

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/p-mensah/dataroom_backend_api.git
cd dataroom_backend_api
```

### 2. Create Virtual Environment

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS/Linux:**
```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Installation Steps

To properly set up the platform UI assets:

1. **Create Documentation Directory**
```bash
mkdir -p docs/images
```

2. **Add Platform Screenshots**
Place the following images in `docs/images/`:
- `landing-page.png` - Landing page with access request form
- `dashboard.png` - Investor dashboard with metrics
- `categories.png` - Six document categories overview
- `documents.png` - Document listing with version control

These images will be referenced in the README to help users understand the platform interface.

**Windows:**
```bash
mkdir uploads\documents
type nul > app\__init__.py
```

**macOS/Linux:**
```bash
mkdir -p uploads/documents
touch app/__init__.py
```

---

## Configuration

### 1. Environment Variables

Create a `.env` file in the root directory with the following variables:

```env
# Application Settings
APP_NAME=SAYeTECH Investor Dataroom

# MongoDB Configuration
MONGODB_URL=mongodb+srv://username:password@cluster.mongodb.net/?retryWrites=true&w=majority
DATABASE_NAME=investor_dataroom

# Email Configuration (Gmail Example)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your-email@gmail.com
SMTP_PASSWORD=your-app-password
FROM_EMAIL=your-email@gmail.com
ADMIN_EMAIL=admin@sayetech.com

# Security
SECRET_KEY=your-super-secret-key-change-this-in-production-min-32-chars
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# File Upload Settings
UPLOAD_DIR=uploads/documents
MAX_FILE_SIZE=52428800
ALLOWED_EXTENSIONS=[".pdf",".doc",".docx",".xls",".xlsx",".ppt",".pptx"]

# Redis (Optional - for caching)
REDIS_URL=redis://localhost:6379
CACHE_TTL=3600

# Slack Notifications (Optional)
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/YOUR/WEBHOOK/URL

# Meeting Configuration
CALENDLY_API_KEY=your-calendly-api-key
```

### 2. MongoDB Atlas Setup

1. Create a free cluster at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
2. Create a database user with read/write permissions
3. Whitelist your IP address (use `0.0.0.0/0` for testing only)
4. Get your connection string from the "Connect" button
5. Replace `username` and `password` in the connection string
6. Update `MONGODB_URL` in your `.env` file

### 3. Gmail App Password Setup

For Gmail SMTP integration:

1. Enable 2-Factor Authentication on your Google account
2. Visit: https://myaccount.google.com/apppasswords
3. Select "Mail" and "Other (Custom name)"
4. Generate the app password
5. Use this 16-character password in `SMTP_PASSWORD`

**Note:** Never use your actual Gmail password in the application.

---

## Database Setup

The application automatically creates database indexes on startup. To verify or manually create indexes:

```python
from app.database import create_indexes
create_indexes()
```

### Collections Created Automatically:

- `access_requests` - Investor access requests and approval status
- `investors` - Approved investor profiles with unique IDs
- `admin_users` - Administrator accounts
- `documents` - Uploaded document metadata
- `document_access` - Document view and download logs
- `qa_threads` - Questions submitted by investors
- `qa_responses` - Admin responses to questions
- `meetings` - Scheduled meetings with investors
- `alert_configs` - Alert rule configurations
- `alert_logs` - Triggered alert history
- `search_history` - Investor search query logs
- `company_metrics` - Company performance KPIs
- `testimonials` - Customer testimonials
- `audit_logs` - System-wide audit trail

---

## Running the Application

### Development Mode

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Production Mode

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

### Access Points:

- **API Base URL**: http://localhost:8000
- **Interactive API Docs (Swagger)**: http://localhost:8000/docs
- **Alternative API Docs (ReDoc)**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health

---

## API Documentation

### Authentication Endpoints

```http
POST   /api/auth/login                    # User/Admin login
POST   /api/auth/register                 # Admin registration
POST   /api/auth/verify-otp               # OTP verification
POST   /api/auth/resend-otp               # Resend OTP code
GET    /api/auth/me                       # Get current user info
```

### Access Request Endpoints

```http
POST   /api/access-requests                # Submit new access request
GET    /api/access-requests/{id}           # Get request details
GET    /api/access-requests/check/{email}  # Check request status
PATCH  /api/access-requests/{id}/approve   # Approve request (creates investor)
PATCH  /api/access-requests/{id}/deny      # Deny request
GET    /api/admin/access-requests          # List all requests (admin)
```

### Document Management Endpoints

```http
POST   /api/documents/upload                # Upload new document
GET    /api/documents/search                # Search documents
GET    /api/documents/{id}                  # Get document details
GET    /api/documents/{id}/download         # Download document
PUT    /api/documents/{id}                  # Update document
DELETE /api/documents/{id}                  # Delete document
GET    /api/documents/categories/list       # List all categories
GET    /api/documents/suggestions           # Get search suggestions
GET    /api/documents/recent                # Get recently viewed docs
```

### Q&A Endpoints

```http
POST   /api/qa/threads                      # Create new question
GET    /api/qa/threads                      # List all questions
GET    /api/qa/threads/{id}                 # Get specific thread
POST   /api/qa/threads/{id}/respond         # Post answer (admin)
PUT    /api/qa/threads/{id}                 # Update question/answer
DELETE /api/qa/threads/{id}                 # Delete thread
GET    /api/qa/threads/search               # Search Q&A history
```

### Meeting Scheduler Endpoints

```http
POST   /api/meetings/                       # Schedule new meeting
GET    /api/meetings/                       # List all meetings (admin)
GET    /api/meetings/my-meetings            # Get user's meetings
GET    /api/meetings/upcoming               # Get upcoming meetings
GET    /api/meetings/available-slots        # Get available time slots
GET    /api/meetings/{id}                   # Get meeting details
PUT    /api/meetings/{id}/reschedule        # Reschedule meeting
PUT    /api/meetings/{id}/cancel            # Cancel meeting
PUT    /api/meetings/{id}/complete          # Mark as completed (admin)
DELETE /api/meetings/{id}                   # Delete meeting (admin)
```

### Analytics Endpoints

```http
GET    /api/analytics/dashboard             # Get dashboard statistics
GET    /api/analytics/heatmap               # Document engagement heatmap
GET    /api/analytics/investor/{id}/activity # Investor activity report
GET    /api/analytics/investors/list        # All investor activities
GET    /api/analytics/export                # Export analytics to CSV
```

### Company Information Endpoints

```http
GET    /api/company/metrics                 # Get company metrics
POST   /api/company/metrics                 # Update metrics (admin)
PUT    /api/company/metrics/{id}            # Update specific metric
GET    /api/company/testimonials            # Get testimonials
POST   /api/company/testimonials            # Add testimonial (admin)
DELETE /api/company/testimonials/{id}       # Delete testimonial
```

### Alert System Endpoints

```http
POST   /api/alerts/config                   # Create alert configuration
GET    /api/alerts/config                   # List all alert configs
PUT    /api/alerts/config/{id}              # Update alert config
DELETE /api/alerts/config/{id}              # Delete alert config
GET    /api/alerts/logs                     # Get alert trigger logs
```

---

## Project Structure

```
dataroom_backend_api/
│
├── app/
│   ├── __init__.py                # Package initializer
│   ├── main.py                    # Application entry point
│   ├── config.py                  # Configuration settings
│   ├── database.py                # MongoDB connection setup
│   ├── models.py                  # Pydantic models
│   ├── services.py                # Business logic layer
│   └── utils.py                   # Helper functions
│
├── uploads/                       # File storage directory
│   └── documents/                 # Uploaded documents
│
├── .env                          # Environment variables (gitignored)
├── .gitignore                    # Git ignore rules
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```

---

## User Experience Flow

### For New Investors

1. **Landing Page**: Visit the SAYeTECH Investor Data Room landing page
2. **Request Access**: Click "Request Access to Data Room" button
3. **Submit Information**: Provide email, name, company, phone, and message
4. **OTP Verification**: Receive and verify OTP code via email
5. **Admin Review**: Wait for admin approval (typically 24-48 hours)
6. **Approval Notification**: Receive email with unique Investor ID
7. **Login**: Access data room with approved credentials
8. **Dashboard**: View company overview and key metrics
9. **Browse Documents**: Navigate six organized categories
10. **Due Diligence**: View and download documents as needed

### For Approved Investors

1. **Login**: Click "Already Approved? Login" or "Investor Login"
2. **OTP Authentication**: Enter email and verify OTP
3. **Dashboard Access**: Land on personalized dashboard
4. **Quick Actions**: 
   - View round details (Series A status)
   - Check key metrics (50K+ farmers reached)
   - Confirm access status (Active)
5. **Document Navigation**:
   - Click document categories in navigation
   - Search documents using search bar
   - View documents (eye icon)
   - Download documents (download icon)
6. **Version Tracking**: See version badges (v1, v2, v3) on documents

### For Administrators

1. **Admin Portal**: Access admin dashboard
2. **Review Requests**: View pending access requests
3. **Approve/Deny**: Make decisions with optional notes
4. **Investor Creation**: System auto-generates investor ID upon approval
5. **Document Management**: Upload and organize documents by category
6. **Analytics**: Monitor investor activity and document engagement
7. **Meeting Scheduler**: Coordinate meetings with investors
8. **Q&A Management**: Respond to investor questions

### 1. Submit Access Request

```python
import requests

url = "http://localhost:8000/api/access-requests"
payload = {
    "email": "investor@example.com",
    "full_name": "John Doe",
    "company": "Investment Firm LLC",
    "phone": "+1234567890",
    "message": "Interested in learning more about SAYeTECH"
}

response = requests.post(url, json=payload)
print(response.json())
# Output: {"message": "Access request submitted successfully", "id": "...", "status": "pending"}
```

### 2. Approve Access Request (Admin)

```python
import requests

url = "http://localhost:8000/api/access-requests/{request_id}/approve"
headers = {"Authorization": "Bearer YOUR_ADMIN_TOKEN"}
payload = {"admin_notes": "Approved for Q1 2025 review"}

response = requests.patch(url, json=payload, headers=headers)
print(response.json())
# Output: {"message": "Access request approved successfully", "investor_id": "INV-20250112-A7B3C9"}
```

### 3. Search Documents

```python
import requests

url = "http://localhost:8000/api/documents/search"
headers = {"Authorization": "Bearer YOUR_TOKEN"}
params = {
    "query": "financial statements",
    "category": "financials",
    "investor_id": "INV-20250112-A7B3C9"
}

response = requests.get(url, params=params, headers=headers)
documents = response.json()
```

### 4. Schedule Meeting

```python
import requests

url = "http://localhost:8000/api/meetings/"
headers = {"Authorization": "Bearer YOUR_TOKEN"}
params = {"investor_id": "INV-20250112-A7B3C9"}
payload = {
    "scheduled_at": "2025-01-15T14:00:00Z",
    "duration_minutes": 30,
    "notes": "Q4 investment discussion"
}

response = requests.post(url, json=payload, params=params, headers=headers)
print(response.json())
```

### 5. Get Analytics Dashboard

```python
import requests

url = "http://localhost:8000/api/analytics/dashboard"
headers = {"Authorization": "Bearer YOUR_ADMIN_TOKEN"}

response = requests.get(url, headers=headers)
stats = response.json()
print(f"Active users: {stats['active_users']}")
print(f"Total documents: {stats['total_documents']}")
```

---

## Security Features

### Authentication & Authorization
- **JWT Token-based Authentication**: Secure, stateless authentication
- **Password Hashing**: Bcrypt with salt for password storage
- **OTP Verification**: Two-factor authentication for access requests
- **Role-based Access Control**: Admin vs. Investor permissions

### Data Protection
- **Input Validation**: Pydantic model validation for all inputs
- **File Type Validation**: Whitelist-based file upload validation
- **SQL Injection Prevention**: MongoDB parameterized queries
- **XSS Protection**: Input sanitization and output encoding
- **HTTPS/TLS**: Encrypted data transmission in production

### Operational Security
- **Rate Limiting**: Prevent abuse and DDoS attacks
- **CORS Protection**: Configurable allowed origins
- **Audit Logging**: Complete trail of all system actions
- **IP Tracking**: Monitor and log access locations
- **Session Management**: Secure token expiration and refresh

---

## Deployment

### Docker Deployment

**Dockerfile:**
```dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create uploads directory
RUN mkdir -p uploads/documents

# Expose port
EXPOSE 8000

# Run application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**Build and Run:**
```bash
docker build -t dataroom-api .
docker run -p 8000:8000 --env-file .env dataroom-api
```

### Docker Compose (with MongoDB and Redis)

**docker-compose.yml:**
```yaml
version: '3.8'

services:
  api:
    build: .
    ports:
      - "8000:8000"
    env_file:
      - .env
    depends_on:
      - mongodb
      - redis
    volumes:
      - ./uploads:/app/uploads

  mongodb:
    image: mongo:6.0
    ports:
      - "27017:27017"
    environment:
      MONGO_INITDB_ROOT_USERNAME: admin
      MONGO_INITDB_ROOT_PASSWORD: password
    volumes:
      - mongodb_data:/data/db

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

volumes:
  mongodb_data:
```

### Production Deployment Checklist

- [ ] Change `SECRET_KEY` to a cryptographically secure random string
- [ ] Set specific CORS origins (remove wildcard `*`)
- [ ] Enable HTTPS with valid SSL certificates
- [ ] Configure MongoDB backups (automated daily backups)
- [ ] Set up Redis for production caching
- [ ] Configure monitoring (Sentry, DataDog, New Relic)
- [ ] Enable rate limiting on all endpoints
- [ ] Set up CDN for static file delivery
- [ ] Configure firewall rules (allow only necessary ports)
- [ ] Set up log aggregation (ELK stack, CloudWatch)
- [ ] Enable database encryption at rest
- [ ] Configure automated security patches
- [ ] Set up health check endpoints for load balancers
- [ ] Create disaster recovery plan

---

## Testing

### Install Test Dependencies

```bash
pip install pytest pytest-asyncio pytest-cov httpx
```

### Run Tests

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest --cov=app tests/

# Run specific test file
pytest tests/test_access_requests.py

# Run with verbose output
pytest -v tests/
```

### Test Structure

```
tests/
├── test_access_requests.py
├── test_documents.py
├── test_meetings.py
├── test_qa.py
└── test_analytics.py
```

---

## Performance Optimization

### Database Optimization
- **Indexing**: Automatic index creation on frequently queried fields
- **Connection Pooling**: MongoDB connection pooling enabled
- **Query Optimization**: Efficient queries with projection and aggregation

### Caching Strategy
- **Redis Caching**: Cache frequently accessed data (documents, metrics)
- **TTL Configuration**: Configurable cache expiration times
- **Cache Invalidation**: Smart cache invalidation on data updates

### Application Performance
- **Async Operations**: Non-blocking I/O for file operations
- **Response Compression**: Gzip compression for API responses
- **CDN Integration**: Serve static files via CDN
- **Lazy Loading**: Paginated responses for large datasets

### Monitoring
- **Response Time Tracking**: Monitor API endpoint performance
- **Database Query Analysis**: Identify slow queries
- **Resource Usage**: Track CPU, memory, and disk usage
- **Error Rate Monitoring**: Alert on elevated error rates

---

## Contributing

We welcome contributions from the community. Please follow these guidelines:

### Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally
3. Create a new feature branch
4. Make your changes
5. Write or update tests as needed
6. Ensure all tests pass
7. Submit a pull request

### Code Style

- Follow PEP 8 style guidelines for Python code
- Use type hints for function parameters and returns
- Write docstrings for all functions and classes
- Keep functions small and focused on a single task

### Commit Messages

- Use clear, descriptive commit messages
- Start with a verb (Add, Fix, Update, Remove)
- Reference issue numbers when applicable

### Example Workflow

```bash
# Fork and clone
git clone https://github.com/YOUR_USERNAME/dataroom_backend_api.git
cd dataroom_backend_api

# Create feature branch
git checkout -b feature/add-new-endpoint

# Make changes and commit
git add .
git commit -m "Add new investor analytics endpoint"

# Push to your fork
git push origin feature/add-new-endpoint

# Open pull request on GitHub
```

---

## Troubleshooting

### Common Issues

**MongoDB Connection Failed**
```
Solution: Check MONGODB_URL in .env, verify network access in MongoDB Atlas
```

**Email Sending Failed**
```
Solution: Verify SMTP credentials, check firewall allows port 587/465
```

**File Upload Failed**
```
Solution: Check uploads/documents directory exists and has write permissions
```

**Import Errors**
```
Solution: Ensure all dependencies are installed: pip install -r requirements.txt
```

---

## License

This project is proprietary and confidential. All rights reserved by SAYeTECH.

Unauthorized copying, distribution, or use of this software is strictly prohibited.

---

## Support

For questions, issues, or feature requests:

- **Email**: admin@sayetech.com
- **GitHub Issues**: [Create an issue](https://github.com/p-mensah/dataroom_backend_api/issues)
- **Documentation**: [Full documentation](https://dataroom-backend-api.onrender.com/docs#/)

---

## Acknowledgments

This project is built with the following open-source technologies:

- [FastAPI](https://fastapi.tiangolo.com/) - Modern, fast web framework for Python
- [MongoDB](https://www.mongodb.com/) - Document-oriented NoSQL database
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Data validation using Python type hints
- [Python](https://www.python.org/) - Programming language
- [Uvicorn](https://www.uvicorn.org/) - ASGI server implementation

---

**Copyright 2025 SAYeTECH. All rights reserved.**
