def segments_in_all_digits(digits):
    out_segments = set('abcdefg')
    for in_digit in digits:
        out_segments = out_segments.intersection(set(in_digit))
    return out_segments


with open("InputFiles/Day_8.txt") as f:
    entries = []
    for line in f:
        notes, output_val = line.split(' | ')
        entries.append((notes.split(), output_val.split()))

# Part 1
part_1_ans = 0
for entry in entries:
    _, output_val = entry
    for digit in output_val:
        # Digits 1, 4, 7 and 8 have 2, 4, 3 and 7 segments respectively
        if len(digit) in [2, 4, 3, 7]:
            part_1_ans += 1
print(part_1_ans)

# Part 2
num_wires_pos_segments = {2: 'cf', 3: 'acf', 4: 'bcdf'}  # digit segments represented by patterns with unique lengths
segments_on_in_all_digits = {5: 'adg', 6: 'abfg'}  #
segments_to_digit = {'abcefg': '0', 'cf': '1', 'acdeg': '2', 'acdfg': '3', 'bcdf': '4', 'abdfg': '5', 'abdefg': '6',
                     'acf': '7', 'abcdefg': '8', 'abcdfg': '9'}  # lookup table for segments to digits

part_2_ans = 0
for entry in entries:
    notes, output_val = entry

    # To find the number represented by the output values we need to find a mapping between segments and signal wires
    # Once this mapping is found, a simple lookup table can be used to find the digits represented by the segments
    # Our algorithm for finding this logically will consist of three sections
    # To start, we keep track of the possible signal wires for each segment
    # These possibilities will be eliminated until there is only one possible signal wire for each segment
    pos_mappings = {i: set('abcdefg') for i in 'abcdefg'}

    # First, we consider the signal patterns with lengths which are unique among the digits
    # For example, if a signal pattern has length 2 we know it must represent digit 1, which has segments c and f on
    # This means that for segments c and f, we can eliminate any signal wires that are not part of that signal pattern
    # For example, if the signal pattern was 'ab', then segments c and f must be mapped to either signal wires a or b
    # This means we can eliminate any possibilities for segments c and f that are not signal wires a or b
    # This can be done for all signal patterns with lengths 2, 3 and 4 (digits 1, 7, 4 respectively)
    # Note that we do not consider length 7 (digit 8) even though it has a unique length, and this is because
    # a signal pattern with length 7 will have all signal wires and so it is not useful for eliminating possibilities
    multiple_digit_lens = {i: [] for i in segments_on_in_all_digits.keys()}
    for digit in notes + output_val:
        if len(digit) in num_wires_pos_segments:
            for segment in num_wires_pos_segments[len(digit)]:
                pos_mappings[segment] = pos_mappings[segment].intersection(set(digit))
        elif len(digit) in segments_on_in_all_digits:
            multiple_digit_lens[len(digit)].append(digit)

    # Second, we consider the signal patterns with lengths that multiple different digits have: lengths 5 and 6
    # We observe that there are segments that are turned on in all digits with these lengths
    # For example, digits with length 5 (digits 2, 3, 5) all have segments a, d, g in common
    # This is also true for digits with length 6 (digits 0, 6, 9) and they all have segments a, b, f, g in common
    # This means that since signal wires are mapped to segments, among all signal patterns with length 5, there
    # should also be three signal wires that all signal patterns have in common (for length 6 this will be 4 wires)
    # For example, if all signal wires with length 5 have 'cdf' in common, then segments a, d, and g must be mapped to
    # only signal wires c, d, or f and any other possibilities for these segments can be eliminated
    # An nearly identical (only the number of common signal wires is different) can be done for signal wires of length 6
    for length, segments in segments_on_in_all_digits.items():
        digit_segments = segments_in_all_digits(multiple_digit_lens[length])
        for segment in segments:
            pos_mappings[segment] = pos_mappings[segment].intersection(digit_segments)

    # Third, at this point, the mapping should be completely determined and the signal patterns are no longer needed
    # However, we still have to logically eliminate possibilities within the mapping itself
    # For example, segment a might be mapped to only wire d, but segment b might have wires d and f as possibilities
    # Since wires can only be mapped to one segment (segments a and b cannot both be mapped to wire d), segment b cannot
    # be mapped to wire d (if it was segment a would have no possible mapping)
    # Using this logic, we go through the segments, and if a segment is mapped to only one signal wire, we eliminate
    # that signal wire from being a possibility for all the other segments
    while any(len(mapping) > 1 for mapping in pos_mappings.values()):
        unique_mappings = set()
        for segment in pos_mappings.keys():
            if len(pos_mappings[segment]) == 1:
                unique_mappings.add(list(pos_mappings[segment])[0])

        for segment, mapping in pos_mappings.items():
            if len(mapping) > 1:
                pos_mappings[segment] = mapping.difference(unique_mappings)

    # Finally, after we are done finding the mapping, we reverse it so that signal wires are mapped to segments
    # Determining the mapping was easier in the previous configuration, but this configuration will be easier to use
    # to find the digits represented by the output signal patterns
    pos_mappings = {list(mapping)[0]: segment for segment, mapping in pos_mappings.items()}

    num_val = ''
    for output_segments in output_val:
        segments = []
        for digit in output_segments:
            segments.append(pos_mappings[digit])
        num_val += segments_to_digit[''.join(sorted(segments))]
    part_2_ans += int(num_val)
print(part_2_ans)
