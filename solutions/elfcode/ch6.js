for (i = 0; i < 4; i++)
  elf.moveTo(lollipop[i])
elf.moveTo(lever[0])
response = elf.get_lever(0)
response.unshift("munchkins rule")
elf.pull_lever(response)
elf.moveTo(munchkin[0])
elf.moveUp(2)

// Game won
