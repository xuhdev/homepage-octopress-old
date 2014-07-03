def match_number_range(string, pattern):
    """
    Matches a string with pattern. The pattern can contain {num1..num2} to express the a range of numbers. The match is
    successful if no exception is raised. Note the code won't work if you have any capturing groups in it.

    string: the string to match
    pattern: the pattern to be matched
    """

    import re

    integer_regex = r'[\+\-]?[0-9]+'

    # extract all the number pairs (number ranges)
    number_pairs = list(map(lambda x: (float(x[0]), float(x[1])), re.findall(r'(?<!\\){{({})..({})}}'.format(integer_regex, integer_regex), pattern)))

    # replace all occurence of {num1..num2} by integer numbers
    new_pattern = re.sub(r'(?<!\\){{{}..{}}}'.format(integer_regex, integer_regex), r'({})'.format(integer_regex), pattern)

    matching_obj = re.fullmatch(new_pattern, string)

    if matching_obj == None:
        raise Exception('No matching')

    if len(matching_obj.groups()) != len(number_pairs):
        raise Exception('More unexcepted capturing groups found.')

    for nums in zip(matching_obj.groups(), number_pairs):
        small_int = nums[1][0]
        large_int = nums[1][1]
        if float(nums[0]) < small_int or float(nums[0]) > large_int:
            raise Exception('No matching')

    # successfully matched if we reach here

# examples
# match a number between -1 and 100
# match_number_range('4', '{-1..100}')
# match number range 1 to 4 followed by letter a then number range 2 to 100
# match_number_range('2a5', '{1..4}a{2..100}')
