import math
import ac
import time
import sys
import acsys
from third_party.sim_info import *
import os
import platform
if platform.architecture()[0] == "64bit":
    libdir = 'third_party/lib64'
else:
    libdir = 'third_party/lib'
sys.path.insert(0, os.path.join(os.path.dirname(__file__), libdir))
os.environ['PATH'] = os.environ['PATH'] + ";."

from third_party.sim_info import info


appName = "AllIn1"
width, height = 525, 260
pos_x, pos_y = 30, 30

l_kmh = 0
kmh = 0
l_mph = 0
mph = 0
driver_name = 0
l_driver_name = 0
l_accelerator = 0
accelerator = 0
l_brake = 0
brake = 0
l_clutch = 0
clutch = 0
l_gear = 0
gear = 0
l_rpm = 0
rpm = 0
l_actual_fuel = 0
actual_fuel = 0
l_performance_meter = 0
performance_meter = 0
l_turbo_boost = 0
turbo_boost = 0
l_top_speed_kmh = 0
top_speed_kmh = 0
l_top_speed_mph = 0
top_speed_mph = 0
l_lastlap = 0
lastlap = 0
l_bestlap = 0
bestlap = 0
l_laptime = 0
laptime = 0
last_minutes = 0
last_seconds = 0
best_minutes = 0
best_seconds = 0
lap_minutes = 0
lap_seconds = 0
l_position = 0
position = 0
l_lapPosition = 0
lapPosition = 0
l_completedLaps = 0
completedLaps = 0
kilometry = 0.00001


def acMain(ac_version):

    global l_completedLaps, l_kmh, l_mph, l_driver_name, driver_name, l_accelerator, l_brake, l_clutch, l_rpm, l_actual_fuel, l_performance_meter, l_gear, l_turbo_boost, l_top_speed_kmh, l_top_speed_mph, l_avearge_speed, l_lastlap, l_bestlap, l_laptime, l_position, l_lapPosition

    appWindow = ac.newApp(appName)
    ac.setSize(appWindow, width, height)

    ac.log("Hello, Assetto Corsa application world!")
    ac.console("Hello, Assetto Corsa console!")

    l_kmh = ac.addLabel(appWindow, "0 km/h");
    ac.setPosition(l_kmh, pos_x, pos_y + 30)

    l_mph = ac.addLabel(appWindow, "0 mp/h");
    ac.setPosition(l_mph, pos_x, pos_y + 50)

    driver_name = ac.getDriverName(0)
    l_driver_name = ac.addLabel(appWindow, driver_name)
    driver_name_length = len(driver_name)
    middle_index = math.floor(driver_name_length / 2)
    center_x = (width / 2) - middle_index - (pos_x / 2)
    ac.setPosition(l_driver_name, center_x, pos_y)

    l_accelerator = ac.addLabel(appWindow, "0");
    ac.setPosition(l_accelerator, pos_x, pos_y + 70)

    l_brake = ac.addLabel(appWindow, "0");
    ac.setPosition(l_brake, pos_x, pos_y + 90)

    l_clutch = ac.addLabel(appWindow, "0");
    ac.setPosition(l_clutch, pos_x, pos_y + 110)

    l_gear = ac.addLabel(appWindow, "N");
    ac.setPosition(l_gear, pos_x, pos_y + 130)

    l_rpm = ac.addLabel(appWindow, "0");
    ac.setPosition(l_rpm, pos_x, pos_y + 150)
    ac.setFontColor(l_rpm, 1, 0, 0, 1)

    l_actual_fuel = ac.addLabel(appWindow, "0");
    ac.setPosition(l_actual_fuel, pos_x, pos_y + 190)

    l_performance_meter = ac.addLabel(appWindow, "0");
    ac.setPosition(l_performance_meter, pos_x + 300, pos_x + 90)

    l_turbo_boost = ac.addLabel(appWindow, "0");
    ac.setPosition(l_turbo_boost, pos_x, pos_y + 170)

    l_top_speed_kmh = ac.addLabel(appWindow, "0");
    ac.setPosition(l_top_speed_kmh, pos_x + 130, pos_y + 90)

    l_top_speed_mph = ac.addLabel(appWindow, "0");
    ac.setPosition(l_top_speed_mph, pos_x + 130, pos_y + 110)

    l_lastlap = ac.addLabel(appWindow, "00:00.0");
    ac.setPosition(l_lastlap, pos_x + 130, pos_y + 50)

    l_bestlap = ac.addLabel(appWindow, "00:00.0");
    ac.setPosition(l_bestlap, pos_x + 130, pos_y + 70)

    l_laptime = ac.addLabel(appWindow, "00:00.0");
    ac.setPosition(l_laptime, pos_x + 130, pos_y + 30)

    l_position = ac.addLabel(appWindow, "0");
    ac.setPosition(l_position, pos_x + 300, pos_y + 30)

    l_lapPosition = ac.addLabel(appWindow, "0");
    ac.setPosition(l_lapPosition, pos_x + 300, pos_y + 70)

    l_completedLaps = ac.addLabel(appWindow, "0");
    ac.setPosition(l_completedLaps, pos_x + 300, pos_y + 50)

    return appName

