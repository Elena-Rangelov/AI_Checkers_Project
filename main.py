from state import State
from player import Player

p1 = Player(True)
p2 = Player(False)

st = State(p1, p2)
print("training...")
st.play(1)