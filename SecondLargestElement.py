def get_secondLargest(arr):
    second_max = float("-inf")
    max = float("-inf")

    for i in range(0,len(arr)):
        item = arr[i]
        if item>max:
            second_max=max
            max=item
        elif item>second_max and item<max:
            second_max=item

            return -1 if second_max== float("-inf")else second_max

