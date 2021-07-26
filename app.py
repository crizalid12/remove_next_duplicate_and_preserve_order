def remove_next_duplicate_and_preserve_order(sequence):
    result_list = []
    previous_item = sequence[0]
    current_item = sequence[1]
    result_list.append(previous_item)
    
    for next_item in sequence[2:]:
        if previous_item == current_item:
            pass
        if previous_item != current_item:
            result_list.append(current_item)
        previous_item = current_item
        current_item = next_item

    result_list.append(sequence[-1])
        
    return result_list
