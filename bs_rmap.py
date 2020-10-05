in1_sides = [round(chan.vals[0], 2) for chan in op('all_sides').chans('in1*')]
in2_sides = [round(chan.vals[0], 2) for chan in op('all_sides').chans('in2*')]
in3_sides = [round(chan.vals[0], 2) for chan in op('all_sides').chans('in3*')]

in_sides_list = [in1_sides, in2_sides, in3_sides]

ref_sides = [round(float(side.val), 2) for side in op('sides').col(0)]

# print('ref_sides', ref_sides)

for idx, in_sides in enumerate(in_sides_list):
    if ref_sides[0] in in_sides and ref_sides[2] in in_sides: 
        op('bs1').par.chop.val = f"bs_in_{idx + 1}"
    elif ref_sides[0] in in_sides and ref_sides[1] in in_sides:
        op('bs2').par.chop.val = f"bs_in_{idx + 1}"
    elif ref_sides[1] in in_sides and ref_sides[2] in in_sides:
        op('bs3').par.chop.val = f"bs_in_{idx + 1}"