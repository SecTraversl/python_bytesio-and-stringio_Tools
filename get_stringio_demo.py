# %%
#######################################
def get_stringio_demo():
    """Demo of using io.StringIO.

    Example:
        >>> get_stringio_demo()\n
        'bob, 21, janitor, sanitization team, 02alice, 22, secretary, admin team, 03chuck, 23, plumber, construction team, 04'

    Returns:
        str: Returns a string.
    """
    import io
    stringbuffer = io.StringIO()
    somecontent = 'bob, 21, janitor, sanitization team, 02\nalice, 22, secretary, admin team, 03\nchuck, 23, plumber, construction team, 04\n'
    for line in somecontent.splitlines():
        # stringbuffer.seek(line.find(','))
        # stringbuffer.write(line[0:2] + line[-2:-1])
        stringbuffer.write(line)
    return stringbuffer.getvalue()

