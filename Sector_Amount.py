#!/usr/bin/env python3

#Most hard drives are divided into sectors of 512 bytes each.  Our disk has
#a size of 16 GB. Calculate how many sectors the disk has.

disk_size = 16*1024*1024*1024
sector_size = 512
sector_amount = (disk_size/sector_size)

print(sector_amount)
