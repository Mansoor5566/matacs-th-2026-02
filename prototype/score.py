"""Tiny scoring check. Takes facts (as the AI would extract them) and does the maths.
No API calls. The point: scoring is plain code, so it is repeatable."""
BUDGET, MAX_WEEKS = 260_000, 16

def score(f):
    exp = min(f["installs"], 12) / 12 * 30
    price = max(0, min(1, (BUDGET - f["price"]) / (BUDGET * 0.2))) * 25   # full marks at 80% of budget
    if f["weeks"] is None:
        return None                                                        # can't score -> flag
    time = max(0, min(1, (MAX_WEEKS - f["weeks"]) / 8)) * 15               # full marks at 8 weeks
    warr = (min(f["panel"], 25) / 25 + min(f["work"], 12) / 12) * 7.5
    team = sum([f["lead"], f["crew"], f["safety"], f["monitor"]]) * 3.75
    return round(exp + price + time + warr + team, 1)

# facts as numbers only (no proposal text)
facts = {
 "A": dict(installs=14, price=238000, weeks=12, panel=25, work=10, lead=1, crew=1, safety=1, monitor=1),
 "C": dict(installs=9,  price=244000, weeks=14, panel=25, work=10, lead=1, crew=1, safety=0, monitor=0),
 "D": dict(installs=11, price=231000, weeks=None, panel=25, work=10, lead=1, crew=0, safety=1, monitor=0),
 "E": dict(installs=8,  price=242500, weeks=13, panel=25, work=12, lead=1, crew=1, safety=1, monitor=1),
}
for k, v in facts.items():
    print(k, score(v))
for w in (8, 12):
    d = dict(facts["D"], weeks=w); print(f"D at {w} weeks:", score(d))
