import argparse

def main(args):
    regs = {}
    def get_val(reg):
        if not reg in regs:
            regs[reg] = 0
        return regs[reg]
    max_val = 0

    with open(args.path, 'r') as f:
        for line in f:
            mod_reg, mod_op, mod_val, _, cond_reg, cond_op, cond_val = line.split()
            cond_reg_val = get_val(cond_reg)
            if cond_op == '>':
                cond = cond_reg_val > int(cond_val)
            elif cond_op == '==':
                cond = cond_reg_val == int(cond_val)
            elif cond_op == '<':
                cond = cond_reg_val < int(cond_val)
            elif cond_op == '>=':
                cond = cond_reg_val >= int(cond_val)
            elif cond_op == '<=':
                cond = cond_reg_val <= int(cond_val)
            elif cond_op == '!=':
                cond = cond_reg_val != int(cond_val)
            else:
                assert(False)

            if cond:
                mod_reg_val = get_val(mod_reg)
                if mod_op == 'inc':
                    regs[mod_reg] = mod_reg_val + int(mod_val)
                elif mod_op == 'dec':
                    regs[mod_reg] = mod_reg_val - int(mod_val)
                else:
                    assert(False)
                if regs[mod_reg] > max_val:
                    max_val = regs[mod_reg]

    print('Part one:', max(regs.values()))
    print('Part two:', max_val)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path')
    args = parser.parse_args()
    main(args)
