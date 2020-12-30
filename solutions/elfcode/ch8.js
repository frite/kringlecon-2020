function getKeyByValue(arr) {
  var str = ""
  arr.forEach(obj => Object.keys(obj).filter(function(key) {
    if (obj[key] === "lollipop") {
      str = key
    }
  }))
  return str
}

function levers() {
  nums = []
  for (i = 0; i < 6; i++) {
    nums.push(elf.get_lever(i))
  }
  sums = []
  sums[0] = nums[0]
  for (i = 1; i < 6; i++)
    sums[i] = sums[i - 1] + nums[i]
  return sums
}

function up() {
  elf.moveUp(2)
}
sums = levers()
pos = 0
for (i = 1; i < 13; i += 4) {
  elf.moveRight(i)
  elf.pull_lever(sums[pos])
  up()
  elf.moveLeft(i + 2)
  elf.pull_lever(sums[pos + 1])
  up()
  pos += 2
}
elf.tell_munch(getKeyByValue)
elf.moveRight(11)
