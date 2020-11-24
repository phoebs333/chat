
def read_file(filename):
    lines=[]
    with open (filename,'r', encoding='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    person = None
    phoebe_word_count = 0
    phoebe_sticker_count = 0
    phoebe_image_count = 0
    bea_word_count = 0
    bea_sticker_count = 0
    bea_image_count = 0
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Phoebe': 
            if s[2] =='貼圖':
                phoebe_sticker_count += 1
            elif s[2] == '圖片':
                phoebe_image_count += 1
            else:
                for m in s[2:]:
                    phoebe_word_count += len(m)
        elif name == 'Bea':
            if s[2] == '貼圖':
                bea_sticker_count += 1
            elif s[2] == '圖片':
                bea_image_count += 1
            else:
                for m in s[2]:
                    bea_word_count += len(m)
    print ('Phoebe說了', phoebe_word_count, '個字')
    print ('Phoebe傳了', phoebe_sticker_count, '個貼圖')
    print ('Phoebe傳了', phoebe_image_count,'張圖片')

    print('Bea說了', bea_word_count, '個字')
    print('Bea傳了', bea_sticker_count, '個貼圖')
    print ('Bea傳了', bea_image_count,'張圖片')

def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')

def main():
    lines = read_file('[LINE]Bea Lee.txt')
    lines = convert(lines)
    #write_file('output.txt', lines)

main()