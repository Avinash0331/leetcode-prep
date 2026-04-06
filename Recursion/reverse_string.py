def reverse(s):
    #recursion
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]
    

reverse("abc")

# Example: reverse("abc")
# reverse("abc") → reverse("bc") + "a"
# reverse("bc") → reverse("c") + "b"
# reverse("c") → reverse("") + "c" → "" + "c" → "c"
# Result: "c" + "b" + "a" = "cba"    