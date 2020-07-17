from Crypto.Hash import MD5


def bruteforce(password):
    message = "ctflag"
    hash = MD5.new()
    hash.update(message.encode("utf8")+password.encode("utf8"))
    if hash.hexdigest() == "e82a4b4a0386d5232d52337f36d2ab73":
        print(hash.hexdigest())
        print(message+password)

list_num = "0123456789"
for i in list_num:
    for j in list_num:
        for k in list_num:
            for l in list_num:
                for m in list_num:
                    password = i+j+k+l+m
                    bruteforce(password)
