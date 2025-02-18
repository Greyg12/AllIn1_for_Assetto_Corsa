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

AppName = "InOne"

width, height = 525, 225
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
l_current_fuel = 0
current_fuel = 0
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
kilometers = 0.0
l_fuel_per_100km = 0.0
fuel_per_100km = 0.0
l_fuel_per_mile = 0.0
fuel_per_mile = 0.0
fuel_start = 0.0
fuel_used = 0.0


def acMain(ac_version):

    global l_completedLaps, l_kmh, l_mph, l_driver_name, driver_name, l_accelerator, l_brake, l_clutch, l_rpm, l_current_fuel, l_performance_meter, l_gear, l_turbo_boost, l_top_speed_kmh, l_top_speed_mph, l_lastlap, l_bestlap, l_laptime, l_position, l_lapPosition, l_fuel_per_mile, l_fuel_per_100km

    # Creating window for the app
    appWindow = ac.newApp(AppName)
    ac.setSize(appWindow, width, height)

    # Creating all needed labels for app
    l_kmh = ac.addLabel(appWindow, "0 km/h")
    ac.setPosition(l_kmh, pos_x, pos_y + 30)

    l_mph = ac.addLabel(appWindow, "0 mp/h")
    ac.setPosition(l_mph, pos_x, pos_y + 50)

    driver_name = ac.getDriverName(0)
    l_driver_name = ac.addLabel(appWindow, driver_name)
    driver_name_length = len(driver_name)
    middle_index = math.floor(driver_name_length / 2)
    center_x = (width / 2) - middle_index - (pos_x / 2)
    ac.setPosition(l_driver_name, center_x, pos_y)

    l_accelerator = ac.addLabel(appWindow, "0")
    ac.setPosition(l_accelerator, pos_x, pos_y + 70)

    l_brake = ac.addLabel(appWindow, "0")
    ac.setPosition(l_brake, pos_x, pos_y + 90)

    l_clutch = ac.addLabel(appWindow, "0")
    ac.setPosition(l_clutch, pos_x, pos_y + 110)

    l_gear = ac.addLabel(appWindow, "N")
    ac.setPosition(l_gear, pos_x, pos_y + 130)

    l_rpm = ac.addLabel(appWindow, "0")
    ac.setPosition(l_rpm, pos_x, pos_y + 150)
    ac.setFontColor(l_rpm, 1, 0, 0, 1)

    l_current_fuel = ac.addLabel(appWindow, "0")
    ac.setPosition(l_current_fuel, pos_x + 300, pos_y + 110)

    l_performance_meter = ac.addLabel(appWindow, "0")
    ac.setPosition(l_performance_meter, pos_x + 300, pos_x + 90)

    l_turbo_boost = ac.addLabel(appWindow, "0")
    ac.setPosition(l_turbo_boost, pos_x + 130, pos_y + 130)

    l_top_speed_kmh = ac.addLabel(appWindow, "0")
    ac.setPosition(l_top_speed_kmh, pos_x + 130, pos_y + 90)

    l_top_speed_mph = ac.addLabel(appWindow, "0")
    ac.setPosition(l_top_speed_mph, pos_x + 130, pos_y + 110)

    l_lastlap = ac.addLabel(appWindow, "00:00.0")
    ac.setPosition(l_lastlap, pos_x + 130, pos_y + 50)

    l_bestlap = ac.addLabel(appWindow, "00:00.0")
    ac.setPosition(l_bestlap, pos_x + 130, pos_y + 70)

    l_laptime = ac.addLabel(appWindow, "00:00.0")
    ac.setPosition(l_laptime, pos_x + 130, pos_y + 30)

    l_position = ac.addLabel(appWindow, "0")
    ac.setPosition(l_position, pos_x + 300, pos_y + 30)

    l_lapPosition = ac.addLabel(appWindow, "0")
    ac.setPosition(l_lapPosition, pos_x + 300, pos_y + 70)

    l_completedLaps = ac.addLabel(appWindow, "0")
    ac.setPosition(l_completedLaps, pos_x + 300, pos_y + 50)

    l_fuel_per_100km = ac.addLabel(appWindow, "Fuel usage: 0.00 l/100 km")
    ac.setPosition(l_fuel_per_100km, pos_x + 300, pos_y + 130)

    l_fuel_per_mile = ac.addLabel(appWindow, "Fuel usage: 0.00 mpg")
    ac.setPosition(l_fuel_per_mile, pos_x + 300, pos_y + 150)

    return AppName