def acUpdate(deltaT):
    global totalLaps, kilometry, completedLaps, l_completedLaps, l_kmh, kmh, l_mph, mph, l_accelerator, accelerator, l_actual_fuel, l_gear, gear, l_performance_meter, brake, clutch, rpm, performance_meter, actual_fuel, l_actual_fuel, l_turbo_boost, turbo_boost, l_top_speed_kmh, top_speed_kmh, top_speed_mph, top_speed_mph, l_lastlap, lastlap, l_bestlap, bestlap, l_laptime, laptime, last_minutes, last_seconds, best_minutes, best_seconds, lap_minutes, lap_seconds, position, l_position, l_lapPosition, lapPosition

    kmh = ac.getCarState(0, acsys.CS.SpeedKMH)
    ac.setText(l_kmh, "{} km/h".format(int(kmh)))

    mph = ac.getCarState(0, acsys.CS.SpeedMPH)
    ac.setText(l_mph, "{} mp/h".format(int(mph)))

    accelerator = ac.getCarState(0, acsys.CS.Gas)
    accelerator *= 100
    ac.setText(l_accelerator, "Throttle: {}".format(int(accelerator)))

    brake = ac.getCarState(0, acsys.CS.Brake)
    brake *= 100
    ac.setText(l_brake, "Brake: {}".format(int(brake)))

    clutch = ac.getCarState(0, acsys.CS.Clutch)
    clutch *= 100
    invert_clutch = 100 - clutch
    ac.setText(l_clutch, "Clutch: {}".format(int(invert_clutch)))

    gear = info.physics.gear
    if gear == 1:
        gear_text = "N"
    elif gear == 0:
        gear_text = "R"
    else:
        gear_text = str(gear - 1)

    ac.setText(l_gear, "{}".format(gear_text))

    rpm = ac.getCarState(0, acsys.CS.RPM)
    if rpm >= info.static.maxRpm * 0.95:
        ac.setFontColor(l_gear, 1, 0, 0, 1)
        ac.setFontColor(l_rpm, 1, 0, 0, 1)
    elif rpm >= info.static.maxRpm * 0.85:
        ac.setFontColor(l_rpm, 1, 1, 0, 1)
        ac.setFontColor(l_gear, 1, 1, 1, 1)
    else:
        ac.setFontColor(l_rpm, 1, 1, 1, 1)
        ac.setFontColor(l_gear, 1, 1, 1, 1)

    ac.setText(l_rpm, "{} rpm".format(int(rpm)))

    actual_fuel = info.physics.fuel
    if actual_fuel <= 5:
        ac.setFontColor(l_actual_fuel, 1, 0, 0, 1)
    rounded_fuel = round(actual_fuel, 2)
    ac.setText(l_actual_fuel, "Fuel left: {} l".format(rounded_fuel))


    performance_meter = info.graphics.distanceTraveled
    kilometry = performance_meter / 1000
    ac.setText(l_performance_meter, "Session distance: {:.2f} km".format(kilometry))

    turbo_boost = ac.getCarState(0, acsys.CS.TurboBoost)
    turbo_rounded = round(turbo_boost, 1)
    ac.setText(l_turbo_boost, "{} psi".format(turbo_rounded))

    lastlap = ac.getCarState(0, acsys.CS.LastLap)
    last_minutes = int(lastlap / 60000)
    last_seconds = int((lastlap % 60000) / 1000)
    ac.setText(l_lastlap, "Last: {}:{}.{}".format(last_minutes, last_seconds, int(lastlap % 1000)))

    bestlap = ac.getCarState(0, acsys.CS.BestLap)
    best_minutes = int(bestlap / 60000)
    best_seconds = int((bestlap % 60000) / 1000)
    ac.setText(l_bestlap, "Best: {}:{}.{}".format(best_minutes, best_seconds, int(bestlap % 1000)))

    laptime = ac.getCarState(0, acsys.CS.LapTime)
    lap_minutes = int(laptime / 60000)
    lap_seconds = int((laptime % 60000) / 1000)
    if lap_seconds < 10:
        ac.setText(l_laptime, "LapTime: {}:0{}.{}".format(lap_minutes, lap_seconds, int(laptime % 1000)))
    else:
        ac.setText(l_laptime, "LapTime: {}:{}.{}".format(lap_minutes, lap_seconds, int(laptime % 1000)))

    if last_seconds < 10:
        ac.setText(l_lastlap, "Last: {}:0{}.{}".format(last_minutes, last_seconds, int(lastlap % 1000)))
    else:
        ac.setText(l_lastlap, "Last: {}:{}.{}".format(last_minutes, last_seconds, int(lastlap % 1000)))

    if best_seconds < 10:
        ac.setText(l_bestlap, "Best: {}:0{}.{}".format(best_minutes, best_seconds, int(bestlap % 1000)))
    else:
        ac.setText(l_bestlap, "Best: {}:{}.{}".format(best_minutes, best_seconds, int(bestlap % 1000)))


    if(kmh > top_speed_kmh):
        top_speed_kmh = kmh
        ac.setText(l_top_speed_kmh, "Top speed: {} km/h".format(int(top_speed_kmh)))

    if (mph > top_speed_mph):
        top_speed_mph = mph
        ac.setText(l_top_speed_mph, "Top speed: {} mph".format(int(top_speed_mph)))

    position = info.graphics.position
    if position == 1 or position == 21 or position == 31 or position == 41 or position == 51:
        ac.setText(l_position, "Pos. {} st".format(position))
    elif position == 1 or position == 22 or position == 32 or position == 42 or position == 52:
        ac.setText(l_position, "Pos. {} nd".format(position))
    elif position == 3 or position == 23 or position == 33 or position == 43 or position == 53:
        ac.setText(l_position, "Pos. {} rd".format(position))
    else:
        ac.setText(l_position, "Pos. {} th".format(position))

    lapPosition = info.graphics.normalizedCarPosition * 100
    ac.setText(l_lapPosition, "Lap percent: {}%".format(int(lapPosition)))

    totalLapsValue = info.graphics.numberOfLaps
    totalLaps = totalLapsValue
    if totalLaps == 0:
        totalLaps = "--"
    completedLaps = info.graphics.completedLaps
    ac.setText(l_completedLaps, "Lap Nr: {}/{}".format(completedLaps + 1, totalLaps))#ilosc wszystkich