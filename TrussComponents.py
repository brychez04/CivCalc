import math
class Joint:
    """
    CLASS Joint:
        -Describes a joint in a simple truss
        -Net forces on a joint must be in equilibrium
        -Members can freely rotate around joints, so net torque must also be in equilibrium
        -Extended by the Support class
    Fields:
        double x: X-position of joint
        double y: Y-position of joint
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Getters/Setters
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def __eq__(self, joint):
        if self.x == joint.x and self.y == joint.y:
            return True
        return False
    
    def __str__(self):
        return f"({self.x} {self.y})"

class Force:
    """
    CLASS Force:
        -Describes an external force on a simple truss.
        -Internal forces of members are not represented by this class

    Fields:
        double magnitude: Magnitude of force in newtons
        double direction: Direction of force in degrees. Assume 0 degrees is along the x-axis
    """

    def __init__(self, magnitude, direction):
        self.magnitude = magnitude
        self.direction = direction

    def getMagnitude(self):
        return self.magnitude

    def getDirection(self):
        return self.direction

    def getXMagnitude(self):
        return self.magnitude * math.sin(self.direction)

    def getYMagnitude(self):
        return self.magnitude * math.cos(self.direction)

    def setMagnitude(self, magnitude):
        self.magnitude = magnitude

    def setDirection(self, direction):
        self.direction = direction

    def positiveXDirection(self):
        if (0 < self.direction < 90) or (270 < self.direction < 360):
            return 1
        else:
            return -1

    def positiveYDirection(self):
        if 0 < self.direction < 180:
            return 1
        else:
            return -1

    def __str__(self):
        return f"Force of {self.magnitude}N at {self.direction} degrees"

    def __eq__(self, force):
        if self.direction == force.direction and self.magnitude == force.magnitude:
            return True
        return False

class Member:
    """
        -Describes a 2 joint member in a simple truss.
        -Will not experience external loads.
        -Forces perpendicular to a member will not affect the internal force of the member

    Fields:
        Joint joint1: First joint of member
        Joint joint2: Second joint of member
        double length: Length of member
        double internalForce: Internal force of member
        double internalForceX: X-component of internal force of member
        double internalForceY: Y-component of internal force of member
    """

    def __init__(self, joint1, joint2):
        self.joint1 = joint1
        self.joint2 = joint2
        self.length = math.dist([joint1.x, joint1.y], [joint2.x, joint2.y])
        self.internalForce = 0
        self.internalForceX = 0
        self.internalForceY = 0

    def inCompression(self):
        return self.internalForce < 0

    def inTension(self):
        return self.internalForce > 0

    def isZeroForceMember(self):
        return self.internalForce == 0

    # Getters/Setters
    def getJoint1(self):
        return self.joint1

    def getJoint2(self):
        return self.joint2

    def getLength(self):
        return self.length

    def getInternalForce(self):
        return self.internalForce

    def getInternalForceX(self):
        return self.internalForceX

    def getInternalForceY(self):
        return self.internalForceY

    def setJoint1(self, joint):
        self.joint1 = joint

    def setJoint2(self, joint):
        self.joint2 = joint

    def setLength(self, length):
        self.length = length

    def setInternalForce(self, force):
        self.internalForce = force

    def setInternalForceX(self, force):
        self.internalForceX = force

    def setInternalForceY(self, force):
        self.internalForceY = force

    def __str__(self):
        return f"Member {self.joint1.x}, {self.joint1.y} to {self.joint2.x}, {self.joint2.y}. Internal Forces:\n" \
                f" X: {self.internalForceX}, Y: {self.internalForceY}, Total: {self.internalForce}"

class Support(Joint):
    """
    CLASS Support:
        -Describes support joint
        -Extends Joint class
        -If roller connection, X reaction is 0.

    Fields:
        Inherits Joint fields
        boolean isRoller: Roller connection? If not, assumed to be a pin connection
    """

    def __init__(self, x, y, is_roller):
        super().__init__(x, y)
        self.isRoller = is_roller

    def isRoller(self):
        return self.isRoller

    def __str__(self):
        support_type = "Type: Roller" if self.isRoller(self) else "Type: Pin"
        return f"{super.__str__(self)} {support_type}"

    def __eq__(self, other):
        if super().__eq__(other):
            return True
        return False
