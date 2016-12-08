def get_location_from_string(string_location):
    comaIdx = string_location.index(',')
    posX = int(string_location[0:comaIdx])
    posY = int(string_location[comaIdx + 1:])
    return (posX, posY)
