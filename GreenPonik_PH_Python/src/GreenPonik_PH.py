"""
####################################################################
####################################################################
####################################################################
################ GreenPonik Read PH through Python3 ################
####################################################################
####################################################################
####################################################################
Based on DFRobot_PH library
https://github.com/DFRobot/DFRobot_PH/tree/master/RaspberryPi/Python

Need DFRobot_ADS1115 library
https://github.com/DFRobot/DFRobot_ADS1115/tree/master/RaspberryPi/Python
"""
import time

# _temperature      = 25.0
# pH 4.0
_acidVoltage = 2032.44
# pH 7.0
_neutralVoltage = 1500.0


class GreenPonik_PH():
    def begin(self):
        global _acidVoltage
        global _neutralVoltage
        try:
            print(">>>Initialization of ph lib<<<")
            with open('phdata.txt', 'r') as f:
                neutralVoltageLine = f.readline()
                neutralVoltageLine = neutralVoltageLine.strip(
                    'neutralVoltage=')
                _neutralVoltage = float(neutralVoltageLine)
                print("get neutral voltage from txt file: %d" %
                      _neutralVoltage)
                acidVoltageLine = f.readline()
                acidVoltageLine = acidVoltageLine.strip('acidVoltage=')
                _acidVoltage = float(acidVoltageLine)
                print("get acid voltage from txt file: %d" % _acidVoltage)
        except:
            self.reset()

    # def readPH(self,voltage,temperature):
    def readPH(self, voltage):
        global _acidVoltage
        global _neutralVoltage
        slope = (7.0-4.0)/((_neutralVoltage-1500.0) /
                           3.0 - (_acidVoltage-1500.0)/3.0)
        intercept = 7.0 - slope*(_neutralVoltage-1500.0)/3.0
        _phValue = slope*(voltage-1500.0)/3.0+intercept
        return round(_phValue, 2)

    def calibration(self, voltage):
        if (voltage > 1322 and voltage < 1678):
            print(">>>Buffer Solution:7.0")
            f = open('phdata.txt', 'r+')
            flist = f.readlines()
            flist[0] = 'neutralVoltage=' + str(voltage) + '\n'
            f = open('phdata.txt', 'w+')
            f.writelines(flist)
            f.close()
            status_msg = ">>>PH:7.0 Calibration completed,Please enter Ctrl+C exit calibration in 5 seconds"
            print(
                ">>>PH:7.0 Calibration completed,Please enter Ctrl+C exit calibration in 5 seconds")
            time.sleep(5.0)
            cal_res = {'status': 7, 'status_message': status_msg}
            return cal_res
        elif (voltage > 1854 and voltage < 2210):
            print(">>>Buffer Solution:4.0")
            f = open('phdata.txt', 'r+')
            flist = f.readlines()
            flist[1] = 'acidVoltage=' + str(voltage) + '\n'
            f = open('phdata.txt', 'w+')
            f.writelines(flist)
            f.close()
            status_msg = ">>>PH:4.0 Calibration completed,Please enter Ctrl+C exit calibration in 5 seconds"
            print(status_msg)
            time.sleep(5.0)
            cal_res = {'status': 4, 'status_message': status_msg}
            return cal_res
        else:
            status_msg = ">>>Buffer Solution Error Try Again<<<"
            print(status_msg)
            cal_res = {'status': 9999, 'status_message': status_msg}
            return cal_res

    def reset(self):
        global _acidVoltage
        global _neutralVoltage
        _acidVoltage = 2032.44
        _neutralVoltage = 1500.0
        print(">>>Reset to default parameters<<<")
        try:
            print(">>>Read voltages from txt files<<<")
            f = open('phdata.txt', 'r+')
            flist = f.readlines()
            flist[0] = 'neutralVoltage=' + str(_neutralVoltage) + '\n'
            flist[1] = 'acidVoltage=' + str(_acidVoltage) + '\n'
            f = open('phdata.txt', 'w+')
            f.writelines(flist)
            f.close()
            print(">>>Reset to default parameters<<<")
        except:
            print(">>>Cannot read voltages from txt files<<<")
            print(">>>Let's create them and apply the default values<<<")
            f = open('phdata.txt', 'w')
            flist = 'neutralVoltage=' + str(_neutralVoltage) + '\n'
            flist += 'acidVoltage=' + str(_acidVoltage) + '\n'
            f.writelines(flist)
            f.close()
