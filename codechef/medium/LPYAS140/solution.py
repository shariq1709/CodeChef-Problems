def calculate_area(length, width):
    # Write your code here
    result=length*width
    return result
    
def main():
    length, width = map(int, input().split())
    area = calculate_area(length, width)
    print(area)


main()
