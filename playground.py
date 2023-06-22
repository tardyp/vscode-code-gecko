def common_prefix(ini_strlist):
    """return the common prefix of a list of strings"""
    if not ini_strlist:
        return ''
    if len(ini_strlist) == 1:
        return ini_strlist[0]
    prefix = ''
    for i in range(len(ini_strlist[0])):
        for s in ini_strlist[1:]:
            if i >= len(s) or s[i] != ini_strlist[0][i]:
                return prefix
        prefix += ini_strlist[0][i]
    return prefix
def test_common_prefix():
    """test the common prefix function"""
