def print_pyramid(size, char='*'):
  """Print a pyramid pattern"""
  for i in range(1, size + 1):
    print(' ' * (size - i) + char * (2 * i - 1))

def print_diamond(size, char='*'):
  """Print a diamond pattern"""
  for i in range(1, size + 1):
    print(' ' * (size - i) + char * (2 * i - 1))
  for i in range(size - 1, 0, -1):
    print(' ' * (size - i) + char * (2 * i - 1))

def print_number_triangle(size):
  """Print a number triangle"""
  for i in range(1, size + 1):
    for j in range(1, i + 1):
      print(j, end=' ')
    print()

def print_floyds_triangle(size):
  """Print Floyd's triangle"""
  num = 1
  for i in range(1, size + 1):
    for j in range(i):
      print(num, end=' ')
      num += 1
    print()

def print_inverted_pyramid(size, char='*'):
  """Print an inverted pyramid"""
  for i in range(size, 0, -1):
    print(' ' * (size - i) + char * (2 * i - 1))

def main():
  print("=== Pattern Printer ===")
  print("1. Pyramid")
  print("2. Diamond")
  print("3. Number Triangle")
  print("4. Floyd's Triangle")
  print("5. Inverted Pyramid")
  
  choice = input("\nChoose pattern (1-5): ").strip()
  size = int(input("Enter size: "))
  
  if choice == '1':
    char = input("Enter character (default '*'): ").strip() or '*'
    print_pyramid(size, char)
  elif choice == '2':
    char = input("Enter character (default '*'): ").strip() or '*'
    print_diamond(size, char)
  elif choice == '3':
    print_number_triangle(size)
  elif choice == '4':
    print_floyds_triangle(size)
  elif choice == '5':
    char = input("Enter character (default '*'): ").strip() or '*'
    print_inverted_pyramid(size, char)
  else:
    print("Invalid choice!")

if __name__ == "__main__":
  main()