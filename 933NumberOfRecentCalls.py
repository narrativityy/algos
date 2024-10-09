class RecentCounter:

    def __init__(self):
        self.queue = []
        self.counter = []

    def ping(self, t: int) -> int:
        """
        Records a ping at time t and returns the number of pings that have been recorded in the past 3000 milliseconds.
        """
        self.queue.append(t)
        # Remove old pings from the queue
        while self.queue[len(self.queue) - 1] - self.queue[0] > 3000:
            self.queue.pop(0)

        # Return the size of the queue, which is the number of pings in the past 3000ms
        return len(self.queue)


import unittest

class TestRecentCounter(unittest.TestCase):
    def setUp(self):
        self.rc = RecentCounter()

    def test_single_ping(self):
        self.assertEqual(self.rc.ping(100), 1)

    def test_multiple_pings_within_3000ms(self):
        self.rc.ping(100)
        self.rc.ping(200)
        self.rc.ping(300)
        self.assertEqual(self.rc.ping(400), 4)

    def test_multiple_pings_outside_3000ms(self):
        self.rc.ping(100)
        self.rc.ping(4000)
        self.assertEqual(self.rc.ping(5000), 2)

    def test_ping_at_exact_3000ms_boundary(self):
        self.rc.ping(100)
        self.rc.ping(3100)
        self.assertEqual(self.rc.ping(3200), 2)

    def test_ping_at_negative_time(self):
        self.rc.ping(-100)
        self.assertEqual(self.rc.ping(100), 2)

if __name__ == '__main__':
    unittest.main()