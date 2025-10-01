spice_mix = set()
print(f"Initial spice mix id: {id(spice_mix)}")
print(f"Initial spice mix: {spice_mix}")
spice_mix.add("Ginger")
spice_mix.add("cardamom")
spice_mix.add("lemon")
print(f"Updated spice mix: {spice_mix}")
print(f"After spice mix id: {id(spice_mix)}")

# When we add elements to the set, the id of the set remains the same,
# indicating that the same set object is being modified in place.
# This is because sets are mutable in Python.
# The contents of the set change, but the object itself does not get recreated in memory.
# This is in contrast to immutable types like integers or strings,
# where changing the value results in a new object being created.