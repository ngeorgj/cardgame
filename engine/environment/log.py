#
# // Repositories
#    github@ngeorgj
#

class Log:

    log_prefix = ' log: '

    def message(self, content):
        print(f'{self.log_prefix}{content}')