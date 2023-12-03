import mecademicpy.robot

#class for the SOP16 component (2 sets of 8 terminals)
class BGA:
    def __init__(self, robot):
        self.rbt = robot

    
    def pressButton(self):
        #RESET ROBOT
        self.rbt.SetJointVel(100)
        self.rbt.MoveJoints(90,0,0,0,0,-90)
        self.rbt.MoveJoints(89.60276,58.61276,-9.38405,2.50345,-47.11293,-90)
        
        #right above, change position to boop
        self.rbt.MoveJoints(89.60534,67.08336,-11.71448,2.29293,-53.24948,-90.81724)
        ## OLD, USES RUBBER ## self.rbt.MoveJoints(89.60276,61.97767,-9.49086,2.3819,-50.36845,2.17414)
        #boop active, wait a minute
        # self.rbt.Delay(.25)
        # self.rbt.SetJointVel(100)
        # self.rbt.MoveLinRelWrf(0,0,20,0,0,0)
        # #now go up robo loser
        # self.rbt.MoveJoints(90.93181,43.23,9.86819,2.6519,-50.89707,2.07069)
        print("button pressed")
    
    def grabComp(self):
        #test
        self.rbt.MoveJoints(90.93181,43.23,9.86819,2.6519,-50.89707,2.07069)
        self.rbt.SetJointVel(50) #OPTIONAL
        #is right above, going to grab.
        #########################################################
        ##TODO: FIX PART PICKUP SO ITS MORE RELIABLE (In hashes)
        #########################################################
        # self.rbt.MoveJoints(91.31767,55.46922,8.52491,1.455,-64.0169,-0.63448) #TOO LIGHT
        self.rbt.MoveJoints(90.71302,55.30112,7.22405,2.10569,-60.31603,2.69224) #PRESSURE
        #########################################################
        self.rbt.SetJointVel(10)
        self.rbt.SetValveState(1, 0)
        self.rbt.Delay(1)
        ##Comment after to keep nozzle down #######################################################
        #picked up, go straight up
        self.rbt.MoveJoints(91.17724,35.84328,3.16138,1.86983,-39.02017,-1.45259)
        #gone straight up, now get ready to flux.
        self.rbt.MoveJoints(91.17724,31.55871,-9.98664,3.19759,-21.61345,-2.97069)
        self.rbt.SetJointVel(50)
        # raised up even more
        print("component grabbed")

    def flux(self):
        #150mm tall flux bowl
        self.rbt.MoveJoints(33.18802,42.92302,-28.72009,-80.88207,-57.96,73.17414)
        # flux up
        self.rbt.MoveJoints(33.19733,46.45371,-10.92569,-69.19241,-63.55914,49.5301750) #LIGHT
        # self.rbt.MoveJoints(33.18828,46.93759,-10.29078,-68.67362,-63.95845,48.36638) #PRESS IN
        # we in the flux rn
        self.rbt.Delay(.5)
        # small delay
        self.rbt.MoveJoints(33.18802,42.92302,-28.72009,-80.88207,-57.96,73.17414)
        # flux in the air
        print("component fluxxed")

    def preheat(self):
        # self.rbt.MoveJoints()
        # self.rbt.MoveJoints()
        # self.rbt.MoveJoints()
        # self.rbt.MoveJoints()
        # self.rbt.MoveJoints()
        # self.rbt.MoveJoints()
        # self.rbt.MoveJoints()
        # self.rbt.MoveJoints()
        print("preheat done")

    def solder(self):
        print("solder process started")
        self.rbt.SetJointVel(25)
        self.rbt.MoveJoints(40.37664,23.93302,8.49233,57.76707,-49.99241,-45.55948)
        self.rbt.SetJointVel(50)#could change
        # pivoted
        #self.rbt.MoveJoints(10.90112,26.96379,25.05879,13.72914,-52.83621,-8.39483)
        self.rbt.MoveJoints(14.51741,27.83405,23.48612,18.7769,-52.26,-32.6431)
        ## NEW ANGLE, -2 Z ## self.rbt.MoveJoints(14.51017,28.05698,23.64853,18.45776,-53.38086,-27.75862)
        # self.rbt.SetJointVel(5)
        # knock knock, at solder
        #you might want it to be slower
        self.rbt.SetCartLinVel(20)
        self.rbt.MoveLinRelWrf(0, 0, -1.5, 0, 0, 0) #normally 3.5
        self.rbt.MoveLinRelWrf(0 , -60, 0, 0, 0, 0) # normally only -60
        # self.rbt.SetCartLinVel(20)
        # self.rbt.MoveLinRelWrf(0 , -15, 0, 0, 0, 0)
        # shimmy through solder
        self.rbt.SetJointVel(75)#variable
        self.rbt.MoveJoints(-12.62612,21.78621,18.6975,-19.03603,-42.09155,14.36638)
        # up after solder
        print("solder process done")

    def drop(self):
        self.rbt.MoveJoints(-12.62612,21.78621,18.6975,-19.03603,-42.09155,14.36638)
        self.rbt.SetCartLinVel(300)
        self.rbt.MoveLinRelWrf(0 , -135, 0, 0, 0, 0)
        # testing the waters
        print("valves turned off")
        self.rbt.SetValveState(0, 0)  
        ## REMOVED TO OPTIMIZE ## self.rbt.Delay(.5)
        #turnoff of valve, going to bump part off
        #########################################################
        #TODO: Change drop process so its less awkward and more reliable
        #Location of bump should change, "cardboard" position change
        #consider fixing the "cardboard" with tape
        #consider adding negative x to MoveLn RelWrf to be closer to the plate. 
        #########################################################
        ##OLD##self.rbt.MoveJoints(-58.40948,59.00793,-52.23078,-85.83879,-58.67224,82.05517)
        # self.rbt.MoveJoints(-58.51552,68.82259,-71.96121,-91.34845,-58.87966,92.94828)
        #up (OPTIONAL)
        self.rbt.MoveJoints(-58.51578,61.57293,-51.12905,-83.2169,-59.52776,77.14052)
        #down
        self.rbt.MoveJoints(-58.51552,68.82259,-71.96121,-91.34845,-58.87966,92.94828)
        #up
        self.rbt.SetJointVel(100)
        self.rbt.Delay(.5) 
        # plop  
        self.rbt.MoveJoints(90,0,0,0,0,-90)
        #return to starts
        print("component done, dropped in cleaner.")
        