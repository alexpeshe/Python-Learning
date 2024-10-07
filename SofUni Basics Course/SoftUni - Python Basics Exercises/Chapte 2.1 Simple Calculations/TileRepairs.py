p_ground_side_length = int(input())
tile_width = float(input())
tile_length = float(input())
bench_width = int(input())
bench_length = int(input())

playground = p_ground_side_length*p_ground_side_length

bench = bench_width*bench_length

playground_to_cover = playground - bench

tile_ground = tile_width*tile_length

tiles_needed = playground_to_cover/tile_ground
time_needed = tiles_needed*0.2

print(tiles_needed)
print(time_needed)



