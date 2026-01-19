#R = (v₀² * sin(2θ)) / g
import math

def trajectory_range(velocity, angle):

    velocity = float(velocity)
    angle = float(angle)
    g = 9.81

    if angle <= 0 or angle >= 90:
        return "angle must be between 0 and 90"

    angle_radians = math.radians(2 * angle)
    angle_sin = math.sin(angle_radians)

    Range = (velocity**2 * angle_sin) / g
    return Range


v, ang = input("Enter velocity and angle: ").split()
print("Distance traveled: ", trajectory_range(v, ang))
