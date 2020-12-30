function my_func(arrays) {
  return arrays.flat().filter(function(item) {
    return (parseInt(item) == item);
  }).reduce((a, b) => a + b)
}

function pull(i) {
  elf.pull_lever(i)
}
for (i = 0; i < 2; i++) {
  elf.moveDown(1 + (4 * i))
  pull(i * 4)
  elf.moveLeft(2 + (4 * i))
  pull((i * 4) + 1)
  elf.moveUp(3 + (4 * i))
  pull((i * 4) + 2)
  elf.moveRight(4 + (4 * i))
  pull((i * 4) + 3)
  lever += 4
}
elf.moveUp(2)
elf.moveLeft(4)
elf.tell_munch(my_func)
elf.moveUp(2)
