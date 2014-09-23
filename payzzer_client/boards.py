class Board(object):
    def __init__(self, data):
        self.__type = data.get('__type')

        self.id = data.get('id')
        self.default_account_id = data.get('default_account_id')
        self.name = data.get('name')
        self.role = data.get('role')

    def __repr__(self):
        return self.__unicode__()

    def __unicode__(self):
        return 'Board#{0}({1})'.format(self.id, self.name)


class Boards(object):
    def __init__(self, data):
        self.__type = data.get('__type')

        self.default_board_id = data.get('default_board_id')
        self._boards = {board.get('id'): Board(board) for board in data.get('board_list')}
        self.boards = self._boards.values()
        self.default = self._boards.get(self.default_board_id)

    def __repr__(self):
        return self.__unicode__()

    def __unicode__(self):
        return 'Boards({0}): default={1}'.format(len(self.boards), self.default_board_id)

    def __iter__(self):
        return iter(self.boards)
