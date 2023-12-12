# Easy Mecademic Programming for Hyrel
## The Process of Robot Programming
1) Make the robot code with the Mecademic Portal (self explanatory)
     - make a final version that can run the correct part nicely
3) Convert robot script into python code (see below)
4) Send it to Danny for review :)
## Setup
install mecademicpy (might already be installed)
```sh 
pip install mecademicpy
```
## Programming the mecademic robot
Any program that's written in the browser or mecademic portal can easily be converted into it's python equivalent <br/> 
<code>Robot Script (192.168.0.100)</code>
```txt 
MoveJoints(90,0,0,0,0,0)
```
This is the equivalent code in the correct location: <br /> 
<code>EDITTHIS.py</code>
```python
class TemplateClass:
...
    def pressButton(self):
        ##########################################################################################
        # FIRST BLOCK EXECTUED BY main.py
        ##########################################################################################
        self.rbt.MoveJoints(90,0,0,0,0,0)
...
```
Notes:
- each method is there only for organization purposes.
- the \_\_init\_\_(...) method should not have any instructions
- Yes, all you need to do add "self.rbt." to make it into valid python code

## Using the Vacuum Sensor
The vacuum sensor is meant to confirm that a part is either on or off the robot at a specific stage. The two most useful commands are:
<code>Python</code>
```py
# Assert that the robot should have a part ON at the moment. Otherwise, the robot will stop movement. 
self.switch.assert_on()
# Asserts that there should be no part on. Same effect as the other method.
self.switch.assert_off()
```
