from __future__ import annotations



def stable_matching(
    donor_pref: list[list[int]], recipient_pref: list[list[int]]
) -> list[int]:
    assert len(donor_pref) == len(recipient_pref)

    def _prefers_current_match(
        recipient: int, prev_donor: int, current_donor: int
    ) -> bool:
        """Checks if recipient prefers their current donor over a new one"""
        rec_preference = recipient_pref[recipient]
        return rec_preference.index(prev_donor) < rec_preference.index(current_donor)

    def _update_records(donor: int, recipient: int, prev_donor: int) -> None:
        """Updates the donor and recipient records"""
        rec_record[recipient] = donor
        donor_record[donor] = recipient
        if prev_donor != -1:
            unmatched_donors.append(prev_donor)
        unmatched_donors.remove(donor)

    n = len(donor_pref)
    unmatched_donors = list(range(n))
    donor_record = [-1] * n
    rec_record = [-1] * n
    num_donations = [0] * n

    while unmatched_donors:
        donor = unmatched_donors[0]
        recipient = donor_pref[donor][num_donations[donor]]
        num_donations[donor] += 1
        prev_donor = rec_record[recipient]

        # If recipient prefers current match, move on to the next one
        if prev_donor != -1 and _prefers_current_match(recipient, prev_donor, donor):
            continue

        _update_records(donor, recipient, prev_donor)

    return donor_record
