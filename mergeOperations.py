import nuke

def operationUp():
    """Increase in 1 the operation value of the merge nodes."""
    updateOperation(1)

def operationDown():
    """Decrease in 1 the operation value of the merge nodes."""
    updateOperation(-1)

def updateOperation(opValue):
    """Updates the operation knob of the merge nodes currently selected.

    Args:
        opValue(int): Increment value to add to the operation knob.
    """
    valuesN = None
    for nodeObj in nuke.selectedNodes("Merge2"):
        if valuesN is None:
            nodeValues = nodeObj.knob("operation").values()
            valuesN = len(nodeValues)
        nodeObj.knob("operation").setValue(((int(nodeObj.knob("operation").getValue()) + opValue) % valuesN))