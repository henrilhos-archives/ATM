import random


class ATM:
    def __init__(self, notes=dict()):
        self.notes = dict()
        self.amount = 0
        self.set_notes(notes)

    def set_notes(self, notes):
        for key, value in notes.items():
            self.set_note(key, value)

    def set_note(self, note, quantity):
        self.notes[note] = quantity
        self.update_amount()

    def update_amount(self):
        self.amount = 0
        for key, value in self.notes.items():
            self.amount += key * value

    def get_amount(self):
        return self.amount

    def get_notes_string(self):
        notes = {note: qtd for note, qtd in self.notes.items() if qtd > 0}
        notes_list = list(notes.keys())
        notes_string = ' | '.join((str(n) for n in notes_list))

        return notes_string

    def get_quantity(self, note):
        return self.notes.get(note, 0)

    def withdraw(self, value):
        result = dict()
        for note in sorted(self.notes, reverse=True):
            while value >= note and self.get_quantity(note) > 0:
                result[note] = result.get(note, 0) + 1
                value -= note
                self.set_note(note, self.get_quantity(note) - 1)

        return result


def spaces_size(length):
    return get_spaces(
        {
            3: 0,
            2: 1,
            1: 2
        }.get(length, 0)
    )


def get_spaces(size):
    spaces = ''

    for i in range(size):
        spaces += ' '

    return spaces


if __name__ == '__main__':
    notes = dict()
    notes_list = [2, 5, 10, 20, 50, 100]

    for note in notes_list:
        quantity = random.randrange(0, 16, 1)
        notes[note] = quantity

    atm = ATM(notes)

    print('Valor total disponível: R$', atm.get_amount())
    print('Notas disponíveis:')
    print(atm.get_notes_string())

    value_to_withdraw = input('\nInsira o valor desejado de saque: ')
    value_to_withdraw = int(value_to_withdraw)

    value = atm.withdraw(value_to_withdraw)

    print('\nNota | Quantidade')
    for note, qtd in value.items():
        note_length = len(str(note))
        print(spaces_size(note_length), note, '|', qtd)
