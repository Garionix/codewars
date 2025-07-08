# возвращает маску строки
def maskify(cc):
    mask_array = list(cc)
    if len(mask_array) < 5:
        return ''.join(mask_array)
    else:
        for n in range(0, len(mask_array) - 4):
            mask_array[n] = '#'
    
    return ''.join(mask_array)


print(maskify(''))