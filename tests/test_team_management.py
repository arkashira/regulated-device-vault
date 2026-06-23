from team_management import TeamManagement, TeamMember
import pytest

def test_invite_member():
    team_management = TeamManagement()
    token = team_management.invite_member("test@example.com", "Developer")
    assert token is not None
    assert "test@example.com" in team_management.team_members

def test_revoke_access():
    team_management = TeamManagement()
    team_management.invite_member("test@example.com", "Developer")
    team_management.revoke_access("test@example.com")
    assert "test@example.com" not in team_management.team_members

def test_get_member_role():
    team_management = TeamManagement()
    team_management.invite_member("test@example.com", "Developer")
    assert team_management.get_member_role("test@example.com") == "Developer"

def test_create_account():
    team_management = TeamManagement()
    token = team_management.invite_member("test@example.com", "Developer")
    team_management.create_account(token)
    assert "test@example.com" in team_management.team_members

def test_check_permission():
    team_management = TeamManagement()
    team_management.invite_member("test@example.com", "Developer")
    assert team_management.check_permission("test@example.com", "merge_code")
    assert not team_management.check_permission("test@example.com", "view_compliance_artifacts")

def test_invalid_role():
    team_management = TeamManagement()
    with pytest.raises(ValueError):
        team_management.invite_member("test@example.com", "InvalidRole")

def test_invalid_token():
    team_management = TeamManagement()
    with pytest.raises(ValueError):
        team_management.create_account("InvalidToken")
