moma_artworks = {"Starry Night", "The Persistence of Memory", "The Scream", "Girl with a Pearl Earring"}

louvre_artworks = {"Mona Lisa", "The Scream", "Liberty Leading the People", "Girl with a Pearl Earring"}

rijksmuseum_artworks = {"The Night Watch", "Girl with a Pearl Earring", "The Milkmaid", "Starry Night"}


moma_artworks_New= {"Composition with Red, Blue,and Yellow."}
moma_artworks.update(moma_artworks_New)

shared_masterpieces = moma_artworks & louvre_artworks & rijksmuseum_artworks

print("\nShared Masterpieces:\n")
print(f"\n{shared_masterpieces}\n")

louvre_artworks_New = {"Raft of the Medusa", "Liberty Leading the People"}
rijksmuseum_artworks_New = {"The Jewish Bride", "The Milkmaid"}

update = louvre_artworks.update(louvre_artworks_New)
updated = rijksmuseum_artworks.update(rijksmuseum_artworks_New)

print(moma_artworks)
print(louvre_artworks)
print(rijksmuseum_artworks)

print("\n The master list\n")

print("\nDiffrences\n")
diffrence = moma_artworks - louvre_artworks - rijksmuseum_artworks
print(diffrence)

del rijksmuseum_artworks



"""
One of my biggest achievements(Newbie)
"""



moma_artworks = {"Starry Night", "The Persistence of Memory", "The Scream", "Girl with a Pearl Earring"}
louvre_artworks = {"Mona Lisa", "The Scream", "Liberty Leading the People", "Girl with a Pearl Earring"}
rijksmuseum_artworks = {"The Night Watch", "Girl with a Pearl Earring", "The Milkmaid", "Starry Night"}

moma_artworks.add("Composition with Red, Blue, and Yellow")

shared_masterpieces = moma_artworks.intersection(louvre_artworks, rijksmuseum_artworks)
print("\nShared Masterpieces:\n", shared_masterpieces)

louvre_artworks.update({"Raft of the Medusa", "Liberty Leading the People"})
rijksmuseum_artworks.update({"The Jewish Bride", "The Milkmaid"})

master_list = moma_artworks.union(louvre_artworks, rijksmuseum_artworks)
print("\nMaster List of Unique Artworks:\n", master_list)
print("Total Unique Artworks:", len(master_list))

rijksmuseum_artworks.discard("The Milkmaid")
print("\nUpdated Rijksmuseum Collection:\n", rijksmuseum_artworks)

exclusive_moma = moma_artworks.difference(louvre_artworks, rijksmuseum_artworks)
print("\nExclusive Pieces from MoMA:\n", exclusive_moma)
