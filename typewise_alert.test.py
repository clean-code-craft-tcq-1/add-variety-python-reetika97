import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
  #tests for infers_breach
  def test_infers_breach_as_per_limits(self):
    self.assertTrue(typewise_alert.infer_breach(20, 50, 100) == 'TOO_LOW')
  def test_infers_breach_as_per_limits(self):
    self.assertTrue(typewise_alert.infer_breach(50, 50, 100) == 'NORMAL')
  def test_infers_breach_as_per_limits(self):
    self.assertTrue(typewise_alert.infer_breach(101, 50, 100) == 'TOO_HIGH')


if __name__ == '__main__':
  unittest.main()