def acUpdate(deltaT):
    global kilometers, completedLaps, kmh, mph, accelerator,  gear, brake, clutch, rpm, performance_meter, current_fuel, turbo_boost, top_speed_kmh, top_speed_mph, top_speed_mph, lastlap, bestlap,  laptime, last_minutes, last_seconds, best_minutes, best_seconds, lap_minutes, lap_seconds, position,  lapPosition, fuel_per_100km, fuel_per_mile, fuel_used, fuel_start

    # Speed
    kmh = ac.getCarState(0, acsys.CS.SpeedKMH)
    mph = ac.getCarState(0, acsys.CS.SpeedMPH)
    ac.setText(l_kmh, "{} km/h".format(int(kmh)))
    ac.setText(l_mph, "{} mp/h".format(int(mph)))

    # Inputs
    accelerator = int(ac.getCarState(0, acsys.CS.Gas) * 100)
    brake = int(ac.getCarState(0, acsys.CS.Brake) * 100)
    clutch = 100 - int(ac.getCarState(0, acsys.CS.Clutch) * 100)
    ac.setText(l_brake, "Brake: {}".format(int(brake)))
    ac.setText(l_accelerator, "Throttle: {}".format(int(accelerator)))
    ac.setText(l_clutch, "Clutch: {}".format(int(clutch)))

    # Gears
    gear = info.physics.gear
    gear_text = "N" if gear == 1 else "R" if gear == 0 else str(gear - 1)
    ac.setText(l_gear, gear_text)

    # Engine rpm
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

    # Fuel
    current_fuel = round(info.physics.fuel, 2)
    if current_fuel <= 5:
        ac.setFontColor(l_current_fuel, 1, 0, 0, 1)
    ac.setText(l_current_fuel, "Fuel left: {} l".format(current_fuel))

    # Turbo and distance
    kilometers = round(info.graphics.distanceTraveled / 1000, 2)
    turbo_boost = round(ac.getCarState(0, acsys.CS.TurboBoost), 1)
    ac.setText(l_performance_meter, "Session distance: {:.2f} km".format(kilometers))
    ac.setText(l_turbo_boost, "{} psi".format(turbo_boost))

    # Lap times
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

    # Highest speed
    if kmh > top_speed_kmh:
        top_speed_kmh = kmh
        ac.setText(l_top_speed_kmh, "Top speed: {} km/h".format(int(top_speed_kmh)))
    if mph > top_speed_mph:
        top_speed_mph = mph
        ac.setText(l_top_speed_mph, "Top speed: {} mph".format(int(top_speed_mph)))

    # Position, Lap % and completed Laps
    position = info.graphics.position
    position_suffix = "st" if position % 10 == 1 else "nd" if position % 10 == 2 else "rd" if position % 10 == 3 else "th"
    if position == 1 or position == 21 or position == 31 or position == 41 or position == 51:
        ac.setText(l_position, "Pos. {} {}".format(position, position_suffix))
    elif position == 1 or position == 22 or position == 32 or position == 42 or position == 52:
        ac.setText(l_position, "Pos. {} {}".format(position, position_suffix))
    elif position == 3 or position == 23 or position == 33 or position == 43 or position == 53:
        ac.setText(l_position, "Pos. {} {}".format(position, position_suffix))
    else:
        ac.setText(l_position, "Pos. {} {}".format(position, position_suffix))

    lapPosition = info.graphics.normalizedCarPosition * 100
    ac.setText(l_lapPosition, "Lap percent: {}%".format(int(lapPosition)))

    totalLaps = info.graphics.numberOfLaps
    if totalLaps == 0:
        totalLaps = "--"
    completedLaps = info.graphics.completedLaps
    ac.setText(l_completedLaps, "Lap Nr: {}/{}".format(completedLaps + 1, totalLaps))

    # Fuel consumption
    if fuel_start == 0.0:
        fuel_start = round(info.physics.fuel, 2)
    fuel_used = round(fuel_start - current_fuel, 2)

    if kilometers > 0:
        fuel_per_100km = round((fuel_used / kilometers) * 100, 2)
    else:
        fuel_per_100km = 0.00

    miles = kilometers * 0.621371
    gallons_used = fuel_used / 3.78541
    if miles > 0:
        fuel_per_mile = round(miles / gallons_used, 2)
    else:
        fuel_per_mile = 0.00

    if fuel_start < current_fuel:
        fuel_start = current_fuel

    ac.setText(l_fuel_per_100km, "Fuel usage: {:.2f} l/100 km".format(fuel_per_100km))
    ac.setText(l_fuel_per_mile, "Fuel usage: {:.2f} mpg".format(fuel_per_mile))