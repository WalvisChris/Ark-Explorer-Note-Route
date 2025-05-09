class HilbertCurveAlgorithm:
    def __init__(self, notes, start_position):
        self.notes = notes
        self.start_position = start_position

    def hilbert_index(self, x, y, order=16):
        # Normalize x and y to fit in order-bit space
        n = 1 << order
        x = int(x / 100 * (n - 1))
        y = int(y / 100 * (n - 1))

        # Convert (x, y) to Hilbert index
        index = 0
        s = n >> 1
        while s > 0:
            rx = int((x & s) > 0)
            ry = int((y & s) > 0)
            index += s * s * ((3 * rx) ^ ry)
            if ry == 0:
                if rx == 1:
                    x, y = n - 1 - x, n - 1 - y
                x, y = y, x
            s >>= 1
        return index

    def solve(self):
        print("\033[33mHilbert Curve Ordering:\033[0m Sorting notes based on Hilbert curve...")
        sorted_notes = sorted(self.notes, key=lambda note: self.hilbert_index(note.position[0], note.position[1]))

        print(f"\033[33mHilbert Curve Ordering:\033[0m Sorted {len(self.notes)} notes using Hilbert curve.")

        # Insert starting point first
        route = [self.start_position]
        current_position = self.start_position

        for idx, note in enumerate(sorted_notes):
            route.append(note.position)
            # Print progress after every 10 notes processed
            if idx % 10 == 0:
                print(f"\033[33mHilbert Curve Ordering:\033[0m Added {idx+1}/{len(sorted_notes)} notes to the route.")

        print("\033[33mHilbert Curve Ordering:\033[0m Route completed.")

        return route[1:]  # remove start from result if needed