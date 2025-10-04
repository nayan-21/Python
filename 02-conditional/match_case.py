seat_type = input("Enter seat type (sleeper/AC/general/luxury)").lower()


match seat_type:
    case "sleeper":
        print("Sleeper - No AC, beds available")
    case "ac":
        print("AC - Air conditioned, comfy ride")
    case "general":
        print("General - Cheapest option, no reservation")
    case "luxury":
        print("Luxury - Premium seats with meals")
    case _:
        print("Invalid seat type")

# The match-case statement in Python is a control flow structure that allows for pattern matching against a given value.
# It is similar to switch-case statements found in other programming languages but offers more advanced features.   
# The match-case statement starts with the match keyword followed by the value to be matched (in this case, seat_type).
# Each case is defined using the case keyword followed by a pattern to match against the value. 