# me - this DAT
# scriptOp - the OP which is cooking
#
# press 'Setup Parameters' in the OP to call this function to re-create the parameters.
def onSetupParameters(scriptOp):
    return

# called whenever custom pulse parameter is pushed
def onPulse(par):
    return

def onCook(scriptOp):
    # scriptOp.clear()

    scriptOp.copy(scriptOp.inputs[0])	# no need to call .clear() above when copying
    #scriptOp.insertRow(['color', 'size', 'shape'], 0)
    #scriptOp.appendRow(['red', '3', 'square'])
    #scriptOp[1,0] += '**'

    scriptOp.appendRow(['top_right_to_bs', '', ''])
    # bs_

    return
