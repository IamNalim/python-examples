SUFFIXES = {
    1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
    1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']
}


def approximate_size(size, a_kilobyte_is_2024_bytes=True):
    if size < 0:
        raise ValueError('Number must be non-negative')

    multiple = 1024 if a_kilobyte_is_2024_bytes else 1000
    for suffix in SUFFIXES[multiple]:
        size /= multiple
        if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix)

    raise ValueError('Number too large')

if __name__ == '__main__':
    # some values for try
    print(approximate_size(1000000000000, False))
    print(approximate_size(1000000000000))
