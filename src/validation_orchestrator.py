import json
import dataclasses
import datetime
import smtplib
from email.message import EmailMessage
from typing import List
import unittest.mock as mock

@dataclasses.dataclass
class ValidationResult:
    test_name: str
    result: bool
    message: str

class ValidationOrchestrator:
    def __init__(self, cron_job_interval: int = 24):
        self.cron_job_interval = cron_job_interval
        self.validation_results = []

    def schedule_validation_run(self):
        # Simulate a cron job trigger
        print(f"Scheduling validation run every {self.cron_job_interval} hours")

    def run_validation_tests(self):
        # Simulate running validation tests
        test_results = [
            ValidationResult("Firmware Test", True, "Firmware test passed"),
            ValidationResult("Cloud Test", False, "Cloud test failed")
        ]
        self.validation_results.extend(test_results)

    def aggregate_results(self):
        # Simulate aggregating validation results into a dashboard
        dashboard = {
            "test_results": self.validation_results
        }
        return dashboard

    def send_email_alert(self, project_owner: str, failures: List[ValidationResult]):
        # Simulate sending an email alert
        msg = EmailMessage()
        msg.set_content("Validation test failures")
        msg["Subject"] = "Validation Test Failures"
        msg["From"] = "validation_orchestrator@example.com"
        msg["To"] = project_owner
        try:
            with smtplib.SMTP("localhost") as smtp:
                smtp.send_message(msg)
        except smtplib.SMTPException as e:
            print(f"Error sending email: {e}")

    def trigger_email_alert(self, project_owner: str):
        failures = [result for result in self.validation_results if not result.result]
        if failures:
            self.send_email_alert(project_owner, failures)

    def main(self):
        self.schedule_validation_run()
        self.run_validation_tests()
        dashboard = self.aggregate_results()
        print(json.dumps(dashboard, indent=4))
        self.trigger_email_alert("project_owner@example.com")

if __name__ == "__main__":
    orchestrator = ValidationOrchestrator()
    orchestrator.main()
