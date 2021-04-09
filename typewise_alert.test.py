import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
  #tests for infers_breach
  def test_infers_breach_as_per_limits_L(self):
    self.assertTrue(typewise_alert.infer_breach(20, 50, 100) == 'TOO_LOW')
  def test_infers_breach_as_per_limits_N(self):
    self.assertTrue(typewise_alert.infer_breach(50, 50, 100) == 'NORMAL')
  def test_infers_breach_as_per_limits_H(self):
    self.assertTrue(typewise_alert.infer_breach(101, 50, 100) == 'TOO_HIGH')
  
  #Classifies per PASSIVE_COOLING
  def test_PASSIVE_COOLING_as_per_limits_L(self):  
    self.assertTrue(typewise_alert.classify_temperature_breach('PASSIVE_COOLING', -1) == 'TOO_LOW')
  def test_PASSIVE_COOLING_as_per_limits_H(self):
    self.assertTrue(typewise_alert.classify_temperature_breach('PASSIVE_COOLING', 36) == 'TOO_HIGH')
  def test_PASSIVE_COOLING_as_per_limits_N(self):
    self.assertTrue(typewise_alert.classify_temperature_breach('PASSIVE_COOLING', 30) == 'NORMAL')
    
  #Classifies per HI_ACTIVE_COOLING
  def test_HI_ACTIVE_COOLING_as_per_limits_L(self):  
    self.assertTrue(typewise_alert.classify_temperature_breach('HI_ACTIVE_COOLING', -1) == 'TOO_LOW')
  def test_HI_ACTIVE_COOLING_as_per_limits_H(self):
    self.assertTrue(typewise_alert.classify_temperature_breach('HI_ACTIVE_COOLING', 46) == 'TOO_HIGH')
  def test_HI_ACTIVE_COOLING_as_per_limits_N(self):
    self.assertTrue(typewise_alert.classify_temperature_breach('HI_ACTIVE_COOLING', 36) == 'NORMAL')
    
  #Classifies per MED_ACTIVE_COOLING
  def test_MED_ACTIVE_COOLING_as_per_limits_L(self):  
    self.assertTrue(typewise_alert.classify_temperature_breach('MED_ACTIVE_COOLING', -1) == 'TOO_LOW')
  def test_MED_ACTIVE_COOLING_as_per_limits_H(self):
    self.assertTrue(typewise_alert.classify_temperature_breach('MED_ACTIVE_COOLING', 41) == 'TOO_HIGH')
  def test_MED_ACTIVE_COOLING_as_per_limits_N(self):
    self.assertTrue(typewise_alert.classify_temperature_breach('MED_ACTIVE_COOLING', 36) == 'NORMAL')
    
  #Sends message as per alertTarget
  def test_sent_to_controller(self):  
    self.assertTrue(typewise_alert.check_and_alert('TO_CONTROLLER', {'coolingType':'MED_ACTIVE_COOLING'}, 50) == 'Sent_to_controller')
  def test_sent_to_email(self):  
    self.assertTrue(typewise_alert.check_and_alert('TO_EMAIL', {'coolingType':'MED_ACTIVE_COOLING'}, 50) == 'Sent_to_email')
  def test_sent_to_console(self):  
    self.assertTrue(typewise_alert.check_and_alert('TO_CONSOLE', {'coolingType':'MED_ACTIVE_COOLING'}, 50) == 'Sent_to_console')
    

if __name__ == '__main__':
  unittest.main()
