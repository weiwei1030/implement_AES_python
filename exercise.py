import copy, math

s_box = [['63', '7c', '77', '7b', 'f2', '6b', '6f', 'c5', '30', '01', '67', '2b', 'fe', 'd7', 'ab', '76'],
         ['ca', '82', 'c9', '7d', 'fa', '59', '47', 'f0', 'ad', 'd4', 'a2', 'af', '9c', 'a4', '72', 'c0'],
         ['b7', 'fd', '93', '26', '36', '3f', 'f7', 'cc', '34', 'a5', 'e5', 'f1', '71', 'd8', '31', '15'],
         ['04', 'c7', '23', 'c3', '18', '96', '05', '9a', '07', '12', '80', 'e2', 'eb', '27', 'b2', '75'],
         ['09', '83', '2c', '1a', '1b', '6e', '5a', 'a0', '52', '3b', 'd6', 'b3', '29', 'e3', '2f', '84'],
         ['53', 'd1', '00', 'ed', '20', 'fc', 'b1', '5b', '6a', 'cb', 'be', '39', '4a', '4c', '58', 'cf'],
         ['d0', 'ef', 'aa', 'fb', '43', '4d', '33', '85', '45', 'f9', '02', '7f', '50', '3c', '9f', 'a8'],
         ['51', 'a3', '40', '8f', '92', '9d', '38', 'f5', 'bc', 'b6', 'da', '21', '10', 'ff', 'f3', 'd2'],
         ['cd', '0c', '13', 'ec', '5f', '97', '44', '17', 'c4', 'a7', '7e', '3d', '64', '5d', '19', '73'],
         ['60', '81', '4f', 'dc', '22', '2a', '90', '88', '46', 'ee', 'b8', '14', 'de', '5e', '0b', 'db'],
         ['e0', '32', '3a', '0a', '49', '06', '24', '5c', 'c2', 'd3', 'ac', '62', '91', '95', 'e4', '79'],
         ['e7', 'c8', '37', '6d', '8d', 'd5', '4e', 'a9', '6c', '56', 'f4', 'ea', '65', '7a', 'ae', '08'],
         ['ba', '78', '25', '2e', '1c', 'a6', 'b4', 'c6', 'e8', 'dd', '74', '1f', '4b', 'bd', '8b', '8a'],
         ['70', '3e', 'b5', '66', '48', '03', 'f6', '0e', '61', '35', '57', 'b9', '86', 'c1', '1d', '9e'],
         ['e1', 'f8', '98', '11', '69', 'd9', '8e', '94', '9b', '1e', '87', 'e9', 'ce', '55', '28', 'df'],
         ['8c', 'a1', '89', '0d', 'bf', 'e6', '42', '68', '41', '99', '2d', '0f', 'b0', '54', 'bb', '16']]

def hex2bin(h):
    x = len(h) * 4
    return str(bin(int(h, 16))[2:].zfill(x))

const=['0','0','0','1','1','0','1','1']


def bin2hex(b):
    b = int(b, 2)
    return hex(b)[2:].zfill(2)


def str2hex(s):
    tmp = []
    s = s.replace(' ', '')
    for i in range(0, len(s), 2):
        tmp.append(s[i] + s[i + 1])
    h = []
    li1 = tmp[0:4]
    li2 = tmp[4:8]
    li3 = tmp[8:12]
    li4 = tmp[12:16]
    h.append(li1)
    h.append(li2)
    h.append(li3)
    h.append(li4)
    rs = []
    for i in range(len(h)):
        t = []
        for j in range(len(h)):
            t.append(h[j][i])
        rs.append(t)
    return rs

def xor(x, y):
    li = ''
    for i, j in zip(x, y):
        if i == j:
            c = '0'
        else:
            c = '1'
        li += c
    return li


def ks(key, rd):
    key = key.replace(' ', '')
    ww = copy.deepcopy(key)
    key = []
    tmp = []
    for i in range(0, len(ww), 2):
        tmp.append(ww[i] + ww[i+1])
    li1 = tmp[0:4]
    li2 = tmp[4:8]
    li3 = tmp[8:12]
    li4 = tmp[12:16]
    key.append(li1)
    key.append(li2)
    key.append(li3)
    key.append(li4)
    bsw = key[3][1:] + key[3][:1]
    tw = []
    for i in range(len(bsw)):
        tmp = hex2bin(bsw[i])
        bin1 = int(tmp[0:4], 2)
        bin2 = int(tmp[4:8], 2)
        b = s_box[bin1][bin2]
        tw.append(b)
    if rd < 9:
        rci = hex(2**(rd-1))[2:]
    elif rd == 9:
        rci = '1b'
    else:
        rci = '36'
    x = hex2bin(tw[0])
    y = hex2bin(rci).zfill(8)
    tw[0] = bin2hex(xor(x, y))
    rs = [[] for i in range(4)]
    for i in range(4):
        tmp = hex2bin(key[0][i])
        tmp_tw = hex2bin(tw[i])
        tmp = xor(tmp, tmp_tw)
        rs[0].append(bin2hex(tmp))
    for i in range(3):
        for j in range(4):
            tmp = hex2bin(key[i+1][j])
            rs1 = hex2bin(rs[i][j])
            tmp = xor(tmp, rs1)
            rs[i+1].append(bin2hex(tmp))
    frs = ''
    for i in range(4):
        for j in range(4):
            frs += rs[i][j]
            frs += ' '
    return frs

t = ['00 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f']
t.append('00 11 22 33 44 55 66 77 88 99 aa bb cc dd ee ff')
print(t)