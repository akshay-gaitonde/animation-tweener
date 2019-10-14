import maya.cmds as cmds
import sys
sys.path.append("D:\\akshay\\script")
import tweenerUI



class BaseWindow(object):

    windowName = "BaseWindow"

    def show(self):

        if cmds.window(self.windowName, query=True, exists=True):
            cmds.deleteUI(self.windowName)

        cmds.window(self.windowName)
        self.buildUI()
        cmds.showWindow()


    def buildUI(self):
        column = cmds.columnLayout()
        cmds.text(label="this is base window")
        cmds.setParent(column)

        cmds.button(label="Close", command=self.close)
        print"hello"



    def reset(self,*args):
        pass

    def close(self,*args):
        cmds.deleteUI(self.windowName)


class TweenerUI(BaseWindow):

    windowName="TweenerWindow"
    def buildUI(self):
        column=cmds.columnLayout()

        cmds.text(label="Use this slider to set the tween amount")

        row=cmds.rowLayout(numberOfColumns=2)

        self.slider = cmds.floatSlider(min=0, max=100, value=50, step=1, changeCommand=tweenerUI.tween)
        cmds.button(label="Reset", command=self.reset)

        cmds.setParent(column)
        cmds.button(label="Close", command=self.close)


    def reset(self,*args):
        cmds.floatSlider(self.slider, edit= True, value=50)