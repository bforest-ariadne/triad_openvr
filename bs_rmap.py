def remap_bs():
    in1_sides = [round(chan.vals[0], 2) for chan in op('all_sides').chans('in1*')]
    in2_sides = [round(chan.vals[0], 2) for chan in op('all_sides').chans('in2*')]
    in3_sides = [round(chan.vals[0], 2) for chan in op('all_sides').chans('in3*')]

    in_sides_list = [in1_sides, in2_sides, in3_sides]

    ref_sides = remove_dupes([round(chan.vals[0], 2) for chan in op('all_sides').chans('*')])
    ref_sides.sort()

    print('ref_sides', ref_sides)

    for idx, in_sides in enumerate(in_sides_list):
        if ref_sides[0] in in_sides and ref_sides[2] in in_sides: 
            op('bs1').par.chop.val = f"in{idx + 1}"
        elif ref_sides[0] in in_sides and ref_sides[1] in in_sides:
            op('bs2').par.chop.val = f"in{idx + 1}"
        elif ref_sides[1] in in_sides and ref_sides[2] in in_sides:
            op('bs3').par.chop.val = f"in{idx + 1}"

def remove_dupes(list_in):
    res = []
    [res.append(x) for x in list_in if x not in res] 
    return res


def onValueChange(channel, sampleIndex, val, prev):
    remap_bs()
    return