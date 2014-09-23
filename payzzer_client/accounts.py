class Summary(object):
    def __init__(self, data):
        self.__type = data.get('__type')

        self.currency_id = data.get('currency_id')
        self.currency_iso = data.get('currency_iso')
        self.add_plus_count = data.get('add_plus_count', 0)
        self.add_plus_value = data.get('add_plus_value', 0)
        self.subtrack_minus_count = data.get('subtrack_minus_count', 0)
        self.subtrack_minus_value = data.get('subtrack_minus_value', 0)
        self.move_plus_count = data.get('move_plus_count', 0)
        self.move_plus_value = data.get('move_plus_value', 0)
        self.move_minus_count = data.get('move_minus_count', 0)
        self.move_minus_value = data.get('move_minus_value', 0)
        self.transfer_plus_count = data.get('transfer_plus_count', 0)
        self.transfer_plus_value = data.get('transfer_plus_value', 0)
        self.transfer_minus_count = data.get('transfer_minus_count', 0)
        self.transfer_minus_value = data.get('transfer_minus_value', 0)

    def __repr__(self):
        return self.__unicode__()

    def __unicode__(self):
        return 'Summary#{0}={1:.2f}'.format(self.currency_iso, self.balance)

    @property
    def balance(self):
        return sum([
            self.add_plus_value,
            -self.subtrack_minus_value,
            self.move_plus_value,
            -self.move_minus_value,
            self.transfer_plus_value,
            -self.transfer_minus_value,
        ])


class Account(object):
    def __init__(self, data):
        self.__parent_type = data.get('__type')

        self.__type = data.get('object').get('__type')
        self.id = data.get('object').get('id')
        self.name = data.get('object').get('name')
        self.description = data.get('object').get('description')
        self.icon_id = data.get('object').get('icon_id')
        self.in_balance = data.get('object').get('in_balance')
        self.is_active = data.get('object').get('is_active')

        self.summaries = [Summary(summary) for summary in data.get('summaries_list')]

    def __repr__(self):
        return self.__unicode__()

    def __unicode__(self):
        return 'Account#{0}({1})=[{2}]'.format(self.id, self.name, self.balance)

    @property
    def balance(self):
        """Returns total balance using all currencies, but skips zeroed summaries"""
        return ', '.join(['{0}'.format(summary) for summary in self.summaries if summary.balance])


class Accounts(object):
    def __init__(self, data):
        self.__type = data.get('__type')
        self.browse_type = data.get('browse_type')
        self.report_type = data.get('report_type')
        # boards
        self._accounts = {account.get('object').get('id'): Account(account) for account in data.get('accounts_with_summaries_list')}
        self.accounts = self._accounts.values()

    def __repr__(self):
        return self.__unicode__()

    def __unicode__(self):
        return 'Accounts({0})'.format(len(self.accounts))

    def __iter__(self):
        return iter(self.accounts)
