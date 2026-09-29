import unittest

import core


class TestCore(unittest.TestCase):
    def test_01_no_duplicate_feed(self):
        state = core.new_game()
        self.assertTrue(core.feed(state, 1, 10))
        self.assertFalse(core.feed(state, 1, 10))

    def test_02_machine_capacity(self):
        state = core.new_game()
        state["machine_load"] = 2
        result = core.feed(state, 2, 1)
        self.assertFalse(result)

    def test_03_temp_boundary(self):
        state = core.new_game()
        self.assertEqual(core.check_temp(state, 35), "over")

    def test_04_cancel_releases(self):
        state = core.new_game()
        core.feed(state, 1, 10)
        core.cancel(state, 1)
        self.assertEqual(state["machine_load"], 0)

    def test_05_no_produce_on_aoi_fault(self):
        state = core.new_game()
        state["aoi_fault"] = True
        result = core.produce(state, 5)
        self.assertFalse(result)

    def test_06_static_once(self):
        state = core.new_game()
        core.static_event(state)
        self.assertEqual(state["yield_rate"], 95)

    def test_07_no_place_without_components(self):
        state = core.new_game()
        state["components"] = 0
        result = core.place(state, 5)
        self.assertFalse(result)

    def test_08_load_preserves_order(self):
        state = core.new_game()
        state["order_id"] = 4
        loaded = core.load_state(core.save_state(state))
        self.assertEqual(loaded["order_id"], 4)


if __name__ == "__main__":
    unittest.main()
