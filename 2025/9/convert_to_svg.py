#!/usr/bin/env python3

def points_to_svg(input_file, output_file):
    # Read points from file
    points = []
    with open(input_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                x, y = map(int, line.split(','))
                points.append((x, y))
    
    if not points:
        print("No points found in file")
        return
    
    # Calculate bounds for viewBox
    min_x = min(p[0] for p in points)
    max_x = max(p[0] for p in points)
    min_y = min(p[1] for p in points)
    max_y = max(p[1] for p in points)
    
    # Add some padding
    padding = 100
    width = max_x - min_x + 2 * padding
    height = max_y - min_y + 2 * padding
    
    # Create SVG
    svg_lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{min_x - padding} {min_y - padding} {width} {height}">',
        '  <polyline points="'
    ]
    
    # Add all points
    point_strings = [f'{x},{y}' for x, y in points]
    svg_lines.append('    ' + ' '.join(point_strings))
    
    svg_lines.append('  " fill="none" stroke="black" stroke-width="50"/>')
    
    # Add biggest rectangle
    x1, y1 = 94523, 48719
    x2, y2 = 4733, 32241
    rect_x = min(x1, x2)
    rect_y = min(y1, y2)
    rect_width = abs(x2 - x1)
    rect_height = abs(y2 - y1)
    svg_lines.append(f'  <rect x="{rect_x}" y="{rect_y}" width="{rect_width}" height="{rect_height}" fill="none" stroke="red" stroke-width="100"/>')
    
    svg_lines.append('</svg>')
    
    # Write SVG file
    with open(output_file, 'w') as f:
        f.write('\n'.join(svg_lines))
    
    print(f"Created {output_file} with {len(points)} points")
    print(f"Bounds: x=[{min_x}, {max_x}], y=[{min_y}, {max_y}]")

if __name__ == '__main__':
    points_to_svg('9.txt', 'output.svg')
