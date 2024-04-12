from state import State
from player import Player

p1 = Player("p1", True)
p2 = Player("p2", False)

st = State(p1, p2)
print("training...")
st.play(1)

p1.savePolicy()