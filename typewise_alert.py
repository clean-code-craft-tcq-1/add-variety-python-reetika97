batteryChar={'coolingType':'PASSIVE_COOLING'}
lowerLimit={'PASSIVE_COOLING':0,'HI_ACTIVE_COOLING':0,'MED_ACTIVE_COOLING':0, 'DEFAULT':0}
upperLimit={'PASSIVE_COOLING':35,'HI_ACTIVE_COOLING':45,'MED_ACTIVE_COOLING':40, 'DEFAULT':0}

def send_to_controller(breachType):
  header = 0xfeed
  print(f'{header}, {breachType}')
  return 'Sent_to_controller'

def send_to_console(breachType):
  print(f' The temprature is : {breachType}')
  return 'Sent_to_console'

def send_to_email(breachType):
  recepient = "a.b@c.com"
  if breachType == 'TOO_LOW':
    print(f'To: {recepient}')
    print('Hi, the temperature is too low')
  elif breachType == 'TOO_HIGH':
    print(f'To: {recepient}')
    print('Hi, the temperature is too high')
  return 'Sent_to_email'


alertTargets={'TO_CONTROLLER':send_to_controller,'TO_EMAIL':send_to_email,'TO_CONSOLE':send_to_console}


def infer_breach(value, lowerLimit, upperLimit):
  if value < lowerLimit:
    return 'TOO_LOW'
  if value > upperLimit:
    return 'TOO_HIGH'
  return 'NORMAL'


def classify_temperature_breach(coolingType, temperatureInC):
  return infer_breach(temperatureInC, lowerLimit[coolingType], upperLimit[coolingType])


def check_and_alert(alertTarget, batteryChar, temperatureInC):
  breachType =\
    classify_temperature_breach(batteryChar['coolingType'], temperatureInC)
  return alertTargets[alertTarget](breachType)

