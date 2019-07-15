
old_position=100
initial_velocity=0
old_velocity=0
acceleration=10
old_fuel=100
gravity=-10
thrusters=0

new_fuel = old_fuel - thrusters
acceleration = gravity + thrusters
new_position = old_position + old_velocity + acceleration * 0.5
new_velocity = old_velocity + acceleration


while 1:
    if new_position<=0:
        print "Landing successful!"
        break
    elif new_position!=0:

        thrusters = input('Set thrusters(0-20): ')
        print(thrusters)
        new_fuel = old_fuel - thrusters
        acceleration = gravity + thrusters
        new_position = old_position+old_velocity+acceleration*0.5
        new_velocity = old_velocity+acceleration

        old_velocity=new_velocity
        old_fuel=new_fuel


        print "P: ", new_position, "V: ", new_velocity, "F: ", new_fuel