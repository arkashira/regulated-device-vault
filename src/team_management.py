import json
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class TeamMember:
    email: str
    role: str

class TeamManagement:
    def __init__(self):
        self.team_members: Dict[str, TeamMember] = {}
        self.roles: Dict[str, bool] = {"Developer": False, "QA": False, "Compliance": False}

    def invite_member(self, email: str, role: str) -> str:
        if role not in self.roles:
            raise ValueError("Invalid role")
        token = json.dumps({"email": email, "role": role}).encode()
        self.team_members[email] = TeamMember(email, role)
        return token.decode()

    def revoke_access(self, email: str) -> None:
        if email in self.team_members:
            del self.team_members[email]

    def get_member_role(self, email: str) -> str:
        if email in self.team_members:
            return self.team_members[email].role
        return None

    def create_account(self, token: str) -> None:
        try:
            data = json.loads(token)
            email = data["email"]
            role = data["role"]
            if email not in self.team_members:
                self.team_members[email] = TeamMember(email, role)
        except json.JSONDecodeError:
            raise ValueError("Invalid token")

    def check_permission(self, email: str, permission: str) -> bool:
        if email not in self.team_members:
            return False
        role = self.team_members[email].role
        if role == "Developer" and permission == "merge_code":
            return True
        elif role == "QA" and permission == "view_compliance_artifacts":
            return True
        elif role == "Compliance" and permission == "view_compliance_artifacts":
            return True
        return False
