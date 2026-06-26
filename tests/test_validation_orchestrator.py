import pytest
from unittest.mock import patch
from src.validation_orchestrator import ValidationOrchestrator, ValidationResult

def test_schedule_validation_run():
    orchestrator = ValidationOrchestrator()
    orchestrator.schedule_validation_run()
    assert orchestrator.cron_job_interval == 24

def test_run_validation_tests():
    orchestrator = ValidationOrchestrator()
    orchestrator.run_validation_tests()
    assert len(orchestrator.validation_results) == 2

def test_aggregate_results():
    orchestrator = ValidationOrchestrator()
    orchestrator.run_validation_tests()
    dashboard = orchestrator.aggregate_results()
    assert "test_results" in dashboard
    assert len(dashboard["test_results"]) == 2

@patch('smtplib.SMTP')
def test_send_email_alert(mock_smtp):
    orchestrator = ValidationOrchestrator()
    orchestrator.run_validation_tests()
    failures = [result for result in orchestrator.validation_results if not result.result]
    orchestrator.send_email_alert("project_owner@example.com", failures)
    mock_smtp.assert_called_once_with("localhost")

@patch('smtplib.SMTP')
def test_trigger_email_alert(mock_smtp):
    orchestrator = ValidationOrchestrator()
    orchestrator.run_validation_tests()
    orchestrator.trigger_email_alert("project_owner@example.com")
    mock_smtp.assert_called_once_with("localhost")

def test_validation_result():
    result = ValidationResult("Test Name", True, "Test Message")
    assert result.test_name == "Test Name"
    assert result.result
    assert result.message == "Test Message"

def test_validation_orchestrator_init():
    orchestrator = ValidationOrchestrator(cron_job_interval=12)
    assert orchestrator.cron_job_interval == 12
