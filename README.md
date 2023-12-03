# Easy Mecademic Programming for Hyrel
## Setup
install mecademicpy (might already be installed)
```sh 
pip install mecademicpy
```
## Programming the mecademic robot
Any program that's written in the browser or mecademic portal can easily be converted into it's python equivalent
<code>Mecademic Browser 192.168.0.100</code>
```txt 
MoveJoints(90,0,0,0,0,0)
```

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
