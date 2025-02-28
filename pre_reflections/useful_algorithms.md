

### https://rtouti.github.io/graphics/perlin-noise-algorithm?utm_source=chatgpt.com
# Perlin Noise:
 Perlin Noise is a technique developed by Ken Perlin in 1983 to create natural-looking textures and terrains in computer graphics. It generates smooth, continuous random patterns that resemble elements like clouds, landscapes, or marble. By producing coherent noise, it ensures that neighboring points have similar values, resulting in organic and realistic visuals. This method has been widely adopted in various applications, including procedural content generation in games and simulations.
 
```python
import noise
import numpy as np
import matplotlib.pyplot as plt

### Parameters
width = 100
height = 100
scale = 100.0

### Generate Perlin noise
world = np.zeros((height, width))
for i in range(height):
    for j in range(width):
        world[i][j] = noise.pnoise2(i/scale,
                                    j/scale,
                                    octaves=6,
                                    persistence=0.5,
                                    lacunarity=2.0,
                                    repeatx=1024,
                                    repeaty=1024,
                                    base=42)

### Visualize the noise
plt.imshow(world, cmap='gray')
plt.colorbar()
plt.show()
```

### https://cmaher.github.io/posts/working-with-simplex-noise/?utm_source=chatgpt.com
# Simplex Noise:
 Introduced by Ken Perlin in 2001, Simplex Noise is an improvement over the original Perlin Noise, especially for higher-dimensional applications. It reduces computational complexity and minimizes directional artifacts, making it more efficient and visually appealing in multiple dimensions. Simplex Noise achieves this by dividing space into simplices (e.g., triangles in 2D, tetrahedra in 3D) rather than the grid-based approach of Perlin Noise. This results in smoother and more isotropic textures, which are essential for realistic procedural generation.

```python
from opensimplex import OpenSimplex
import numpy as np
import matplotlib.pyplot as plt

# Initialize OpenSimplex with a seed
simp = OpenSimplex(seed=42)

# Parameters
width, height = 100, 100
scale = 50.0

# Generate OpenSimplex noise
world = np.zeros((height, width))
for y in range(height):
    for x in range(width):
        world[y][x] = simp.noise2d(x / scale, y / scale)

# Visualize the noise
plt.imshow(world, cmap='gray')
plt.colorbar()
plt.title('OpenSimplex Noise')
plt.show()
```
### https://robertheaton.com/2018/12/17/wavefunction-collapse-algorithm/
# Wave Function Collapse (WFC):
 The Wave Function Collapse algorithm, introduced by Maxim Gumin, is used in procedural content generation to produce patterns that conform to a set of constraints derived from an example input. It works by propagating possibilities through a grid, ensuring that the resulting output maintains the local structures and rules present in the source data. WFC is particularly useful for generating complex structures like architectural layouts, dungeon designs, or other patterned arrangements.

```python
// Define the tile set and their constraints
const tiles = [
    { name: 'grass', constraints: ['grass', 'road', 'water'] },
    { name: 'road', constraints: ['grass', 'road'] },
    { name: 'water', constraints: ['grass', 'water'] }
];

// Initialize the grid
const gridSize = 10;
let grid = Array(gridSize).fill().map(() => Array(gridSize).fill(null));

// Function to check if a tile can be placed at a position
function canPlaceTile(x, y, tile) {
    const neighbors = [
        { dx: -1, dy: 0 }, // left
        { dx: 1, dy: 0 },  // right
        { dx: 0, dy: -1 }, // top
        { dx: 0, dy: 1 }   // bottom
    ];

    return neighbors.every(({ dx, dy }) => {
        const nx = x + dx;
        const ny = y + dy;
        if (nx >= 0 && nx < gridSize && ny >= 0 && ny < gridSize) {
            const neighbor = grid[ny][nx];
            if (neighbor && !tile.constraints.includes(neighbor.name)) {
                return false;
            }
        }
        return true;
    });
}

// Function to collapse the wave function at a position
function collapse(x, y) {
    const possibleTiles = tiles.filter(tile => canPlaceTile(x, y, tile));
    if (possibleTiles.length > 0) {
        const selectedTile = possibleTiles[Math.floor(Math.random() * possibleTiles.length)];
        grid[y][x] = selectedTile;
    }
}

// Generate the pattern
for (let y = 0; y < gridSize; y++) {
    for (let x = 0; x < gridSize; x++) {
        collapse(x, y);
    }
}

// Display the result
console.log(grid.map(row => row.map(tile => tile ? tile.name : 'null').join(' ')).join('\n'));
```