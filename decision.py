def decide_action(state, intensity, stress, energy, time):

    if stress >= 8:
        return "breathing", "now"

    if time == "night" and energy <= 4:
        return "sleep", "tonight"

    if state == "overwhelmed":
        if intensity >= 3:
            return "grounding", "now"
        else:
            return "breathing", "within_15_min"

    if state == "restless":
        if energy >= 6:
            return "movement", "now"
        elif intensity >= 3:
            return "grounding", "within_15_min"
        else:
            return "breathing", "within_15_min"

    if state == "mixed":
        return "journaling", "later_today"

    if state == "focused":
        if energy >= 6 and stress <= 5:
            return "deep_work", "now"
        else:
            return "light_planning", "within_15_min"

    if state == "calm":
        if time == "night":
            return "sleep", "tonight"
        else:
            return "light_planning", "later_today"

    if state == "neutral":
        return "light_planning", "later_today"

    if energy <= 2:
        return "rest", "now"

    if energy <= 4:
        return "rest", "later_today"

    if energy >= 6 and time == "night":
        return "deep_work", "tomorrow_morning"

    return "light_planning", "later_today"