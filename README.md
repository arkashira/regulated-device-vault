# Validation Orchestrator
A Python project for orchestrating validation tests and sending email alerts.

## Usage
1. Run the validation orchestrator using `python -m src.validation_orchestrator`.
2. The orchestrator will schedule a validation run every 24 hours.
3. The orchestrator will run validation tests and aggregate the results into a dashboard.
4. If any tests fail, the orchestrator will send an email alert to the project owner.

## Testing
1. Run the tests using `pytest`.
2. The tests will cover the happy path and edge cases for the validation orchestrator.
