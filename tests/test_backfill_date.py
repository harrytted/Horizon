from datetime import datetime, timezone
import unittest

from src.orchestrator import resolve_run_window


class BackfillDateTests(unittest.TestCase):
    def test_resolve_run_window_for_target_date(self) -> None:
        since, until, output_date = resolve_run_window(
            force_hours=24,
            target_date="2026-07-25",
        )

        self.assertEqual(since, datetime(2026, 7, 25, tzinfo=timezone.utc))
        self.assertEqual(until, datetime(2026, 7, 26, tzinfo=timezone.utc))
        self.assertEqual(output_date, "2026-07-25")

    def test_resolve_run_window_rejects_invalid_date(self) -> None:
        with self.assertRaisesRegex(ValueError, "YYYY-MM-DD"):
            resolve_run_window(force_hours=24, target_date="2026/07/25")


if __name__ == "__main__":
    unittest.main()
