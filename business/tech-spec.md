```markdown
# Technical Specification for Regulated Device Vault v1

## Stack
- **Language**: Rust (core services), Python (data processing)
- **Framework**: Actix-web (Rust), FastAPI (Python)
- **Runtime**: Docker containers orchestrated by Kubernetes
- **Database**: PostgreSQL (relational data), MongoDB (flexible schemas)
- **Message Broker**: Apache Kafka (event streaming)
- **Search**: Elasticsearch (audit logs, compliance documents)

## Hosting
- **Free-tier-first platforms**: Google Cloud Run, AWS Fargate
- **Initial deployment**: Google Kubernetes Engine (GKE) with preemptible VMs
- **Data storage**: Google Cloud Storage (GCS) for backups and large files
- **Monitoring**: Google Cloud Operations Suite (formerly Stackdriver)

## Data Model
### Tables/Collections
1. **Devices**
   - `device_id` (UUID)
   - `manufacturer`
   - `model`
   - `regulation_class`
   - `firmware_version`

2. **ValidationTests**
   - `test_id` (UUID)
   - `device_id` (UUID, foreign key)
   - `test_type`
   - `test_parameters`
   - `result`
   - `timestamp`

3. **ComplianceDocuments**
   - `document_id` (UUID)
   - `device_id` (UUID, foreign key)
   - `document_type`
   - `content` (base64 encoded)
   - `version`
   - `status`

4. **AuditLogs**
   - `log_id` (UUID)
   - `user_id` (UUID)
   - `action`
   - `timestamp`
   - `metadata`

## API Surface
1. **POST /api/devices** - Register a new medical device
2. **GET /api/devices/{device_id}** - Retrieve device details
3. **POST /api/tests** - Initiate a validation test
4. **GET /api/tests/{test_id}** - Retrieve test results
5. **POST /api/documents** - Upload a compliance document
6. **GET /api/documents/{document_id}** - Retrieve a compliance document
7. **GET /api/audit** - Retrieve audit logs (filtered by date, user, action)
8. **POST /api/users** - Register a new user (admin only)
9. **POST /api/users/{user_id}/roles** - Assign roles to a user (admin only)
10. **GET /api/users/{user_id}/permissions** - Check user permissions

## Security Model
- **Authentication**: OAuth 2.0 with JWT tokens
- **Authorization**: Role-Based Access Control (RBAC) with the following roles:
  - **Admin**: Full access
  - **Developer**: Can register devices, run tests, upload documents
  - **Auditor**: Read-only access to devices, tests, and documents
- **Secrets Management**: HashiCorp Vault for managing secrets and encryption keys
- **IAM**: Google Cloud IAM for managing access to cloud resources

## Observability
- **Logs**: Structured JSON logs sent to Google Cloud Logging
- **Metrics**: Prometheus for collecting and storing metrics, Grafana for visualization
- **Traces**: OpenTelemetry for distributed tracing, Jaeger for trace visualization

## Build/CI
- **Version Control**: GitHub
- **CI/CD Pipeline**: GitHub Actions
- **Build Tools**: Rust's Cargo, Python's pipenv
- **Containerization**: Docker
- **Orchestration**: Kubernetes
- **Testing**: pytest (Python), cargo test (Rust)
- **Security Scanning**: Trivy for container vulnerability scanning
- **Static Code Analysis**: SonarQube
```