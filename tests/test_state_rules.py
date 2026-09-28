import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from state_rules import can_transition, revival_candidate, transition_idea


class TrajectoryGuardianStateRulesTests(unittest.TestCase):
    def test_silence_does_not_equal_rejection(self):
        self.assertFalse(can_transition("DORMANT", "REJECTED"))

    def test_parked_does_not_jump_to_active(self):
        self.assertFalse(can_transition("PARKED", "ACTIVE"))

    def test_parked_can_reopen_as_exploring(self):
        self.assertEqual(
            transition_idea("PARKED", "EXPLORING", changed_context=True),
            "EXPLORING",
        )

    def test_rejected_requires_reason_to_reopen(self):
        with self.assertRaises(ValueError):
            transition_idea("REJECTED", "EXPLORING")

    def test_rejected_can_reopen_when_context_changes(self):
        self.assertEqual(
            transition_idea("REJECTED", "EXPLORING", changed_context=True),
            "EXPLORING",
        )

    def test_active_commitment_requires_user_authority(self):
        with self.assertRaises(ValueError):
            transition_idea("EXPLORING", "ACTIVE")

        self.assertEqual(
            transition_idea("EXPLORING", "ACTIVE", explicit_user_intent=True),
            "ACTIVE",
        )

    def test_rejection_requires_user_authority(self):
        with self.assertRaises(ValueError):
            transition_idea("EXPLORING", "REJECTED")

        self.assertEqual(
            transition_idea("EXPLORING", "REJECTED", explicit_user_intent=True),
            "REJECTED",
        )

    def test_revival_candidate_when_blocker_resolved(self):
        self.assertTrue(
            revival_candidate("PARKED", blocker_resolved=True, user_reopens=False)
        )

    def test_active_item_is_not_revival_candidate(self):
        self.assertFalse(
            revival_candidate("ACTIVE", blocker_resolved=True, user_reopens=True)
        )


if __name__ == "__main__":
    unittest.main()
