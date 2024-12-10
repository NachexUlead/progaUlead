def calculateTax(state: str, totalPrice: float) -> float:
    state = state.upper()

    if state not in ["NH", "MA", "CA", "TX", "IL", "KY"]:
        raise ValueError(f"error: invalid state: {state}")

    if state == "NH":
        return 0.0
    elif state in ["MA", "CA", "TX"]:
        return totalPrice * 0.18
    elif state == "IL":
        if totalPrice < 1000:
            return 0.0
        elif totalPrice < 10000:
            return totalPrice * 0.12
        else:
            return totalPrice * 0.16
    elif state == "KY":
        if totalPrice < 1000:
            return 0.0
        elif totalPrice < 10000:
            return totalPrice * 0.13
        else:
            return totalPrice * 0.17


def validateState(state: str) -> bool:
    validStates = [
        "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN",
        "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV",
        "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN",
        "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"
    ]
    return state.upper() in validStates