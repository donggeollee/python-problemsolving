def palindrome(spin_string):
    if len(spin_string) <= 1 :
        return True
    if spin_string[0] == spin_string[-1]:
        return palindrome(spin_string[1:-1])
    return False

print(palindrome("abcdedcba"))