
# Virtual to Physical Address Translation

page_size = 1024

page_table = {
    0: 5,
    1: 2,
    2: None,
    3: 7
}

virtual_addresses = [500, 1500, 2500, 3500]

print("Virtual Address Translation")
print("-" * 85)

print(f"{'Virtual':<12}{'Page':<10}{'Offset':<12}"
      f"{'Frame':<12}{'Physical Address / Status'}")

print("-" * 85)

for va in virtual_addresses:

    # Calculate page number and offset
    page_number = va // page_size
    offset = va % page_size

    # Check page table
    frame = page_table.get(page_number)

    if frame is not None:
        # Calculate physical address
        physical_address = frame * page_size + offset

        print(f"{va:<12}{page_number:<10}{offset:<12}"
              f"{frame:<12}{physical_address}")
    else:
        print(f"{va:<12}{page_number:<10}{offset:<12}"
              f"{'-':<12}Page Fault")

print("-" * 85)
