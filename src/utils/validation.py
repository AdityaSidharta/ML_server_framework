def validate_str(input, allow_list):
    if input in allow_list:
        return True
    else:
        return False


def validate_int(input, allow_low, allow_high):
    if not input.isdigit():
        return False
    elif int(input) < allow_low:
        return False
    elif int(input) > allow_high:
        return False
    else:
        return True
