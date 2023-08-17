import pygame
from queue import PriorityQueue
from astar import algorithm
from ressources.spot_class import Spot
from ressources.helper_functions import make_grid, draw_grid, draw, get_clicked_pos, reconstruct_path, h

pygame.display.set_caption("Path Finding Algorithm!")

def main(win, width):
	ROWS = 50
	grid = make_grid(ROWS, width)

	start = None
	end = None

	run = True
	while run:
		draw(win, grid, ROWS, width)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			if pygame.mouse.get_pressed()[0]: # LEFT
				pos = pygame.mouse.get_pos()
				row, col = get_clicked_pos(pos, ROWS, width)
				spot = grid[row][col]
				if not start and spot != end:
					start = spot
					start.make_start()

				elif not end and spot != start:
					end = spot
					end.make_end()

				elif spot != end and spot != start:
					spot.make_barrier()

			elif pygame.mouse.get_pressed()[2]: # RIGHT
				pos = pygame.mouse.get_pos()
				row, col = get_clicked_pos(pos, ROWS, width)
				spot = grid[row][col]
				spot.reset()
				if spot == start:
					start = None
				elif spot == end:
					end = None

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE and start and end:
					for row in grid:
						for spot in row:
							spot.update_neighbors(grid)

					algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)

				if event.key == pygame.K_c:
					start = None
					end = None
					grid = make_grid(ROWS, width)

	pygame.quit()

main(pygame.display.set_mode((500, 500)), 900)
