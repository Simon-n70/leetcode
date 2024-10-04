def roman_to_int(string: str) -> int:
    accordance = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    if string == "" or string == 0:
        return 0
    if len(string) == 1:
        return accordance[string]
    else:
        count = 0
        numbers = []
        less = False
        while count + 1 < len(string):
            if accordance[string[count]] >= accordance[string[count+1]]:  # First+second checks all the same or more
                if less:
                    numbers.append(-accordance[string[count]])  # previous was less
                else:
                    numbers.append(accordance[string[count]])
            elif accordance[string[count]] < accordance[string[count+1]]:  # Third check going up
                numbers.append(-abs(accordance[string[count]]))
            if count + 1 == len(string) - 1:
                numbers.append(accordance[string[-1]])
            count += 1
        result = sum(numbers)
        return result
