# 86028 too low :(

def main():
    with open('input.txt', 'r') as file:
        entries = file.readline().split(',')
        
        boxes = [[] for _ in range(256)]
        
        for entry in entries:
            label = get_label(entry)
            box_idx = calcHash(label)
            
            if entry[-1].isnumeric(): # add lens
                lens_length = int(entry[-1])
                
                replaced = False
                for li, lens in enumerate(boxes[box_idx]):
                    if lens[0] == label:
                        boxes[box_idx][li] = (label, lens_length)
                        replaced = True
                        break
                if not replaced:
                    boxes[box_idx].append((label, lens_length))
            else: # remove
                for lens in boxes[box_idx]:
                    if lens[0] == label:
                        boxes[box_idx].remove(lens)
                        break
        print(calculate_result(boxes))    

def get_label(entry):
    return entry.split('=')[0].split('-')[0]

def calculate_result(boxes):
    total_sum = 0
    for bi, box in enumerate(boxes):
        for li, lens in enumerate(box):
            total_sum += (bi + 1) * (li + 1) * lens[-1]
    return total_sum

def calcHash(str):
    num = 0
    for char in str:
        num = ((num + ord(char)) * 17 ) % 256
    return num

if __name__ == "__main__":
    main()