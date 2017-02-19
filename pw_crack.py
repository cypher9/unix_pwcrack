import crypt
import sys


class SHADOWITEM():
    user = ""
    pwhash = ""

    def __init__(self, user, pwhash):
        self.user = user
        self.pwhash = pwhash


def make_shadow_item(user, pwhash):
    shadowItem = SHADOWITEM(user, pwhash)
    return shadowItem


def testpass(cryptpass, dictfile_path):
    salt = cryptpass[0:2]
    dictfile = open(dictfile_path, 'r')
    for word in dictfile.readlines():
        word = word.split('\n')
        cryptword = crypt.crypt(word, salt)
        if cryptword == cryptpass:
            return str(word)
        else:
            return False


def read_shadow(shadow_file):
    shadowfile = open(shadow_file, 'r')
    user_hash_list = []
    for line in shadowfile.readlines():
        if ':' in line:
            user_hash = line.split(':')
            shadowitem = make_shadow_item(user_hash[0], user_hash[1].strip(' '))
            user_hash_list.append(shadowitem)
    return user_hash_list


def main(dictfile, shadow):
    user_hash_list = read_shadow(shadow)
    for user_hash in user_hash_list:
        print "Testing passwords for user: " + str(user_hash.user)
        found_pw = testpass(user_hash.pwhash, dictfile)
        if found_pw:
            print "Unix password for user: " + str(user_hash.user) + " is " + found_pw
        else:
            print "No passwords matching!"


if __name__ == '__main__':
    dictfile = sys.argv[1]
    shadow_file = sys.argv[2]

    main(dictfile, shadow_file)

