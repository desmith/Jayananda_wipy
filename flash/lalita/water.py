from lalita.pins import valve


def open():
    valve(0)


def close():
    valve(1)


def status():
    return 'stopped' if valve.value() else 'flowing'


close()
