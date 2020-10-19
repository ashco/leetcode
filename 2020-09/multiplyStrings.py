def multiply(num1: str, num2: str) -> str:
    count = 0

    for i in range(len(num1))[::-1]:
        shift = 10 ** (len(num1) - i - 1)

        for j in range(len(num2))[::-1]:
            print(num1[i], num2[j])
            sum = (int(num1[i]) * int(num2[j])) * shift
            count += sum
            shift *= 10
    return str(count)

print(multiply('12', '34'))