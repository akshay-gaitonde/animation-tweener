import maya.cmds as cmds

def tween(percentage, obj=None,attrs=None,selection =True):

    #if obj is not given and selection is set to false, Error early
    if not obj and not selection:
        raise ValueError("No object id given to tween")

    #if no obj is specified ,get it from the first selection
    if not obj:
        obj=cmds.ls(selection=True)[0]

    if not attrs:
        attrs=cmds.listAttr(obj,keyable=True)

    currentTime=cmds.currentTime(query=True)

    for attr in attrs:


        #contruct the full name of the attribute with its object
        attrFull = '%s.%s' % (obj,attr)

        #get the keyframesof the attribute on this object
        keyframes = cmds.keyframe(attrFull,query=True)

        #if there are no key then continue
        if not keyframes:
            continue


        previousKeyFrames =[]
        for frame in keyframes:
            if frame < currentTime:
                previousKeyFrames.append(frame)


        laterKeyFrames = [frame for frame in keyframes if frame > currentTime]


        if not previousKeyFrames and not laterKeyFrames:
            continue


        if previousKeyFrames:
            previousFrame = max(previousKeyFrames)
        else:
            previousFrame = None

        nextFrame = min(laterKeyFrames) if laterKeyFrames else None


        if not previousFrame or not nextFrame:
            continue

        previousValue = cmds.getAttr(attrFull,time=previousFrame)
        nextValue = cmds.getAttr(attrFull,time=nextFrame)

        difference = nextValue - previousValue
        weightedDifference=(difference*percentage)/100
        currentValue = previousValue + weightedDifference

        #print difference, weightedDifference
        cmds.setKeyframe(attrFull,time=currentTime,value=currentValue)