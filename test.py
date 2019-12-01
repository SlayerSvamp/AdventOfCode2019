def test(expected, actual, name=None, *, verbose=False):
    if expected != actual or verbose:
        message = ''

        if expected == actual:
            message += 'verbose: '

        message += f"expected '{expected}', got '{actual}'"

        if name:
            message += ' in {name}'

        print(message)
