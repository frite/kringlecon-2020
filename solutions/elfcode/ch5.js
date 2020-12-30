elf.moveTo(munchkin[0])
response = elf.ask_munch(0).filter(numbersOnly);
elf.tell_munch(response)
elf.moveUp(2)

function numbersOnly(value) {
  if (typeof(value) === 'number') {
    return value;
  }
}
