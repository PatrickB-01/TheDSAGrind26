This file keeps track of patterns that i have seen in coding challenges
# Patterns

| Problem                | Pattern         | Why?                                   |
| ---------------------- | --------------- | -------------------------------------- |
| Contains Duplicate     | Hash Set        | Detect repeated value                  |
| Two Sum                | Hash Map        | Store values seen so far and check whether the complement has already appeared |
| Valid Anagrams         | Hash Map        | Keep count of frequency of values with fast lookup |
| Group Anagrams        | Hash Map        | Use a signature such as a sorted string or frequency count as a key to group related values efficiently |


# Clues

| Clue                | Pattern        |
| ------------------- | -------------- |
| Repeated values + yes/no answer + no need for counts or sorting | Hash Set |
| Need to find a pair or complement quickly | Hash Map |
| Keep count of frequencies + fast lookup for comparison/edit | Hash Map |
| Need to group items by a shared signature or classify them into buckets | Hash Map |
