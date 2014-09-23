import re


class Operation(object):
    TYPE_ADD = 1
    TYPE_SUBTRACT = 2
    TYPE_TRANSFER = 3
    TYPE_MOVE = 4
    TYPE_NOTE = 5
    TYPES = {
        TYPE_ADD: 'add',
        TYPE_SUBTRACT: 'subtract',
        TYPE_TRANSFER: 'transfer',
        TYPE_MOVE: 'move',
        TYPE_NOTE: 'note',
    }

    SOURCE_WEB = 1
    SOURCE_MOBILE = 2
    SOURCE_API = 3
    SOURCES = {
        SOURCE_WEB: 'web',
        SOURCE_MOBILE: 'mobile',
        SOURCE_API: 'api',
    }

    def __init__(self, data):
        self.__type = data.get('__type')
        
        self.type = data.get('type')
        self.source = data.get('source')
        self.id = data.get('id')
        self.account_icon_id = data.get('account_icon_id')
        self.currency_id = data.get('currency_id')
        self.currency_iso = data.get('currency_iso')
        self.signature = data.get('signature')
        self.text = data.get('text')
        self.time = data.get('time')
        self.time_add = data.get('time_add')
        self.value = data.get('value')
        self.account_name = data.get('account_name')
        self.from_account_name = data.get('from_account_name')
        self.to_account_name = data.get('to_account_name')

        tag_pattern = re.compile(r'<!\[#(.+?)\]!>')
        self.tags = tag_pattern.findall(self.text)

    def __repr__(self):
        return self.__unicode__()

    def __unicode__(self):
        # return u'Operation({0})={1}#{2}#'.format(self.TYPES[self.type], self.value, ','.join(self.tags))
        return u'Operation({0}@{1})={2}#{3}#'.format(self.TYPES[self.type], self.time_add, self.value, self.text)

    @property
    def is_add(self):
        return self.type == self.TYPE_ADD

    @property
    def is_subtract(self):
        return self.type == self.TYPE_SUBTRACT

    @property
    def is_transfer(self):
        return self.type == self.TYPE_TRANSFER

    @property
    def is_move(self):
        return self.type == self.TYPE_MOVE

    @property
    def is_note(self):
        return self.type == self.TYPE_NOTE
