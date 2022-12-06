import nuke

def operationUp():
    """Increase in 1 the operation value of the merge nodes."""
    updateOperation(1)

def operationDown():
    """Decrease in 1 the operation value of the merge nodes."""
    updateOperation(-1)

def checkNodes(nodes, opValue):
    """Checks the given nodes and update the operation prop with the given value.

    Args:
        node (list): The list of nuke Nodes to check.
        opValue (int): Increment value to add to the operation knob.

    """
    valuesN = None
    for nodeObj in nodes:
        if valuesN is None:
            nodeValues = nodeObj.knob("operation").values()
            valuesN = len(nodeValues)
        nodeObj.knob("operation").setValue(((int(nodeObj.knob("operation").getValue()) + opValue) % valuesN))

def updateOperation(opValue):
    """Updates the operation knob of the merge nodes currently selected.

    Args:
        opValue (int): Increment value to add to the operation knob.
    """
    checkNodes(nuke.selectedNodes("Merge2"), opValue)
    checkNodes(nuke.selectedNodes("ChannelMerge"), opValue)


def installCommands():
    """Installs the commands in Nuke menu."""
    nuke.menu("Nodes").addCommand("Actions/mergeOpUp", "mergeOperations.operationUp()", 'ctrl+Up')
    nuke.menu("Nodes").addCommand("Actions/mergeOpDown", "mergeOperations.operationDown()", 'ctrl+Down')
