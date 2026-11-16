# Lab 4 Vibe Coding

Ganavi Purushothama | PES2UG24CS167

Meteor Dodge is a Python and Pygame game. SPACE launches, fires a laser during play, and restarts after a loss.

- [Before video](Submission/before.mp4) uses the unmodified course starter at b168286. SPACE launches the ship. Pressing SPACE in flight does not fire.
- [After video](Submission/after.mp4) uses a scripted run of the updated game. The demo places a large meteor and a shield orb on repeatable paths. It shows laser firing, two fragments, shield pickup and absorption, and the multiplier returning to 1x after a hit.
- [Updated code](Submission/Updated_Code/) includes the existing laser and fragment work and the two new commits for shields and scoring.
- [Lab 4 chat excerpt](Submission/Chat_History.pdf) records the relevant user messages and assistant updates.
- [Personal Meteor Dodge repository](https://github.com/Ganavi-Purushothama/PES2UG24CS167-Meteor-Dodge)

Both recordings are 10 seconds. Checks on Python 3.14 with pygame-ce verified the launch and firing states, fragment count, shield protection, multiplier thresholds, unshielded collision, and restart. For the original pinned pygame package, use a Python version with a compatible wheel, such as Python 3.12.
