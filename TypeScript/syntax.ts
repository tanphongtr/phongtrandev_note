interface Human {
  name: string;
  year: number;
  // add a attribute as array number or string
  groups: (string | number)[];
}

class UserEntity implements Human {

  constructor({ name, year, groups }: Human) {
    Object.assign(this, { name, year, groups });
  }
  name: string = '';
  year: number = 1994;
  groups: (string | number)[] = [1, 2, '4'];
}

function showHuman(person: Human) {
  console.log(person.name, person.year);
}

const ps = {
  name: 'Phong',
  year: 1994,
  groups: ['test', 1],
};

showHuman(ps);