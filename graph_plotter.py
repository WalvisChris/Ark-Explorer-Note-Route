import math
import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.widgets import Button
from utils import get_total_distance, load_notes

class GraphPlotter:
    def __init__(self, background_image_path='theislandmap2.jpg'):
        self.bg_img = mpimg.imread(background_image_path)
    
    def plot_route(self, route, starting_position, title="", showLabels=False, showStart=True, showCurrent=True):
        starting_x, starting_y = starting_position
        
        # Remove starting pos from route
        if starting_position in route:
            route.remove(starting_position)
        
        # get note names
        notes = load_notes()
        position_to_name = {note.position: note.name for note in notes}
        
        # Set up the plot
        fig = plt.figure(figsize=(10, 10))
        fig.canvas.manager.set_window_title(title)
        plt.xlim(0, 100)
        plt.ylim(0, 100)
        plt.imshow(self.bg_img, extent=[0, 100, 0, 100], zorder=0)

        # Add title if provided
        text = f"{title} ({math.floor(get_total_distance(route) * 10 + 0.5) / 10}m)"
        plt.title(text, fontsize=16)

        # First line from start to first note
        if showStart:
            plt.scatter(starting_y, 100 - starting_x, color='lime', s=100, zorder=2)
            first_y, first_x = route[0]
            plt.plot(
                [starting_y, first_x],
                [100 - starting_x, 100 - first_y],
                marker='o', color='lime', linewidth=2, markersize=3, zorder=1
            )

        dots = []
        
        # Draw route
        for i in range(len(route) - 1):
            y1, x1 = route[i]
            y2, x2 = route[i + 1]

            y1_flipped = 100 - y1
            y2_flipped = 100 - y2

            plt.plot(
                [x1, x2], [y1_flipped, y2_flipped],
                marker='o', color='r', linewidth=2, markersize=3, zorder=1
            )

            dot1, = plt.plot(x1, y1_flipped, 'o', color='red', markersize=3, zorder=2)
            dots.append(dot1)

            if showLabels:
                label = f"({y1}, {x1})"
                plt.text(x1, y1_flipped + 1, label, fontsize=8, ha='center', va='bottom', color='black', fontweight='bold', zorder=3)
            
            #plt.pause(0.1)

        # add last point to route
        if showLabels:
                label = f"({y2}, {x2})"
                plt.text(x2, y2_flipped + 1, label, fontsize=8, ha='center', va='bottom', color='black', fontweight='bold', zorder=3)

        # route interaction button
        button_next_plt = fig.add_axes([0.1, 0.46, 0.07, 0.02])
        button_prev_plt = fig.add_axes([0.1, 0.44, 0.07, 0.02])
        button_rand_plt = fig.add_axes([0.1, 0.42, 0.07, 0.02])
        button_rest_plt = fig.add_axes([0.1, 0.40, 0.07, 0.02])

        button_next = Button(button_next_plt, 'Next note')
        button_previous = Button(button_prev_plt, 'Previous note')
        button_random = Button(button_rand_plt, 'Random note')
        button_reset = Button(button_rest_plt, 'Reset route')
        
        note_index = [0]

        def next_note(event):
            note_index[0] = (note_index[0] + 1) % len(route)
            update_text()

        def previous_note(event):
            note_index[0] = len(route) - 1 if note_index[0] < 1 else note_index[0] - 1
            update_text()

        def random_note(event):
            note_index[0] = random.randint(0, len(route) - 1)
            update_text()

        def reset_note(event):
            note_index[0] = 0
            update_text()

        def update_text():
            if showCurrent:
                for dot in dots:
                    dot.set_color('red')
                    dot.set_markersize(3)

                dots[note_index[0]].set_color('cyan')
                dots[note_index[0]].set_markersize(6)

            txt = f"{position_to_name[route[note_index[0]]]}\n{route[note_index[0]]}"
            text.set_text(txt)
            fig.canvas.draw_idle()

        button_next.on_clicked(next_note)
        button_previous.on_clicked(previous_note)
        button_random.on_clicked(random_note)
        button_reset.on_clicked(reset_note)

        text = plt.figtext(0.1, 0.5, "empty", wrap=True, ha='left', va='center', fontsize=10)     
        update_text()
   
        plt.show()